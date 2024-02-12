import gzip
import sys
from helpers import *
from Bio import SeqIO

#get the sequence from the fasta file
seq_read = SeqIO.read("sample.fasta","fasta")
sequence = seq_read.seq

#compress the sequence and get the compressed byte like object
byte_seq = compress_dna(sequence)
#write the byte object to file
write_seq_to_bin(byte_seq,'seqbytes.bin')
write_seq_to_bin(byte_seq,'seqbytes.bin')

#read the byte object that has the sequence encoded from file
file_byte_seq = read_seq_from_bin('seqbytes.bin')


#decompress the sequence into a readable formate (string)
DNA = decompress_dna(file_byte_seq)

print(len(sequence))
print(len(DNA))


if(DNA == sequence):
    print("success")
else:
    print("failure")


