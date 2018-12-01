## Input file should be in the form:
## vod ID
## text line 1
## text line 2
## ...
## empty line
## vod ID (Repeat)...

def index_text(chat_file, label): # uses the all-parsed file
    # index shape: vod[(vod_ID, chat[line[text]])]
    vods = []
    chat_index = []
    
    with open(chat_file, 'r', encoding='utf-8') as fp:
        vod_id = fp.readline() # first line is vod ID
        line = fp.readline()
        
        line_num = 0
        vod_count = 0
        while line:
            if line == '\n': # empty line, end of previous vod
                line = fp.readline()
                if line: # line has ID of vod
                    vod_count += 1
                    vods.append((vod_id, chat_index))
                    vod_id = line
                    
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

def create_fv(indx):
    fv = []
    f_names = [] # list of names of features

    f_names.append('exclaiming')
    f_names.append('questioning')
    f_names.append('sentiment score')
    
    f_names.append('label')

    fv.append(f_names)
    
    for line in indx: # (vod_id, chat_info)
        fv.append(_compute_features(line))
    

def _compute_features(line, label):
    vec = []
    vec.append(_endswith_exclaim(line))
    vec.append(_endswith_question(line))
    vec.append(_sentiment_score(line))
    # ADD MORE FEATURE FUNCTION CALLS HERE
    vec.append(label)
    return vec

def output_features(neg_fv, pos_fv, of): # fv = feature vector, of = output file
    # file.write(neg_fv + pos_fv)
    file = open(of, 'w')
    for vec in neg_fv:
        line = ''
        for f in vec:
            line += f + ', '
        file.write(line[:-2] + '\n') # remove last comma and space

# FEATURES GO HERE
# All feature values should be in the range 0 <= x < inf
def _endswith_exclaim(line): # TODO
    return 0

def _endswith_question(line): # TODO
    return 0

def _sentiment_score(line): # TODO
    return 0


if __name__ == '__main__':
    neg_data_file = 'labelled_data/0.txt'
    pos_data_file = 'labelled_data/1.txt'
    neg_indx = index_text(neg_data_file)
    pos_indx = index_text(pos_data_file)
    neg_fv = create_fv(neg_indx, 0)
    pos_fv = create_fv(pos_indx, 1)
    of = 'data/data.csv'
    output_features(neg_fv, pos_fv, of)
