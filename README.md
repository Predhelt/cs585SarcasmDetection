# cs585SarcasmDetection
Created by:
Chigozie Ikoro, Ethan Johnson, and Kyle Toohey

The data folder contains the following folders:
- labelled-data contains gathered sarcastic and non-sarcastic chat comments.
 - 0.txt is the non-sarcastic dataset
 - 1.txt is the sarcastic dataset
- raw-data contains the data extracted directly from twitch vods, each file is a separate unparsed and unlabelled collection of chat messages

- all-parsed.txt is the output after parsing the commands based on the parser.py file
- word_counts.csv is a list of words and the number of times the words occur in the parsed data
- dummy_data.csv is a file of placeholder data in the proper format readable by classifier

- data.csv is the list of samples with each of their features calculated and labels given as the last column.	Computed using create_feature_vector.py

TODO:
- make python script to output feature vector with last index as the label
- Baseline algorithm on dummy data located in readable_data file
- make python script to make a temp file of possible sarcastic/non-sarcastic data to make data gathering faster

- 