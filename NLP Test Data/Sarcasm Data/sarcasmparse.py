#This file was to get all lines with Kappa from a file and put it in
#NewSarcasmData.txt for manual pruning

infile = open("343206330.txt", 'r', encoding='utf-8')
outfile = open("NewSarcasmData.txt", "w", encoding='utf-8')
for line in infile:
    if "Kappa" in line:
        if len(line.split()) > 5:
            if "Kappa" not in line.split()[3]:
                outfile.write(line)
infile.close()
outfile.close()
