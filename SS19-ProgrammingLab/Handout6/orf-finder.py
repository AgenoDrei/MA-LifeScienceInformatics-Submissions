import sys
import math
import numpy as np
from cdna import reverse_sequence

def run(inputPath, outputPath):
    print(f'Log> Input file: {inputPath}, Output file: {outputPath}')
    header, fasta_data = read_fasta(inputPath)

    reading_frames = extract_reading_frames(fasta_data)
    fasta_data_comp = ''.join(reverse_sequence(fasta_data))
    reading_frames += extract_reading_frames(fasta_data_comp, complementary=True)

    write_fasta(outputPath, header, reading_frames, fasta_data, fasta_data_comp)

    print(sorted(reading_frames))
    print('Num found orf: ', len(reading_frames))


def extract_reading_frames(data, complementary=False):
    stop_codons = ['TAA', 'TAG', 'TGA']
    start_codon = 'ATG'
    cur_orf = []
    frames = []
    genome_length = len(data)

    for start_idx in range(0, 3):
        for i in range(start_idx, len(data), 3):
            cur_residues = data[i:i+3]
            if cur_residues in start_codon:
                cur_orf.append(i)
            elif cur_residues in stop_codons and len(cur_orf) > 0:
                frames.append((cur_orf.pop(0), i+3, 'c' if complementary else ''))
        cur_orf.clear()

    return frames


def read_fasta(path):
    with open(path, 'r') as f:
        data = f.read()
        lines = data.split('\n')
        return (lines[0], ''.join(lines[1:]))


def write_fasta(path, header, frames, data, data_comp):
    with open(path, 'w') as f:
        header_start, header_end = '|'.join(header.split('|')[:4]) , '' + header.split('|')[-1]
        for orf in frames:
            comp_flag = orf[2]
            if comp_flag == 'c':
                genome_len = len(data)
                f.write(header_start + f'|:{comp_flag}{genome_len - orf[0]}-{genome_len - orf[1]}|' + header_end + '\n')
                frame = data_comp[orf[0]:orf[1]][::-1]
                for chunk in range(1, len(frame), 70):
                    f.write(''.join(frame[chunk:chunk+70]))
                    f.write('\n')
            else:
                f.write(header_start + f'|:{comp_flag}{orf[0] + 1}-{orf[1]}|' + header_end + '\n')
                frame = data[orf[0]:orf[1]]
                for chunk in range(1, len(frame), 70):
                    f.write(''.join(frame[chunk:chunk+70]))
                    f.write('\n')


if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise Exception('Two parameters required!')
    run(sys.argv[1], sys.argv[2])