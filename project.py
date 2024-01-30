import gzip
import sys
from helpers import *
from Bio import SeqIO

#get the sequence from the fasta file
seq_read = SeqIO.read("sample.fasta","fasta")
sequence = seq_read.seq

"""
<class 'Bio.SeqRecord.SeqRecord'> returned by SeqIO.read() function that contains
ID: Genoma_CpI19_Refinada_v2
Name: Genoma_CpI19_Refinada_v2
Description: Genoma_CpI19_Refinada_v2
Number of features: 0
Seq('GTGTCGGAGGCTCCATCGACATGGAACGAGCGGTGGCAAGAAGTTACTAATGAG...CAC')

"""
#compress the sequence and get the compressed byte like object
byte_seq = compress_dna(sequence)
#write the byte object to file
write_seq_to_bin(byte_seq,'seqbytes.bin')

#read the byte object that has the sequence encoded from file
file_byte_seq = read_seq_from_bin('seqbytes.bin')


#decompress the sequence into a readable formate (string)
file_read_seq = decompress_dna(file_byte_seq)

#compare before compression and after to make sure no changes happened
print(sequence)
print(file_read_seq)
if sequence == file_read_seq:
    print('sequence match')

#to compress the file using gzip library
with open('seqbytes.bin','rb') as file , gzip.open('seqbytes.bin.gz','wb') as compressed_file:
    compressed_file.writelines(file)

print(f'File seqbytes.bin compressed to seqbytes.bin.gz.')

