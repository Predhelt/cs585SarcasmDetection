## Input file should be in the form:
## vod ID
## text line 1
## text line 2
## ...
## empty line
## vod ID (Repeat)

def index_text(chat_file): # uses all-parsed file
    # index shape: vod{vod_name:chat[line[text]]}
    vods = {}
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
                    vods[vod_id] = chat_index
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
    # for vec in indx:
    #    fv.append(_compute_features(vec))
    

def _compute_features(vec):
    vec.append(_word_count())
    vec.append(_char_count())
    vec.append(_endswith_exclain())
    vec.append(_endswith_question())
    return vec

def output_features(neg_fv, pos_fv, of): # fv = feature vector, of = output file
    # file.write(neg_fv + pos_fv)

# FEATURES GO HERE
def _word_count(): # TODO
    return

def _char_count(): # TODO remove?
    return

def _endswith_exclaim(): # TODO
    return

def _endswith_question(): # TODO
    return


if __name__ == '__main__':
    neg_data_file = 'labelled_data/0.txt'
    pos_data_file = 'labelled_data/1.txt'
    neg_indx = index_text(neg_data_file)
    pos_indx = index_text(pos_data_file)
    neg_fv = create_fv(neg_indx)
    pos_fv = create_fv(pos_indx)
    of = 'data/data.csv'
    output_features(neg_fv, pos_fv, of)
