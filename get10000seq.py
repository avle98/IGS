from Bio import SeqIO
from random import sample

original_file = '/Users/avle/OneDrive - Worcester Polytechnic Institute (wpi.edu)/WPI/2020-2021/IGS/output.fasta'
with open(original_file) as f:
    seqs = SeqIO.parse(f, "fasta")
    samps = ((seq.description, seq.sequence) for seq in sample(list(seqs),7000))
    for samp in samps:
        print(">{}\n{}".format(*samp))



awk 'BEGIN {n_seq=0;} /^>/ {if(n_seq%1000000==0){file=sprintf("output.split.%d.fa",n_seq);} print >> file; n_seq++; next;} { print >> file; }' < output.fasta