def compress_dna(sequence):
    compression_mapping = {'A': b'00' ,
                           'T': b'01',
                           'G': b'10',
                           'C': b'11'}
    compressed_sequence = b''
    for i in range(0,len(sequence),4):
        for x in range(4):
            compressed_sequence += compression_mapping[sequence[i+x]]

    byte_sequence = int(compressed_sequence, 2).to_bytes(len(compressed_sequence) // 8, byteorder='big')
    return byte_sequence

def write_seq_to_bin(byte_sequence,file_name):
    with open(file_name, 'wb') as file:
        file.write(byte_sequence)

def read_seq_from_bin(file):
    with open(file, 'rb') as file:
        read_bytes = file.read()
    return read_bytes

def decompress_dna(byte_sequence):
    decompression_mapping = {0: 'A', 1: 'T', 2: 'G', 3: 'C'}
    decompressed_sequence = ''
    for byte in byte_sequence:
        for bits in range(7,-1,-2):
            decompressed_sequence += decompression_mapping[((byte >> bits-1) & 3)]
    return decompressed_sequence
