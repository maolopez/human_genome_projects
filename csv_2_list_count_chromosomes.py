#This script extract the chromosomes from a genome's CSV file into a list and then calculate the frequency of each chromosome.
from funktionen import getDuplicatesWithCount, read_csv, calculations

n = 1  #This is the position of the CSV Column to where Chromosomes are stored
chromosomes = []

filename = 'human_genome.csv'
    
chromosomes = read_csv(filename, chromosomes, n)
#print(chromosomes)
print("This script extract the chromosomes from a genome's CSV file into a list and then calculate the frequency of each chromosome:")
result = getDuplicatesWithCount(chromosomes)
#print(result)
scope = "Chromosome"
     
calculations(scope, result)    





