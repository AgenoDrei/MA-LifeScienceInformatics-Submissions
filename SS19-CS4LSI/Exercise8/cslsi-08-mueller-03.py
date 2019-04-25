glcs = ''

def lcs_naive(seq1, seq2, clcs=''):
    global glcs
    if len(clcs) > len(glcs):
        glcs = clcs
    if len(seq1) == 0 or len(seq2) == 0:
        return 0
    elif seq1[-1] == seq2[-1]:
        return 1 + lcs_naive(seq1[:-1], seq2[:-1], clcs=seq1[-1]+clcs)
    else:
        return max(lcs_naive(seq1[:-1], seq2, clcs=clcs), lcs_naive(seq1, seq2[:-1], clcs=clcs))


def lcs_dym(seq1, seq2):
    pass


if __name__ == '__main__':
    print('Starting...')
    lcs = lcs_naive('AGGTAB', 'GXTXAYB')
    lcs_dym = lcs_dym('AGGTAB', 'GXTXAYB')
    print('LCS: ', lcs, glcs[::-1])