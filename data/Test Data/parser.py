#Goes through every annotated chat log and parses out the timestamp and username.
#Outputs the parsed data to ParsedTestData.txt for testing

import numpy as np
from os import listdir
from os.path import isfile, join
import os
    
def parse_chat(chat_file):
    files = os.listdir();
    files.remove("parser.py")
    print(files)
    for f in files:
        if "RAW" in f:
            files.remove(f)
    print(files)
    #chat_file = "mfbiscuits.txt"
    parsed_chat = open(chat_file, "w", encoding='utf-8')
    for f in files:
        fp = open(f, encoding='utf-8')
        line = fp.readline()
        while line[0] == "S" or line[0] == "N":
            # '[*] <*> +'
            message = line[0] + " " + "".join(line.split('> ')[1:]) # text starts after the first occurrence
            #print(message)
            #if( == ):
            #print("TRUE")
            #statement_with_usernames = "{}".format(line[11:].strip())
                #start_index = statement_with_usernames.find('>')
                #statement = statement_with_usernames[start_index+1:]
            parsed_chat.write(message.lower())
            line = fp.readline()
        fp.close()
    parsed_chat.close()

if __name__ == '__main__':
    parse_chat("ParsedTestData.txt")
