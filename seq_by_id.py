from Bio import SeqIO

my_list = []
with open('/Users/avle/Downloads/taxcheck_familynames.txt') as transcripts:
    for line in transcripts:
        my_list.extend(line.split(' '))

fin = open('/Users/avle/Downloads/unique50_alphabet1.fasta', 'r')
fout = open('/Users/avle/Downloads/extracted_sequences.fasta', 'w')

for record in SeqIO.parse(fin, 'fasta'):
    for item in my_list:
        if item.strip() == record.id:
            fout.write(">" + record.description + "\n")
            fout.write(str(record.seq) + "\n")

fin.close()
fout.close()