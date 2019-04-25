import sys

def taylorSeries(x):
    if x >= 1:
        raise Exception("x has to be smaller than 1 for convergence")

    taylorSum = 1
    curPow = 1
    while True:
        yield taylorSum    
        taylorSum += x**curPow
        #print(x**curPow)
        curPow += 1


if __name__ == '__main__':
    x = float(sys.argv[1])
    n = int(sys.argv[2])

    print("Choosen x: " + str(x))
    print("Choosen n: " + str(n))

    taylorSum = 0
    try:
        taylorGen = taylorSeries(x)
        for i in range(n):
            taylorSum = next(taylorGen)
    except:
        print("Error! Taylor series only converges for x values smaller than 1")
        sys.exit()

    print("Sum of first {} terms wit x={} of series: {}".format(n, x, taylorSum))
