import numpy as np
from os import listdir
from os.path import isfile, join
import re
import operator

def parse_chat(chat_file, raw_path):
    #chat_file = "mfbiscuits.txt"

    chat_name = chat_file.lstrip(raw_path)
    file_name = "parsed_data/" + chat_name + "-parsed.txt"
    parsed_chat = open(file_name, "w", encoding='utf-8')
    with open(chat_file, encoding='utf-8') as fp:
        line = fp.readline()
        while line:
            message = "".join(line.split('> ')[1:]) # text starts after the first occurrence
            parsed_chat.write(message.lower())
            line = fp.readline()
            
    parsed_chat.close()

def parse_all_chats(chat_files, raw_path):
    #Format:
    #line 1: name of vod
    #subsequent lines until blank line: lines of vod
    #next line with text: name of next vod
    
    file_name = "parsed_data/all-parsed.txt"
    parsed_chat = open(file_name, "w", encoding='utf-8')
    for chat_file in chat_files:
        chat_name = chat_file.lstrip(raw_path)[:-4]
        
        with open(chat_file, encoding='utf-8') as fp:
            parsed_chat.write(chat_name + '\n')
            line = fp.readline()
            while line:
                message = "".join(line.split('> ')[1:]) # text starts after the first occurrence
                parsed_chat.write(message.lower())
                line = fp.readline()
            parsed_chat.write('\n') # empty line to denote end of file
        
    parsed_chat.close()

def index_text(chat_file): # uses all-parsed file
    # index shape: vod{vod_name:chat[line[text]]}
    vods = {}
    chat_index = []
    
    with open(chat_file, 'r', encoding='utf-8') as fp:
        vod_name = fp.readline() # first line is vod name
        line = fp.readline()
        
        line_num = 0
        vod_count = 0
        while line:
            if line == '\n': # empty line, end of previous vod
                line = fp.readline()
                if line: # line has name of vod
                    vod_count += 1
                    vods[vod_name] = chat_index
                    vod_name = line
                    
                    line = fp.readline()
                    chat_index = []
                    line_num = 0
                else:
                    break # eof
            
            li = line.split() # make list of words
            
            chat_index.append(li) # add list of words to index

            line = fp.readline()
            line_num += 1
        vods[vod_name] = chat_index # put last vod in the index
    return vods
    #for vod in vods.keys():
    #    print(vods[vod][:10])
    
def word_counts(index):
    wl = {} # word list dictionary
    for vod in index.values():
        for message in vod:
            for word in message:
                # parse words to remove commas
                word = check_word(word)
                word = word.split('/')
                for w in word:
                    if w == '':
                        continue
                    if w not in wl.keys():
                        wl[w] = 1
                    else:
                        wl[w] = wl[w] + 1
    return wl

def check_word(w):
    #stopwords = []
    olws = re.compile('[a-z0-9\^@]') # valid one-letter words
    http = re.compile('.*https?://.+') # check for http link
    marks = re.compile('[^a-z0-9\-_\'\\/]') # contains certain marks
    initials = re.compile('[a-z]\.[a-z]\.+') # initialism
    
    #print(w)
    if(len(w) == 1):
        if(not olws.match(w)):
            return ''
        else: return w

    if(http.match(w)):
        return ''
        
    ms = marks.finditer(w)
    i = 0
    for mi in ms:
        mi = mi.start()
        if(len(w)-1 == mi or not initials.match(w[mi-i:])):
            #print("mark found at index", mi-i)
            if(mi == 0):
                w = w[1:]
            else:
                w = w[:mi-i] + w[mi+1-i:]
            #print(w)
        i += 1
    return w
    
##def check_words(w):
##    thisorthat = re.compile('\w+/\w+') # ex: this/that
##    if thisorthat.match(w)
##        return w.split('/') # IMPROVE: doesn't consider edge cases
##    else: return [w]

def wl_sorted_output(wl):
    #sort it from most common word to least common word
    sorted_wl = sorted(wl.items(), key=operator.itemgetter(1), reverse=True)
    wlf = open('word_counts.csv', 'w', encoding='utf-8')
    for word in sorted_wl:
        output = str(word[0]) + ', ' + str(word[1]) + '\n'
        #print(output)
        wlf.write(output)
    wlf.close()
    
            

if __name__ == '__main__':
    #mypath = 'raw_data/'
    #filenames = np.array([(mypath + f) for f in listdir(mypath) if isfile(join(mypath, f))])
    #print(filenames)
    #parse_all_chats(filenames, mypath)
    indx = index_text('parsed_data/all-parsed.txt') # Get inverted index of vods
    wl = word_counts(indx) # get the word counts of each word
    wl_sorted_output(wl) # output sorted word counts to predetermined file
    #for file in filenames:
        #parse_chat(file, mypath)
        #index_text(file, mypath)
