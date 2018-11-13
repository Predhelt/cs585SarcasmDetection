import numpy as np

def parse_chat(chat_file):
    #chat_file = "mfbiscuits.txt"

    file_name = chat_file + "--parsed.txt"
    parsed_chat = open(file_name, "w")
    with open(chat_file) as fp:
        line = fp.readline()
        while line:
            #line[11:] truncates the timestamp
            if(line[11] == '<'):
                statement_with_usernames = "{}".format(line[11:].strip())
                start_index = statement_with_usernames.find('>')
                statement = statement_with_usernames[start_index+1:]
                parsed_chat.write(statement.lower() + '\n')
            line = fp.readline()
if __name__ == '__main__':
	parse_chat("mfbiscuits.txt")