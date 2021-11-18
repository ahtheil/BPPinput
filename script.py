#This is the script to begin the project with

#The goal of this script is to read alignment phylip files in a directory
#The output will be a single fuile of phylip files with all alignments included 
#in the file. The utput wil be in specifically BPP format. Additionaly, we will 
#Filter based on species we are including in analysis


import os
from os import listdir
from os.path import isfile, join



directory = r'/Users/andytheil/Desktop/Hypochiluswork/BPP run for concatenated/converttophylip/'
onlyfiles = [f for f in listdir(directory) if isfile(join(directory, f))]



