#Used on Sarcasm Data.txt or Not Sarcasm Data.txt to remove timestamps
#and usernames and lowercase everything. Use the output file on Naive Bayes

#Change the files being read from and written to for getting sarcastic and
#not sarcastic

import numpy as np
from os import listdir
from os.path import isfile, join
import os
    
def parse_chat(chat_file):
    #chat_file = "mfbiscuits.txt"
    parsed_chat = open("ParsedNotSarcasmData.txt", "w", encoding='utf-8')
    fp = open(chat_file, encoding='utf-8')
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
    parse_chat("Not Sarcasm Data.txt")
