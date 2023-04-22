import re
import sys
from math import gcd, sqrt
from functools import reduce

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
FREQUENCIES = [0.082, .015, .028, .043, .13, .022, .02, .061, .07, .0015, .0077, .04, .024, .067, .075, .019, .00095,
               .06, .063, .091, .028, .0098, .024, .0015, .02, .00074]

def cosangle(x: list, y: list) -> float:
    xy = 0
    xx = 0
    yy = 0
    for i in range(len(x)):
        xy += x[i] * y[i]
        xx += x[i] ** 2
        yy += y[i] ** 2
    return xy / sqrt(xx * yy)


# https://www.cipherchallenge.org/wp-content/uploads/2020/12/Five-ways-to-crack-a-Vigenere-cipher.pdf
def frequencyAnalysis(offset: int, cipher: str) -> str:
    slices = ['' for _ in range(offset)]
    for i in range(len(cipher)):
        slices[i % offset] += cipher[i]

    frequencies = [[0 for _ in range(26)] for __ in range(offset)]
    for i in range(offset):
        for j in range(len(slices[i])):
            frequencies[i][ALPHABET.index(slices[i][j])] += 1
        for j in range(26):
            frequencies[i][j] = frequencies[i][j] / len(slices[i])

    key = ['A' for _ in range(offset)]
    for i in range(offset):
        for j in range(26):
            testtable = frequencies[i][j:]+frequencies[i][:j]
            if cosangle(FREQUENCIES, testtable) > 0.9:
                key[i] = ALPHABET[j]
    return ''.join(key)

def diff(a: str, b: str) -> str:
    return ALPHABET[(ALPHABET.index(a) - ALPHABET.index(b)) % len(ALPHABET)]

def decrypt(cipher: str, key: str):
    key_len = len(key)
    message = ''

    for i, ci in enumerate(cipher):
        # Note: mi + ki = ci, then mi = ci - ki
        ki = key[i % key_len]
        mi = diff(ci, ki)
        message += mi
    return message


# https://github.com/ragunggg/kasiski/blob/master/kasiski.py
def kasiski(cipher: str) -> int:
    pattern = re.compile(r'(?=(\w{5}))')
    matches = pattern.finditer(cipher)
    fragments = [match.group(1) for match in matches]
    occurrenceIndexes = {fragment: [m.start(0) for m in re.finditer(fragment, cipher)] for fragment in fragments}
    filteredOccurrenceIndexes = dict(filter(lambda item: len(item[1]) > 1, occurrenceIndexes.items()))
    gcdAppliedOnOccurrences = {}

    # https://stackoverflow.com/questions/29194588/python-gcd-for-list
    for key, value in filteredOccurrenceIndexes.items():
        d = [value[i] - value[i - 1] for i in range(1, len(value))]
        gcdAppliedOnOccurrences[key] = reduce(gcd, d)
    return int(reduce(gcd, gcdAppliedOnOccurrences.values()))


if __name__ == "__main__":
    name = 'vigenere.txt'
    if len(sys.argv) > 1:
        name = str(sys.argv[1])
    file = open(name, 'r')
    cipher = file.read()
    keyLength = kasiski(cipher)
    key = frequencyAnalysis(keyLength, cipher)
    dec = decrypt(cipher, key)
    print('[1] Key length: ' + str(keyLength) + '\n[2] Keyword: ' + key + '\n[3] Decrypted text: \n' + dec)
