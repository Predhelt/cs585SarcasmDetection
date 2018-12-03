
#Naive Bayes done using the "bag of words" approach in HW1
sarc_dic = {}
sarc_wcount = 0
nsarc_dic = {}
nsarc_wcount = 0
vocab = set()
alpha = 0.1

#Gets word counts in parsed sarcasm data
def get_sarc_word_counts(chat_log):
    global sarc_dic
    global sarc_wcount
    file = open(chat_log, "r", encoding="utf-8")
    for line in file:
        for token in line.split():
            sarc_wcount = sarc_wcount + 1
            if token not in vocab:
                vocab.add(token)
            if token not in sarc_dic.keys():
                sarc_dic[token] = 1
            else:
                sarc_dic[token] = sarc_dic[token] + 1
    file.close()

#Gets word counts in parsed not sarcasm data
def get_nsarc_word_counts(chat_log):
    global nsarc_dic
    global nsarc_wcount
    file = open(chat_log, "r", encoding="utf-8")
    for line in file:
        for token in line.split():
            nsarc_wcount = nsarc_wcount + 1
            if token not in vocab:
                vocab.add(token)
            if token not in nsarc_dic.keys():
                nsarc_dic[token] = 1
            else:
                nsarc_dic[token] = nsarc_dic[token] + 1        
    file.close()

#Gets the probability of word given sarcastic with alpha smoothing
def get_sarc_prob(word):
    global sarc_dic
    global sarc_wcount
    if word not in sarc_dic.keys():
        sarc_dic[word] = 0
    return (sarc_dic[word] + alpha) / (sarc_wcount + alpha * len(vocab))

#Gets the probability of word given not sarcastic with alpha smoothing
def get_nsarc_prob(word):
    global nsarc_dic
    global nsarc_wcount
    if word not in nsarc_dic.keys():
        nsarc_dic[word] = 0
    return (nsarc_dic[word] + alpha) / (nsarc_wcount + alpha * len(vocab))

#Returns the greater of word given label for a line of text
#NOTE: I used an equal amount of data for each label, so prior = 0.5 for both,
#so I only calculated the log probabilities of the word given label
def classifier(line):
    sarc_prob = 0
    nsarc_prob = 0
    for token in line.split():
        sarc_prob = sarc_prob + get_sarc_prob(token)
        nsarc_prob = nsarc_prob + get_nsarc_prob(token)
    if (sarc_prob > nsarc_prob):
        return "SARCASTIC"
    else:
        return "NOT SARCASTIC"

#Goes through a chat log. Classifies each line as sarcastic or not and checks if
#the line contains Kappa to see if it was correct. Returns the percentage of lines
#it got correct
    
def classify_doc(chat_log):
    file = open(chat_log, "r", encoding="utf-8")
    correct = 0
    count = 0
    for line in file:
        if classifier(line) == "SARCASTIC":
            if ("kappa" in line):
                correct = correct + 1
        else:
            if ("kappa" not in line):
                correct = correct + 1
        count = count + 1
    return correct / count
    
if __name__ == '__main__':
    get_sarc_word_counts("ParsedSarcasmData.txt")
    get_nsarc_word_counts("ParsedNotSarcasmData.txt")
    
    
        
