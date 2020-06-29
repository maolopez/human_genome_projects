FROM python:3.6.9

# Install dependencies
COPY . /

RUN cd src/human_genome_projects && \
    ls -a

WORKDIR src/human_genome_projects

ENTRYPOINT ["python"]
CMD ["./csv_2_list_count_genotypes.py", "human_genome.csv"]
#CMD ["./csv_2_list_count_chromosomes.py", "human_genome.csv"]
#CMD ["./csv_2_list_count_genotypes_by_chromosome.py", "human_genome.csv"]
#ONLY one CMD can be un-commented
