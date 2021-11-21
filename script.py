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

#Make a list for tags of sequences we want to keep in analysis, excluding taxa we dont want

includetaxa = ["CA_H_bernardino_G2894","CA_H_bernardino_G2898","CA_H_bernardino_H025",
        "CA_H_petrunkevitchi_ALTA_G2601","CA_H_petrunkevitchi_TULE_G2463",
        "CA_H_petrunkevitchi_TULE_G2476","CA_H_petrunkevitchi_KING_G2543",
        "CA_H_petrunkevitchi_SAN_G2509","CA_H_petrunkevitchi_SEQ_G2251",
        "CA_H_petrunkevitchi_SEQ_G2488","CA_H_petrunkevitchi_KING_G2550",
        "CA_H_petrunkevitchi_YOSE_G2561","CA_H_petrunkevitchi_YOSE_G2566",
        "CA_H_petrunkevitchi_SAN_G2558","CA_H_kastoni_G2519","CA_H_kastoni_NEY_H324"
        ]

#Open an output file to write results to
outF = open("/Users/andytheil/Desktop/Hypochiluswork/File_formating/pythontestoutput.txt","w")


#Loop through directory to get data from each file, store in python, 
for file in onlyfiles:
    f = open(("/Users/andytheil/Desktop/Hypochiluswork/File_formating/phylipalignment550/"+file),"r")
    contents = f.read()

    #Next step, write a if statement to check if individuals are on list
    
    outF.write(str(contents))
    
    #Write to a output file

    f.close()
    
    
#Close output file
outF.close()
