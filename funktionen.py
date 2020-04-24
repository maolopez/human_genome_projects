#!/usr/bin/python

## Script Name: funktionen.py
## Author: Mauricio G. Lopez
## Created: 2020.02.24
## Last update: 2020.04.24
## This script relies on module funktionen
## Not intended to be run as a standalone
##

#System Modules
import csv
import os.path

#https://thispointer.com/python-find-duplicates-in-a-list-with-frequency-count-index-positions/
def getDuplicatesWithCount(w):
   ''' Get frequency count of duplicate elements in the given list '''
   dictOfElems = dict()
   # Iterate over each element in list
   #w = []
   for i in w:
      # If element exists in dict then increment its value else add it in dict
      if i in dictOfElems:
         dictOfElems[i] += 1
      else:
         dictOfElems[i] = 1    
         # Filter key-value pairs in dictionary. Keep pairs whose value is greater than 1 i.e. only duplicate elements from list.
   dictOfElems = {key:value for key, value in dictOfElems.items() if value >= 1}
   # Returns a dict of duplicate elements and thier frequency count
   return dictOfElems


def read_csv(f, c, n):
    # read CSV file & load into a list
    c = []
    if not os.path.exists(f):
        print("Give me a local file.csv or use -h in order to get help")
        exit(0)
    else:    
        with open(f, 'r') as my_file:  
            reader = csv.reader(my_file, delimiter='\n')
            for delimiter in reader:
                my_list = my_file.read()
                #clean single quotes, and \n, split string into elements in a list.
                my_list = my_list.strip('\n')
                my_list = my_list.replace('\n' , ',')
                genomes = my_list.split(',')
                try:
                    #Isolate the chromosomes from the gemome
                    for genome in genomes:
                       c.append(genomes[n])
                       n += 4
                except IndexError:
                    pass
                continue
    return c


def read_csv_x2(f, c, n):    
    # read CSV file & load into list
    i = 0
    c = []
    chromosomes = []
    genotypes = []
    if not os.path.exists(f):
        print("Give me a local file.csv or use -h in order to get help")
        exit(0)
    else:    
        with open(f, 'r') as my_file:
            reader = csv.reader(my_file, delimiter='\n')
            for delimiter in reader:
                my_list = my_file.read()
                #clean single quotes, and \n, split string into elements in a list.
                my_list = my_list.strip('\n')
                my_list = my_list.replace('\n' , ',')
                genomes = my_list.split(',')
                try:
                    #Isolate the pair chromosome::genotype from the genome
                    for genome in genomes:
                       chromosomes.append(genomes[n])
                       n += 2
                       genotypes.append(genomes[n])
                       c.append((chromosomes[i], genotypes[i]))
                       n += 2
                       i += 1
                except IndexError:
                    pass
                continue
    return c


def calculations(s, r):
    total = 0
    for key, value in r.items():
        total = total + value
    for key, value in r.items():
        print("Percentage", '{0:.2f}%'.format((value / total * 100)))
        print(s, key , ' :: ', value)
    print("The percentages were calculated based in the grand total: ", total)
