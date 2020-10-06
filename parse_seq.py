# Ann-Elizabeth Le
# WPI Bioinformatics/ Computational Biology IGS 2020-2021
# Last Updated: 10/05/2020 1500

# Get shorter identifier for each sequence
import fastaparser as fastaparser
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import fastaparser

original_file = '/Users/avle/OneDrive - Worcester Polytechnic Institute (wpi.edu)/WPI/2020-2021/IGS/unique50.fasta'
corrected_file = '/Users/avle/Downloads/new_file.fasta'


# # this works
# with open(original_file) as old_file:
#     parser = fastaparser.Reader(old_file)
#     for record in parser:
#         print('>', record.description.partition(('**acc'))[0])
#         print(record.sequence_as_string())

# this works
with open(corrected_file, 'w') as f_out:
    for seq_record in SeqIO.parse(open(original_file, mode='r'), 'fasta'):
        seq_record.description1 = ' '.join(seq_record.description.split()[1:])
        seq_record.description2 = ''.join(seq_record.description1.partition('**acc')[0])
        print('>' + seq_record.description2)
        print(seq_record.seq)
f_out.close()


# with open(corrected_file, 'w') as f_out:
#     for seq_record in SeqIO.parse(open(original_file, mode='r'), 'fasta'):
#         seq_record.description1 = ' '.join(seq_record.description.split()[1:])
#         seq_record.description2 = ''.join(seq_record.description1.partition('**acc')[0])
#         print('>' + seq_record.description2)
#         print(seq_record.seq)
#         sequence = fastaparser.FastaSequence(
#             description = seq_record.description2,
#             sequence = seq_record.seq)
#         SeqIO.write(sequence, corrected_file, 'fasta')
# f_out.close()

# with open(corrected_file, 'w') as new_file:
#     with open(original_file, 'r') as old_file:
#         for seq_record in old_file:
#             parser = fastaparser.Reader(old_file)
#             # seq_record.description1 = ' '.join(seq_record.description.split()[1:])
#             seq_record.description = ''.join(seq_record.partition('**acc')[0])
#             writer = fastaparser.Writer(new_file)
#             writer.writefasta(seq_record.description)
#             writer.writefasta(seq_record.sequence)
            # sequence = fastaparser.FastaSequence(
            #     description=records.description.split('*')[0],
            #     sequence=records.sequence_as_string()
            # )


# with open(original_file) as old_file:
#         # descriptions = record.description.partition(('**acc'))[0]
#         # sequences = record.sequence_as_string()
#     with open(corrected_file, 'w') as new_file:
#         parser = fastaparser.Reader(old_file)
#         writer = fastaparser.Writer(new_file)
#         for record in parser:
#             parser = fastaparser.Reader(old_file)
#             writer.writefasta(record.description.partition(('**acc'))[0])
#             writer.writefasta(record.sequence_as_string())



# count = SeqIO.convert(original_file, "fasta", "/Users/avle/Downloads/output.gb", "genbank")
# print("Converted %i records" % count)

#




