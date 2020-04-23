#This script extract the genotypes from a CSV file into a list and then calculate the frequency of each genotype.
from funktionen import getDuplicatesWithCount, read_csv, calculations

n = 3  #This is the position of the CSV Column to where Genotypes are stored
genotypes = []
filename = 'human_genome.csv'

genotypes = read_csv(filename, genotypes, n)
#print(genotypes)
print("This script extract the genotypes from a CSV file into a list and then calculate the frequency of each genotype")
result = getDuplicatesWithCount(genotypes)

scope = "Genotype"

calculations(scope, result) 

