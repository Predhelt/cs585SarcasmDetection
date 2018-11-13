import numpy as np
from os import listdir
from os.path import isfile, join

def parse_chat(chat_file, raw_path):
    #chat_file = "mfbiscuits.txt"

    chat_name = chat_file.lstrip(raw_path)
    file_name = "parsed_data/" + chat_name + "-parsed.text"
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
    fp.close()

if __name__ == '__main__':
    mypath = 'raw_data/'
    filenames = np.array([(mypath + f) for f in listdir(mypath) if isfile(join(mypath, f))])
    #print(filenames)
    for file in filenames:
        parse_chat(file, mypath)
