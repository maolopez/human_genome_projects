human_genome_projects
=====================

Manipulating txt, csv files with human genome information

General description
===================

A CSV file with a Human DNA genoma has 2395592 words. Instead a text file with the Bible book has only 824383 words. The CSV files has 4 columns and 598912 rows. The columns are rsid, chromosome, position and genotype. Percentages are calculated too.


Usage
-----

|*Script*                                   |*Description*                                 |*Usage*                                          |

| ------------------------------------------|:--------------------------------------------:|:------------------------------------------------|

|csv_2_list_count_genotypes.py              |calculate the frequency of each genotype      |python3 csv_2_list_count_genotypes.py file.csv   |

|csv_2_list_count_chromosomes.py            |calculate the frequency of each chromosome    |python3 csv_2_list_count_chromosomes.py file.csv |

|csv_2_list_count_genotypes_by_chromosome.py|the frequency of each chromosome:genotype pair|same logic                                       |
