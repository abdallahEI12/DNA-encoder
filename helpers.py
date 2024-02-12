import math
from math import ceil
from struct import pack, unpack


def compress_dna(sequence):
    compression_mapping = {'A': "00" ,
                           'T': '01',
                           'G': "10",
                           'C': '11'}

    sequence_length = len(sequence)

    compressed_sequence = pack('>Q',sequence_length)

    for index in range(0,sequence_length,4):
        byte = ''
        try:

            for base in range(index,index+4):

                byte += compression_mapping[sequence[base]]

            compressed_sequence += pack('>B',int(byte,2))


        except IndexError:
            compressed_sequence += pack('>B', int(byte,2))

    return compressed_sequence


def write_seq_to_bin(byte_sequence,file_name):
    with open(file_name, 'wb') as file:
        file.write(byte_sequence)


def read_seq_from_bin(file):
    with open(file, 'rb') as file:
        read_bytes = file.read()
    return read_bytes

def decompress_dna(byte_sequence):
    decompression_mapping = {0: 'A', 1: 'T', 2: 'G', 3: 'C'}

    number_of_bases = unpack('>Q',byte_sequence[:8])[0]
    bases_byte_sequence = byte_sequence[8:]


    base_sequence = ''

    for byte in bases_byte_sequence:

        for bits in range(7,-1,-2):

            base_sequence += decompression_mapping[((byte >> bits-1) & 3)]

    return base_sequence[:number_of_bases]

