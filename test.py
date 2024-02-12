from helpers import *
from Bio import SeqIO
#
records = SeqIO.parse("pdb_seqres.fasta", "fasta")
for record in records:
    # Process each record as needed
    print(record.id, len(record))
    print(record.seq)