#!/usr/bin/python

## Script Name: csv_2_list_count_chromosomes.py
## Author: Mauricio G. Lopez
## Created: 2020.02.24
## Last update: 2020.04.24
## This script relies on module funktionen
## Not intended to be run as a standalone
## This script extract the chromosomes from a genome's CSV file into a list and then calculate the frequency of each chromosome.

#System Modules
import argparse

#Local Modules
from funktionen import getDuplicatesWithCount, read_csv, calculations

n = 1  #This is the position of the CSV Column to where Chromosomes are stored
chromosomes = []

parser = argparse.ArgumentParser(description='Extract/Frequency Chromosomes', prog='csv_2_list_count_chromosomes.py', usage='%(prog)s [-h] filename')
parser.add_argument("filename", help="Give me a local file.csv")
args = parser.parse_args()
filename = args.filename
    
chromosomes = read_csv(filename, chromosomes, n)
#print(chromosomes)
print("This script extract the chromosomes from a genome's CSV file into a list and then calculate the frequency of each chromosome:")
result = getDuplicatesWithCount(chromosomes)
#print(result)
scope = "Chromosome"
     
calculations(scope, result)    





