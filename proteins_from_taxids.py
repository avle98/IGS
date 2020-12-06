from Bio import Entrez

Entrez.email = "avle@wpi.edu"

# Esearch searches and retrieves primary IDs and term translations
handle = Entrez.esearch(db="protein",
                        term="txid10239[Organism] OR txid10240[Organism]
                        retstart=100,
                        retmax=100000
                        )
record = Entrez.read(handle)
print(record['IdList'])
handle.close()


# then use Batch Entrez on https://www.ncbi.nlm.nih.gov/sites/batchentrez
