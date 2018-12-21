# cs585SarcasmDetection
Created by:
Chigozie Ikoro, Ethan Johnson, and Kyle Toohey

create_feature_vector.py contains several functions to compute different types of feature vectors from different file formats.  The output of this file are located in the data folder as .csv files that are used by our classifiers.

The sarcasm_detection.py script trains and then runs the neural net classifier we have made and currently outputs all the occurrences of when the predicted labels do not match the truth label with the line number as the first value

The data folder contains the following folders:
- labelled-data contains gathered sarcastic and non-sarcastic chat comments.
 - 0.txt is the non-sarcastic dataset
 - 1.txt is the sarcastic dataset
- raw-data contains the data extracted directly from twitch vods, each file is a separate unparsed and unlabelled collection of chat messages

It also contains the following files:
- all-parsed.txt is the output after parsing the commands based on the parser.py file
- word_counts.csv is a list of words and the number of times the words occur in the parsed data
- dummy_data.csv is a file of placeholder data in the proper format readable by classifier
- train_data.csv is a file of the training data we used on our classifiers, labels given as the last column.	Computed using create_feature_vector.py
- test_data.csv is a file of the test data we used on our classifiers, labels given as the last column.	Computed using create_feature_vector.py

How to run the program twitch-chatlog:
run line in cmd after using npm to install the twitch-chatlog to a local directory: 

twitch-chatlog -s 00:15:00 -l 7200 <vod_id> > <filename>

twitch-chatlog -s 00:15:00 -l 7200 <vod_id> > "C:\dir\vod<streamerName>_output.txt"

ex:
twitch-chatlog -s 00:15:00 -l 10800 333145457 > "C:\dir\vodSips_3hrOutput.txt"