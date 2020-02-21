#This script extract the genotypes from a CSV file into a list and then calculate the frequency of each genotype.
import csv

#https://thispointer.com/python-find-duplicates-in-a-list-with-frequency-count-index-positions/
def getDuplicatesWithCount(genotypes):
   ''' Get frequency count of duplicate elements in the given list '''
   dictOfElems = dict()
   # Iterate over each element in list
   for genotype in genotypes:
      # If element exists in dict then increment its value else add it in dict
      if genotype in dictOfElems:
         dictOfElems[genotype] += 1
      else:
         dictOfElems[genotype] = 1    
         # Filter key-value pairs in dictionary. Keep pairs whose value is greater than 1 i.e. only duplicate elements from list.
   dictOfElems = { key:value for key, value in dictOfElems.items() if value > 1}
   # Returns a dict of duplicate elements and thier frequency count
   return dictOfElems

#from my own skill below
n = 3
genotypes = []
genomes = []
filename = 'human_genome.csv'
# read CSV file & load into list
with open(filename, 'r') as my_file:
    reader = csv.reader(my_file, delimiter='\n')
    for delimiter in my_file:
        my_list = my_file.read()
        #clean single quotes, and \n, split string into elements in a list.
        my_list = my_list.strip('\n')
        my_list = my_list.replace('\n' , ',')
        genomes = my_list.split(',')
        try:
            #Isolate the genotypes from the genome
            for genome in genomes:
               genotypes.append(genomes[n])
               n += 4
        except IndexError:
            pass
        continue

#print(genotypes)
dictOfElems = getDuplicatesWithCount(genotypes)
for key, value in dictOfElems.items():
        print(key , ' :: ', value)





