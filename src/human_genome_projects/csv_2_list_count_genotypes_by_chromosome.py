#!/usr/bin/python

## Script Name: csv_2_list_count_genotypes_by_chromosome.py
## Author: Mauricio G. Lopez
## Created: 2020.02.24
## Last update: 2020.04.24
## This script relies on module funktionen
## Not intended to be run as a standalone
## This script extract the genotypes from a CSV file into a list and then calculate the frequency of each genotype in every chromose 1-22 + X,Y,MT 

#System Modules
import argparse

#Local Modules
from funktionen import read_csv_x2, getDuplicatesWithCount, calculations

n = 1  #This is the position of the CSV Column to where Chromosomes are stored
genocromes = []
total = 0

parser = argparse.ArgumentParser(description='Extract/Frequency Chromosome:Genotype', prog='csv_2_list_count_genotypes_by_chromosome.py', usage='%(prog)s [-h] filename')
parser.add_argument("filename", help="Give me a local file.csv")
args = parser.parse_args()
filename = args.filename
    
genocromes = read_csv_x2(filename, genocromes, n)
#print(genochromes)
print("This script extract the genotypes from a CSV file into a list and then calculate the frequency of each genotype in every chromose 1-22 + X,Y,MT: ")
result = getDuplicatesWithCount(genocromes)

scope = "Chromosome:Genotype"

calculations(scope, result) 








