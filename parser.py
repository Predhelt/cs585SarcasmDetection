import numpy as np
from os import listdir
from os.path import isfile, join

def parse_chat(chat_file, raw_path):
    #chat_file = "mfbiscuits.txt"

    chat_name = chat_file.lstrip(raw_path)
    file_name = "parsed_data/" + chat_name + "-parsed.txt"
    parsed_chat = open(file_name, "w", encoding='utf-8')
    with open(chat_file, encoding='utf-8') as fp:
        line = fp.readline()
        while line:
            # '[*] <*> +'
            message = "".join(line.split('> ')[1:]) # text starts after the first occurrence
            #print(message)
            #if( == ):
            #print("TRUE")
            #statement_with_usernames = "{}".format(line[11:].strip())
            #start_index = statement_with_usernames.find('>')
            #statement = statement_with_usernames[start_index+1:]
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
        while line:
            if line == '\n': # empty line, end of previous vod
                line = fp.readline()
                if line: # line has name of vod
                    vods[vod_name] = chat_index
                    vod_name = line
                    
                    line = fp.readline
                    chat_index = []
                    line_num = 0
                else:
                    break # eof
            wi = line.split(' ')
            
            chat_index.append(wi)

            line = fp.readline()
            line_num += 1
    print(vods.keys())
    
            

if __name__ == '__main__':
    mypath = 'raw_data/'
    filenames = np.array([(mypath + f) for f in listdir(mypath) if isfile(join(mypath, f))])
    #print(filenames)
    #parse_all_chats(filenames, mypath)
    index_text('parsed_data/all-parsed.txt')
    
    #for file in filenames:
        #parse_chat(file, mypath)
        #index_text(file, mypath)
