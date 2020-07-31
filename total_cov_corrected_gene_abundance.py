import sys

input_directory = sys.argv[1]

#create list of kegg files to parse through
protein_files = [file for file in os.listdir(input_directory) if file.endswith(".faa")]

#Sum coverage of every gene per bacterial prodigal file
for annot in protein_files:
        with open(os.path.join(input_directory, annot)) as input:
                count = 0
                for line in input:
                        if line.startswith(">NODE"):
                                cov = float(line.split("_")[5])
                                count = count + cov
                        else:
                                pass
        print(str(annot)+" summed gene count (cov corrected) is: "+str(count))
        input.close()