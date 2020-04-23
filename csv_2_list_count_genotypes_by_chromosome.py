#This script extract the genotypes from a CSV file into a list and then calculate the frequency of each genotype in every chromose 1-22 + X,Y,MT
from funktionen import read_csv_x2, getDuplicatesWithCount, calculations

n = 1  #This is the position of the CSV Column to where Chromosomes are stored
genocromes = []
total = 0
filename = 'human_genome.csv'
    
genocromes = read_csv_x2(filename, genocromes, n)
#print(genochromes)
print("This script extract the genotypes from a CSV file into a list and then calculate the frequency of each genotype in every chromose 1-22 + X,Y,MT: ")
result = getDuplicatesWithCount(genocromes)

scope = "Chromosome:Genotype"

calculations(scope, result) 








