import numpy as np
import sys


def align_sequences(penality, biosum, seq1, seq2):
    print(f'Aligning sequences {seq1} and {seq2}...')
    seq1 = '_' + seq1
    seq2 = '_' + seq2
    grid = np.zeros((len(seq1), len(seq2)))

    # Init grid
    init_value = 0
    for i in range(grid.shape[0]): #rows
        grid[i][0] = init_value
        init_value -= 1
    init_value = 0
    for i in range(grid.shape[1]): #cols
        grid[0][i] = init_value
        init_value -= 1

    # Calc values for grid
    for c in range(1, grid.shape[1]):
        for r in range(1, grid.shape[0]):
            d_dig = grid[r-1, c-1] + calcScore(biosum, penality, seq1[r], seq2[c])
            d_up = grid[r-1, c] + penality
            d_left = grid[r, c-1] + penality
            grid[r, c] = max(d_dig, d_up, d_left)

            #pretty_print(seq1, seq2, grid)


    pretty_print(seq1, seq2, grid)
    alignment = traceback(grid, seq1, seq2, biosum, penality)
    score = calc_alignment_score(alignment[2])

    print('Alignment score: ', grid[grid.shape[0] - 1, grid.shape[1] - 1])
    print('Alignment: ', alignment[0])
    print('Alignment: ', alignment[2])
    print('Alignment: ', alignment[1])
    print('Metrics: ', score)

def calc_alignment_score(descriptor):
    denom = 0
    nom_sim, nom_idt = 0, 0
    for i in range(len(descriptor)):
        val = descriptor[i]
        if val == '\t':
            continue
        denom += 1
        if val == '|':
            nom_sim += 1
            nom_idt += 1
        elif val == ':':
            nom_sim += 1
    return {'Sequence similarity (in %)': nom_sim / denom, 'Sequence identity (in %)': nom_idt / denom}

def traceback(grid, seq1, seq2, biosum, penality):
    r, c = grid.shape[0] - 1, grid.shape[1] - 1
    res_seq1, res_seq2 = '', ''
    descriptor = ''
    while r > 0 and c > 0:
        r = r - 1
        c = c - 1
        if grid[r + 1, c] > grid[r, c]:
            r += 1
            res_seq1 += '_'
            res_seq2 += seq2[c]
        elif grid[r, c + 1] > grid[r, c]:
            c += 1
            res_seq1 += seq1[r]
            res_seq2 += '_'
        else:
            res_seq1 += seq1[r]
            res_seq2 += seq2[c]
        res_seq1 += '\t'
        res_seq2 += '\t'

    res_seq1 = res_seq1[-2::-1]
    res_seq2 = res_seq2[-2::-1]
    for i in range(len(res_seq1)):
        val1, val2 = res_seq1[i], res_seq2[i]
        if val1 == '\t' or val2 == '\ŧ':
            continue
        if val1 == val2:
            descriptor += '|'
        elif calcScore(biosum, penality, val1, val2) > 0:
            descriptor += ':'
        else:
            descriptor += ' '
        descriptor += '\t'

    return (res_seq1, res_seq2, descriptor)


def calcScore(biosum, penality, val1, val2):
    if val1 == '_' or val2 == '_':
        return penality
    return int(biosum[val1][val2])


def pretty_print(seq1, seq2, data):
    [print(l, end=':   ') for l in seq2]
    print()
    for r in range(data.shape[0]):
        print(seq1[r], end=': ')
        for c in range(data.shape[1]):
            print(int(data[r, c]), end=',  ')
        print()


def readSequence(path: str) -> str:
    with open(path, 'r') as f:
        data = f.read()
        lines = data.split('\n')
        sequence = ''
        for i, line in enumerate(lines):
            if i == 0:
                continue
            sequence += line
        print(f'Successfully read {len(data)} characters from file {path}')
        return sequence


def readBiosum(path: str) -> dict:
    biosum = {}
    with open(path, 'r') as bs:
        data = bs.read()
    lines = data.split('\n')
    header = None
    for i, line in enumerate(lines):
        values = line.split()
        if i == 0:
            for value in values:
                biosum[value] = {}
            header = values
            continue
        curLetter = None
        for j, value in enumerate(values):
            if j == 0:
                curLetter = value
                continue
            biosum[curLetter][header[j - 1]] = value
    print(biosum)
    return biosum



if __name__ == __name__:
    if len(sys.argv) != 5:
        print('Please start with 4 parameters: Gap Penality, Path to biosum, Path to sequence 1, Path to sequence 2')

    align_sequences(int(sys.argv[1]), readBiosum(sys.argv[2]), readSequence(sys.argv[3]), readSequence(sys.argv[4]))
