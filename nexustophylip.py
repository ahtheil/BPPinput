#This script reads all the ifles in a directory, 
#and converts nexus alignment files to phylip format
#Written by Andy Theil
#Last change 11/21/2021

#os to read file pathx
import os

#Dendropy allows to read alignment data in nexus, and convert to phylip
import dendropy

filenames = []


directory = '/Users/andytheil/Desktop/Hypochiluswork/File_formating/mafft_gblocks_raw/'

#Loop through directory to get file paths in a list
for entry in os.scandir(directory):
    if (entry.path.endswith(".nexus")) and entry.is_file():
        filenames.append(entry.path)

#Iterate each file name in list to feed file path to dendropy for conversion
for file in filenames:

#get method from DendroPy
    d = dendropy.DnaCharacterMatrix.get(
        path=file,
        schema="nexus"
        )
#Write method from dendropy, specifying phylip format
    d.write(
        path= file +".phylip",
        schema="phylip",
        strict=False,
        spaces_to_underscores=True,
        force_unique_taxon_labels=False,
        suppress_missing_taxa=False,
        )

