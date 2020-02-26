#This script extract the genotypes from a CSV file into a list and then calculate the frequency of each genotype in every chromose 1-22 + X,Y,MT
import csv

#https://thispointer.com/python-find-duplicates-in-a-list-with-frequency-count-index-positions/
def getDuplicatesWithCount(genocromes):
   ''' Get frequency count of duplicate elements in the given list '''
   dictOfElems = dict()
   # Iterate over each element in list
   for genocrome in genocromes:
      # If element exists in dict then increment its value else add it in dict
      if genocrome in dictOfElems:
         dictOfElems[genocrome] += 1
      else:
         dictOfElems[genocrome] = 1    
         # Filter key-value pairs in dictionary. Keep pairs whose value is greater than 1 i.e. only duplicate elements from list.
   dictOfElems = { key:value for key, value in dictOfElems.items() if value > 1}
   # Returns a dict of duplicate elements and thier frequency count
   return dictOfElems

#by my own skill below
i = 0
n = 1
genomes = []
genotypes = []
chromosomes = []
genocromes = []
total = 0
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
            #Isolate the pair chromosome::genotype from the genome
            for genome in genomes:
               chromosomes.append(genomes[n])
               n += 2
               genotypes.append(genomes[n])
               genocromes.append((chromosomes[i], genotypes[i]))
               n += 2
               i += 1
        except IndexError:
            pass
        continue

#print(genochromes)
print("This script extract the genotypes from a CSV file into a list and then calculate the frequency of each genotype in every chromose 1-22 + X,Y,MT: ")
dictOfElems = getDuplicatesWithCount(genocromes)
for key, value in dictOfElems.items():
        total = total + value
for key, value in dictOfElems.items():
        print('{0:.2f}%'.format((value / total * 100)))
        print('Chromosome:Genotype', key , ' :: ', value)
print("The percentages were calculated based in the grand total: " + str(total))






