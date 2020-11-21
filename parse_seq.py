# Ann-Elizabeth Le
# WPI Bioinformatics/ Computational Biology ISG 2020-2021
# Last Updated: 11/16/2020 20:33

import sys
from Bio import SeqIO

# Get shorter identifier for each sequence: source ID, protein name and [species]
filename = sys.argv[-1]
def parse_seq(filename):
    for seq_record in SeqIO.parse(open(filename, mode='r'), 'fasta'):
        seq_record.description1 = ' '.join(seq_record.description.split()[1:])
        seq_record.description2 = ''.join(seq_record.description1.partition('**acc')[0])
        print('>' + seq_record.description2)
        print(seq_record.seq)

if __name__ == "__main__":
    parse_seq(sys.argv[-1])







