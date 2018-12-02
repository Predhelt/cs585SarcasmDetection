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

def index_text(chat_file): # uses the all-parsed file
    # index shape: vod[(vod_ID, chat[line[text]])]
    vods = []
    chat_index = []
    
    with open(chat_file, 'r', encoding='utf-8') as fp:
        vod_id = fp.readline() # first line is vod ID
        line = fp.readline()
        
        while line:
            if line == '\n': # empty line, end of previous vod
                line = fp.readline()
                if line: # line has ID of vod
                    vods.append((vod_id, chat_index))
                    vod_id = line
                    
                    line = fp.readline()
                    chat_index = []
                else:
                    break # eof
            
            li = line.split() # make list of words
            
            chat_index.append(li) # add list of words to index

            line = fp.readline()
        vods.append((vod_id, chat_index)) # put last vod in the index
    return vods

def create_fv(indx):
    fv = []
    f_names = [] # list of names of features

    _add_feature_names(f_names)
    fv.append(f_names)
    _add_features(indx, fv)
    return fv

def create_train_fv(indx, label):
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
    fn.append('exclaiming')
    fn.append('questioning')
    fn.append('sentiment score')
    
    return

def _add_features(indx, fv, lbl=-1):
    for vod in indx: # (vod_id, chat_info)
        for line_num in range(len(vod[1])):
            vec = _compute_features(vod, line_num)
            if lbl >= 0:
                vec.append(lbl)
            fv.append(vec)
    
def _compute_features(vod, line_num):
    # vod is in the form (vod_ID, chat[line[text]])
    vec = []
    vec.append(_endswith_exclaim())
    vec.append(_endswith_question())
    vec.append(_sentiment_score())
    # ADD MORE FEATURE FUNCTION CALLS HERE
    return vec

# FEATURES GO HERE
# All feature values should be in the range -inf < x < inf
def _endswith_exclaim(): # TODO
    return 0

def _endswith_question(): # TODO
    return 0

def _sentiment_score(): # TODO
    return 0

def output_training(neg_fv, pos_fv, of): # fv = feature vector, of = output file
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

def output_test(fv, of):
    file = open(of, 'w')
    for vec in fv:
        o = ''
        for f in vec:
            o += str(f) + ', '
        file.write(o[:-2] + '\n') # remove last comma and space

def index_folder(chat_folder):
    # index shape: vod[(vod_ID, chat[line[text]])]
    vods = []
    chat_index = []

    for chat_file in chat_folder:
        with open(chat_file, 'r', encoding='utf-8') as fp:
            line = fp.readline()
            
            while line:
                li = line.split() # make list of words
                
                chat_index.append(li) # add list of words to index

                line = fp.readline()
        vod_id = chat_file.split('/')[-1].split('.')[0]
        vods.append((vod_id, chat_index)) # put vod in the index
    return vods


if __name__ == '__main__':
    neg_data_file = 'data/labelled_data/0.txt'
    pos_data_file = 'data/labelled_data/1.txt'
    neg_indx = index_text(neg_data_file)
    pos_indx = index_text(pos_data_file)
    neg_fv = create_train_fv(neg_indx, 0)
    pos_fv = create_train_fv(pos_indx, 1)
    of_tr = 'data/train_data.csv'
    output_training(neg_fv, pos_fv, of_tr)

    test_dir = 'data/test_data/'
    filenames = np.array([(test_dir + f) for f in listdir(test_dir) if isfile(join(test_dir, f))])
    indx = index_folder(filenames)
    fv = create_fv(indx)
    of_ts = 'data/test_data.csv'
    output_test(fv, of_ts)

