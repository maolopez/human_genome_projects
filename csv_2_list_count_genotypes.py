#!/usr/bin/python

## Script Name: csv_2_list_count_genotypes.py
## Author: Mauricio G. Lopez
## Created: 2020.02.24
## Last update: 2020.04.24
## This script relies on module funktionen
## Not intended to be run as a standalone
## This script extract the genotypes from a CSV file into a list and then calculate the frequency of each genotype. 

#System Modules
import argparse

#Local Modules
from funktionen import getDuplicatesWithCount, read_csv, calculations

n = 3  #This is the position of the CSV Column to where Genotypes are stored
genotypes = []

parser = argparse.ArgumentParser(description='Extract/Frequency Genotypes', prog='csv_2_list_count_genotypes.py', usage='%(prog)s [-h] filename')
parser.add_argument("filename", help="Give me a local file.csv")
args = parser.parse_args()
filename = args.filename

genotypes = read_csv(filename, genotypes, n)
#print(genotypes)
print("This script extract the genotypes from a CSV file into a list and then calculate the frequency of each genotype")
result = getDuplicatesWithCount(genotypes)

scope = "Genotype"

calculations(scope, result) 

