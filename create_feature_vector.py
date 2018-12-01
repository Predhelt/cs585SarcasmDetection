## Input file should be in the form:
## vod ID
## text line 1
## text line 2
## ...
## empty line
## vod ID (Repeat)...

#LINE FORMAT IS (vod_id, chat_info)
#chat[line[text]]
def index_text(chat_file): # uses the all-parsed file
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
        vods.append((vod_id, chat_index)) # put last vod in the index
    return vods

def create_fv(indx, label):
    fv = []
    f_names = [] # list of names of features

    f_names.append('exclaiming_end')
    f_names.append('questioning_end')
    #f_names.append('sentiment score')
    f_names.append('uppercase_word_count')
    f_names.append('people_tagged')
    f_names.append('#_of_exclamations')
    f_names.append('#_of_questions')
    f_names.append('punctuation_pairs')
    f_names.append('label')

    fv.append(f_names)

    for line in indx: # (vod_id, chat_info)
        fv.append(_compute_features(line, label))
    return fv


def _compute_features(line, label):
    vec = []
    vec.append(_endswith_exclaim(line))
    vec.append(_endswith_question(line))
    vec.append(_uppercase_words(line))
    vec.append(_people_tagged(line))
    vec.append(_character_count(line, '!'))
    vec.append(_character_count(line, '?'))
    vec.append(_punctuation_pairs(line))
   # vec.append(_sentiment_score(line))
    # ADD MORE FEATURE FUNCTION CALLS HERE
    vec.append(label)
    return vec

# FEATURES GO HERE
# All feature values should be in the range 0 <= x < inf
#return 1 if line ends with exclamation point. 0 if not.
def _endswith_exclaim(line): # TODO
    text = line[1][0][2]
    if text[-1] == '!':
        return 1
    return 0

def _endswith_question(line): # TODO
    text = line[1][0][2]
    if text[-1] == '?':
        return 1
    return 0

def _sentiment_score(line): # TODO
    text = line[1][0][2]
    tokens = text.lower().split()
    return 0

#Returns percentage of words that are uppercase 0<= x <= 1
def _uppercase_words(line):
    count = 0
    text = line[1][0][2]
    tokens = text.split()
    for word in tokens:
        if word.isupper():
            count += 1
    return float(count/len(tokens))

#Returns number of times certain character is present in line. Usually check for '!' or '?' Default for character = !
def _character_count(line, character = '!'):
    count = 0
    text = line[1][0][2]
    for c in text:
        if c == character:
            count+=1
    return count

#Return number of people tagged in statement. Used to denote conversation.
def _people_tagged(line):
    text = line[1][0][2]
    tokens = text.split()
    count = 0
    for word in tokens:
        if word[0] == '@':
            count+=1
    return count

#Return pairs of expressive punctuation. Example: Where is my supersuit!?!?!?!!!?? should return 5
def _punctuation_pairs(line):
    punc_list = ['!', '?']
    count = 0
    text = line[1][0][2]
    for i in range(0, len(text)-1):
        first = text[i]
        second = text[i+1]
        if first in punc_list and second in punc_list:
            count += 1
            i = i + 2
            continue
    return count

def output_features(neg_fv, pos_fv, of): # fv = feature vector, of = output file
    # file.write(neg_fv + pos_fv)
    file = open(of, 'w')
    for vec in neg_fv:
        line = ''
        for f in vec:
            line += str(f) + ', '
        file.write(line[:-2] + '\n') # remove last comma and space
    for vec in pos_fv[1:]:
        line = ''
        for f in vec:
            line += str(f) + ', '
        file.write(line[:-2] + '\n') # remove last comma and space

if __name__ == '__main__':
    neg_data_file = 'data/labelled_data/0.txt'
    pos_data_file = 'data/labelled_data/1.txt'
    neg_indx = index_text(neg_data_file)
    pos_indx = index_text(pos_data_file)
    neg_fv = create_fv(neg_indx, 0)
    pos_fv = create_fv(pos_indx, 1)
    of = 'data/data.csv'
    output_features(neg_fv, pos_fv, of)
