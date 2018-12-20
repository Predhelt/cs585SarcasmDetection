#This file randomly added lines from every chat file in the list below
#and added them to NewNotSarcasmData.txt for manual pruning

import random
import os

files = ['310706577 - ProtonJon.txt', '313575730 - ProtonJon.txt', \
         '318038609 - iateyourpie.txt', '322216663 - BrownMan.txt', \
         '326644094 - Strippin.txt', '326978616 - Cryaotic.txt', \
         '331496134 - CohhCarnage.txt', '333600559 - Chess.txt', \
         '334024790 - CohhCarnage.txt', '334809322 - iateyourpie.txt', \
         '335907373 - BrownMan.txt', '339843274 - Strippin.txt', \
         '341020114 - LIRIK.txt', '341811860 - Chess.txt', \
         '342691250 - DansGaming.txt', '343199076 - LIRIK.txt', \
         '343206330 - DansGaming.txt', '343487106 - Cryaotic.txt']

outfile = open("NewNonSarcasmData.txt", "w", encoding='utf-8', errors='ignore')  
for f in files:
    infile = open(f, 'r', encoding='utf-8', errors='ignore')
    random.seed(56389)
    for line in infile:
        if "Kappa" not in line:
            a = random.randint(1, 10000)
            if (a > 6050 and a < 6070):
                outfile.write(line)

infile.close()
outfile.close()
