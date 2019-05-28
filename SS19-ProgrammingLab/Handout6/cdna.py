import sys
import math
import numpy as np



def run(inputPath, outputPath):
    print(f'Log> Input file: {inputPath}, Output file: {outputPath}')
    header, fasta_data = read_fasta(inputPath)
    comp_data = reverse_sequence(fasta_data)
    write_fasta(outputPath, header, comp_data)

def reverse_sequence(seq):
    dna_map = {'A': 'G', 'T': 'C', 'C': 'T', 'G': 'A'}
    return [dna_map[base] for base in seq][::-1]

def read_fasta(path):
    with open(path, 'r') as f:
        data = f.read()
        lines = data.split('\n')
        return (lines[0], ''.join(lines[1:]))

def write_fasta(path, header, data):
    with open(path, 'w') as f:
        f.write(header + ' complementary' + '\n')
        for chunk in range(0, len(data), 70):
            f.write(''.join(data[chunk:chunk+70]))
            f.write('\n')

if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise Exception('Two parameters required!')
    run(sys.argv[1], sys.argv[2])