def Recurse(Seq1, Seq2, m, n):
    if(m == 0 or n == 0):
        return ''
    elif(Seq1[m - 1] == Seq2[n - 1]):
        return Recurse(Seq1, Seq2, m - 1, n - 1) + Seq1[m - 1]
    else:
        return max(Recurse(Seq1, Seq2, m - 1, n), Recurse(Seq1, Seq2, m, n - 1), key=len)


def Dyn(Seq1, Seq2, m, n):
    P = [[None for x in range(n + 1)] for y in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                P[i][j] = 0
            elif Seq1[i - 1] == Seq2[j - 1]:
                P[i][j] = P[i - 1][j - 1] + 1
            else:
                P[i][j] = max(P[i - 1][j], P[i][j - 1])
    Subseq = ''
    while m > 0 and n > 0:
        if (Seq1[m - 1] == Seq2[n - 1]):
            Subseq = Seq1[m - 1] + Subseq
            m -= 1
            n -= 1
        elif (P[m - 1][n] > P[m][n - 1]):
            m -= 1
        else:
            n -= 1

    return(Subseq)


Seq1 = 'GTTTGGGCCTTATTATGGCAT'
Seq2 = 'ATTTCCGTTGATTATTAAA'

print(Recurse(Seq1, Seq2, len(Seq1), len(Seq2)))
print(Dyn(Seq1, Seq2, len(Seq1), len(Seq2)))
