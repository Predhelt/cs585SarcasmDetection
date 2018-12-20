## Input file should be in the form:
## vod ID
## text line 1
## text line 2
## ...
## empty line
## vod ID (Repeat)...

import numpy as np
from os import listdir
from os.path import isfile, join
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
def index_text(chat_file): # uses any raw data file
    # index shape: chat[line[text]]
    chat_list = []
    
    with open(chat_file, 'r', encoding='utf-8', errors='replace') as fp:
        line = fp.readline()
        while line:
            if line == '':
                continue
            
            li = line.split() # make list of words
            
            chat_list.append(li[2:]) # add list of words to index
            # removes the timestamp and username because they are not being used

            line = fp.readline()
    return chat_list

def index_kyle_text(chat_file): # uses any data files formatted by kyle
    # index shape: chat[line[text]]
    neg_list = []
    pos_list = []

    with open(chat_file, 'r', encoding='utf-8', errors='replace') as fp:
        line = fp.readline()

        while line:
            if line == '':
                continue

            li = line.split() # make list of words

            if li[0] == 'n':
                neg_list.append(li[1:]) # add list of words to index
            elif li[0] == 's':
                pos_list.append(li[1:])
            else:
                continue

            line = fp.readline()
    return neg_list, pos_list

def create_field_fv(indx):
    fv = []
    f_names = [] # list of names of features

    _add_feature_names(f_names)
    fv.append(f_names)
    _add_features(indx, fv)
    return fv

def create_fv(indx, label):
    # same as create_fv but adds label at the end of each line
    fv = []
    f_names = [] # list of names of features

    _add_feature_names(f_names)
    f_names.append('label')
    fv.append(f_names)
    _add_features(indx, fv, lbl=label)
    return fv

def _add_feature_names(fn):
    # Makes sure the names are in the same order as in _compute_features()
    fn.append('exclaiming_end')
    fn.append('questioning_end')
    #f_names.append('sentiment score')
    fn.append('uppercase_word_count')
    fn.append('people_tagged')
    fn.append('#_of_exclamations')
    fn.append('#_of_questions')
    fn.append('punctuation_pairs')
    fn.append('sentiment score')
    fn.append('overall sentiment score')
    
    return

def _add_features(indx, fv, lbl=-1):
    for line in indx: # chat_info
        vec = _compute_features(line)
        if lbl >= 0:
            vec.append(lbl)
        fv.append(vec)
    
def _compute_features(line):
    # vod is in the form (vod_ID, chat[line[text]])
    vec = []
    vec.append(_endswith_char(line, '!'))
    vec.append(_endswith_char(line, '?'))
    vec.append(_uppercase_words(line))
    vec.append(_people_tagged(line))
    vec.append(_character_count(line, '!'))
    vec.append(_character_count(line, '?'))
    vec.append(_punctuation_pairs(line))
    vec.append(_sentiment_score(line))
    vec.append(_overall_sentiment(line))
    # ADD MORE FEATURE FUNCTION CALLS HERE
    return vec

# FEATURES GO HERE
# All feature values should be in the range -inf < x < inf
def _endswith_char(line, char):
    lastword = line[-1]
    if line[-1] == char:
        return 1
    return 0

#Calculates difference in sentiments
def _sentiment_score(line):
    string = ""
    for s in line:
        string += s + " "
    analyzer = SentimentIntensityAnalyzer()
    vec = analyzer.polarity_scores(string)
    return abs(vec['neg'] - vec['pos']) - vec['neu']

#Gets the overall sentiment of a line
def _overall_sentiment(line):
    string = ""
    for s in line:
        string += s + " "
    analyzer = SentimentIntensityAnalyzer()
    vec = analyzer.polarity_scores(string)
    return vec['compound']

#Returns percentage of words that are uppercase 0<= x <= 1
def _uppercase_words(line):
    count = 0
    
    num_chars = 0
    for word in line:
        if word.isupper():
            count += 1
        num_chars += len(word)
    return float(count/num_chars)

#Returns number of times certain character is present in line. Usually check for '!' or '?' Default for character = !
def _character_count(line, character = '!'):
    count = 0
    
    for word in line:
        for c in word:
            if c == character:
                count+=1
    return count

#Return number of people tagged in statement. Used to denote conversation.
def _people_tagged(line):
    
    count = 0
    for word in line:
        if word[0] == '@':
            count+=1
    return count

#Return pairs of expressive punctuation. Example: Where is my supersuit!?!?!?!!!?? should return 5
def _punctuation_pairs(line):
    punc_list = ['!', '?']
    count = 0
    

    #print(line)
    for i in range(len(line)): # index i is the current word
        #print(line[i], len(line), i)
        for j in range(len(line[i])): # index j is the current char
            #print(len(line[i]), j)
            if j >= len(line[i])-1: # index j out of range of word
                if i < len(line)-1: # index i not out of range
                    first = line[i][j]
                    second = line[i+1][0]
                else:
                    break
            else:
                first = line[i][j]
                second = line[i][j+1]
            if first in punc_list and second in punc_list:
                count += 1
                j = j + 2
                continue
    return count
  
def output_data(neg_fv, pos_fv, of): # fv = feature vector, of = output file
    # file.write(neg_fv + pos_fv)
    file = open(of, 'w')
    for vec in neg_fv:
        o = ''
        for f in vec:
            o += str(f) + ', '
        file.write(o[:-2] + '\n') # remove last comma and space
    for vec in pos_fv[1:]:
        o = ''
        for f in vec:
            o += str(f) + ', '
        file.write(o[:-2] + '\n') # remove last comma and space
    file.close()

def output_field(fv, of):
    file = open(of, 'w')
    for vec in fv:
        o = ''
        for f in vec:
            o += str(f) + ', '
        file.write(o[:-2] + '\n') # remove last comma and space
    file.close()

def index_folder(chat_folder):
    # index shape: chat[line[text]]
    indx = []

    for chat_file in chat_folder:
        with open(chat_file, 'r', encoding='utf-8') as fp:
            line = fp.readline()
            words = []
            
            while line:
                li = line.split() # make list of words
                
                words.append(li) # add each word to the list

                line = fp.readline()
            indx.append(words) # put vod in the index
    return indx


if __name__ == '__main__':
    neg_data_file = 'data/labelled_data/0.txt'
    pos_data_file = 'data/labelled_data/1.txt'
    neg_indx = index_text(neg_data_file)
    pos_indx = index_text(pos_data_file)
    neg_fv = create_fv(neg_indx, 0)
    pos_fv = create_fv(pos_indx, 1)
    of_tr = 'data/data.csv'
    print(len(neg_fv), type(neg_fv))
    print(len(pos_fv), type(pos_fv))
    output_data(neg_fv, pos_fv, of_tr)

    test_data_file = 'data/labelled_data/ParsedTestData.txt'
    neg_indx, pos_indx = index_kyle_text(test_data_file)
    neg_fv = create_fv(neg_indx, 0)
    pos_fv = create_fv(pos_indx, 1)
    of_tr = 'data/test_data1.csv'
    print(len(neg_fv), type(neg_fv))
    print(len(pos_fv), type(pos_fv))
    output_data(neg_fv, pos_fv, of_tr)
