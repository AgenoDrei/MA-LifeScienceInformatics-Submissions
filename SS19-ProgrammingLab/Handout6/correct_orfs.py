import sys
import numpy as np


def run(custom_orfs_path, coding_regions_path, min_orf_size=350):
    custom_orfs = get_sequence_positions(custom_orfs_path, min_orf_size)
    correct_genes = get_sequence_positions(coding_regions_path)

    print(f'Total number of open reading frames: {len(custom_orfs)}')
    print(f'Total number of genes: {len(correct_genes)}')

    correct_predictions, correct_ends, missed_genes = 0, 0, len(correct_genes)
    for end_orf, start_orf in custom_orfs.items():
        for end_gene, start_gene in correct_genes.items():
            if start_gene == start_orf:
                correct_predictions += 1
            if end_gene == end_orf:
                correct_ends += 1
                missed_genes -= 1

    print(f'Total number and ratio of open reading frames correctly predicting a gene: {correct_predictions}, {correct_predictions / len(custom_orfs) * 100}%')
    print(f'Total number and ratio of open reading frames correctly predicting at least the stop codon of a gene: {correct_ends}, {correct_ends / len(custom_orfs) * 100}%')
    print(f'Number of missed genes: {missed_genes}')

def get_sequence_positions(orf_path, min_orf_size=None):
    orf_dict = {}
    with open(orf_path, 'r') as f:
        data = f.read()
        lines = data.split('\n')

        for line in lines:
            if len(line) < 1 or line[0] != '>':
                continue
            header_parts = line.split('|')
            position_str = header_parts[4].split(' ')[0]
            start, end = position_str.split('-')
            start = str(start).replace(':',  '')
            start = str(start).replace('c', '')
            if min_orf_size != None and min_orf_size > np.abs(int(start) - int(end)):
                continue
            orf_dict[int(end)] = int(start)

    return orf_dict


if __name__ == '__main__':
    if len(sys.argv) != 4:
        raise Exception('Three parameters required!')
    run(sys.argv[1], sys.argv[2], min_orf_size=int(sys.argv[3]))