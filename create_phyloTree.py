from Bio import Phylo
import sys

infile = sys.argv[1]
intype = sys.argv[2]
outfile = sys.argv[3]
outtype = sys.argv[4]

Phylo.convert(infile,intype, outfile, outtype)