#This script will take a directory of phylip alingment files
#It will read them and only include specified taxa in the output
#
#Written by Addy Theil
#Last change 11/21/2021


#Import functions from package os to read files from directory
from os import listdir
from os.path import isfile, join

#Make the list of file names
directory = '/Users/andytheil/Desktop/Hypochiluswork/File_formating/phylipalignment550/'
onlyfiles = [f for f in listdir(directory) if isfile(join(directory, f))]

#Open an output file to write results to
outF = open("/Users/andytheil/Desktop/Hypochiluswork/File_formating/pythontestoutput.txt","w")

#Loop through directory to get data from each file, store in python, 
for file in onlyfiles:
    f = open(("/Users/andytheil/Desktop/Hypochiluswork/File_formating/phylipalignment550/"+file),"r")
    
#reading the first line in as the header
    header = f.readline()
    seqlen = header[3:6]

#loop through each sequence in the file and check the header as CA  
    taxa = f.readlines()

#Loop to calculate individuals per alingment file for header info
    counter = 0
    for seq in taxa:
        if (seq[0:2] == "CA"):
            counter += 1
#Header format for printing to file
    header = str(counter) + " " + seqlen
 
#actually wiriting the header into the output file
    outF.write(header) 
    outF.write("\n")
    
#Making the header for each sequence at beginning of each line
    genenum = file[0:8].replace("-","")
    genenum = genenum.replace(".","")
    genenum = genenum.replace(" ","")
#Loop that writes the actual sequence
    for seq in taxa:
        if (seq[0:2] == "CA"):
            outF.write(genenum+"^"+str(seq))
    
    f.close()
#Close output file

outF.close()
