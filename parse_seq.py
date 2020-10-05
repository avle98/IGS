# Ann-Elizabeth Le
# WPI Bioinformatics/ Computational Biology IGS 2020-2021
# Last Updated: 10/05/2020 1500

# Get shorter identifier for each sequence

import fastaparser

filename = '/Users/avle/OneDrive - Worcester Polytechnic Institute (wpi.edu)/WPI/2020-2021/IGS/unique50.fasta'
filename2 = '/Users/avle/Downloads/new_file.fasta'

with open(filename) as fasta_file:
    parser = fastaparser.Reader(fasta_file)
    for seq in parser:
        header = seq.description.split('*')[0]
        sequences = seq.sequence_as_string()
        new_file = open(filename2, 'w')
        with open(filename2, 'w') as new_file:
                new_file.writelines(header)
                new_file.writelines(sequences)
                new_file.close()




