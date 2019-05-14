import needle

if __name__ == '__main__':
    print('Task 3')
    print()
    print('Subtask 1')
    argv = [None, -8, 'blosum62.txt', 'seq1.fasta', 'seq2.fasta']
    needle.run(argv)

    print()
    print('Subtask 3')
    files = ['RNAS1_red-kangaroo.fasta', 'RNAS1_minke-whale.fasta', 'RNAS1_horse.fasta']

    for f in files:
        for f2 in files:
            if f == f2:
                continue
            argv = [None, -8, 'blosum50.txt', f, f2]
            needle.run(argv)

    print()
    print('Subtask 5')
    argv = [None, -8, 'blosum62.txt', 'halodurans.fasta', 'lentus.fasta']
    needle.run(argv)

