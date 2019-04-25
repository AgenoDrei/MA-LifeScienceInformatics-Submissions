import math
import sys
import random
import operator
import collections

def ex1():
    multiplier = 2 * math.sqrt(2) / 9801
    multiplier2 = 0
    summand = sys.maxsize
    i = 0
    while summand >= 1e-15:
        summand = (math.factorial(4.0*i) * (1103.0 + 26390.0*i)) / (math.pow(math.factorial(i), 4.0) * math.pow(396.0, 4.0*i))
        multiplier2 += summand
        i+=1

    estimated_pi = 1.0 / (multiplier * multiplier2)
    print(f"PI estimation error: {math.pi - estimated_pi}")
    return estimated_pi

def ex2():
    happyness = [is_happy_number(x) for x in range(1, 101)]
    print(f"Happyness of the first 100 numbers: {dict(enumerate(happyness))}")
    return enumerate(happyness)

def is_happy_number(num):
    assert num > 0
    while num != 1 and num != 4:
        digits = str(num)
        num = 0
        for digit in digits:
            num += int(math.pow(int(digit), 2))
    return True if num == 1 else False

def is_happy_number_rec(num):
    assert num > 0
    num = int(num)
    if num == 1:
        return True
    elif num == 4:
        return False
    digits = str(num)
    num = 0
    for digit in digits:
        num += int(int(digit)**2)
    is_happy_number_rec(num)

def is_happy_number_cube(num):
    pass


def ex3():
    NUM_PERSONS = 27
    NUM_TRIALS = 10_000
    NUM_DAYS = 365
    num_duplicates = 0
    num_triplicates = 0
    for i in range(NUM_TRIALS):
        birthdays = [random.randint(0, NUM_DAYS) for x in range(NUM_PERSONS)]
        if has_duplicates(birthdays):
            num_duplicates += 1
        if has_triplicates(birthdays):
            num_triplicates += 1
    estimated_prob = num_duplicates / NUM_TRIALS
    approximated_prob = 1 - math.pow(math.e, -1*(NUM_PERSONS**2 / (2 * NUM_DAYS)))
    estimated_prob_triplicates = num_triplicates / NUM_TRIALS

    print(f"Propability over {NUM_TRIALS} trials with {NUM_PERSONS} Persons is: {estimated_prob}")
    print(f"Approximated propability over {NUM_TRIALS} trials with {NUM_PERSONS} Persons is: {approximated_prob}")
    print(f"Estimated propability for three people sharing a non-unique birthday over {NUM_TRIALS} trials with {NUM_PERSONS} Persons is: {estimated_prob_triplicates}")




def has_duplicates(nums):
    counts = dict()
    for num in nums:
        cur_num = counts.get(num)
        if cur_num == None:
            counts[num] = True
        else:
            return True
    return False

def has_triplicates(nums):
    num_duplicates = 0
    counts = dict()
    for num in nums:
        cur_num = counts.get(num)
        if cur_num == None:
            counts[num] = 1
        elif(cur_num == 1):
            counts[num] += 1
            num_duplicates += 1
        else:
            return True
        if num_duplicates > 1:
            return True
    return False


def ex4():
    anagrams = []
    with open("words.txt") as f:
        raw_input = f.read()
        words = raw_input.split("\n")

    print(f"Number of words: {len(words)}")
    sorted_words = {word:custom_hash(word) for word in words}
    sorted_hashs = sorted(sorted_words.items(), key=operator.itemgetter(1))
    current_ana, current_ana_count,  total_ana_count = None, 0, 0
    for i in range(len(sorted_hashs) - 1):
        word = sorted_hashs[i]
        if current_ana == None:
            current_ana = word[1]
            current_ana_count += 1
        elif current_ana == sorted_hashs[i+1][1]:
            current_ana_count += 1
        elif current_ana != sorted_hashs[i+1][1]:
            current_ana = None
            if current_ana_count > 5:
                anagram_list = [sorted_hashs[i-x][0] for x in range(current_ana_count)]
                anagrams.append(anagram_list)
                total_ana_count += current_ana_count
            current_ana_count = 0
    print(f"Number of anagrams found: ", total_ana_count)

    anagrams.sort(key = lambda ana: len(ana), reverse=True)
    print(anagrams)

def custom_hash(word: str) -> int:
    return hash(frozenset(collections.Counter(word).items()))


if __name__ == '__main__':
    ex1()
    ex2()
    ex3()
    ex4()