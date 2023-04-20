import re
from math import gcd
from functools import reduce


ALPHABET = "abcdefghijklmnopqrstuvwxyz".upper()
FREQUENCY = {
    'A': 0.082, 'B': 0.015, 'C': 0.028, 'D': 0.043, 'E': 0.13, 'F': 0.022, 'G': 0.02, 'H': 0.061,
    'I': 0.07, 'J': 0.0015, 'K': 0.0077, 'L': 0.04, 'M': 0.024, 'N': 0.067, 'O': 0.075, 'P': 0.019,
    'Q': 0.00095, 'R': 0.06, 'S': 0.063, 'T': 0.091, 'U': 0.028, 'V': 0.0098, 'W': 0.024, 'X': 0.0015,
    'Y': 0.02, 'Z': 0.00074
}

def alphabet_diff(a, b):
    """Compute (a - b) inside alphabet."""
    return ALPHABET[(ALPHABET.index(a) - ALPHABET.index(b)) % len(ALPHABET)]


def findKey(message, keyLength):
    key = ""
    for i in range(keyLength):
        # initialize dictionaries to store letter occurances
        positionalDict = {}
        scoredDict = {}
        for letter in ALPHABET:
            positionalDict[letter] = {}
            scoredDict[letter] = 0
            for letter2 in ALPHABET:
                positionalDict[letter][letter2] = 0

        # iterate through each potential letter for the key position
        for letter in ALPHABET:
            index = i
            while index < len(message):
                row = ALPHABET.find(message[index])
                column = ALPHABET.find(letter)
                positionalDict[letter][ALPHABET[(row - column) % 26]] += 1
                index = index + keyLength
            print(positionalDict)
            # frequency analysis score by multiplying a character's natural frequency and occurances in the cipher
            for char in ALPHABET:
                scoredDict[letter] += positionalDict[letter][char] * FREQUENCY[char]

        # find the letter with the highest score
        letter = max(scoredDict, key=scoredDict.get)
        key = key + letter

    return key





def vigener_decrypt(ciphertext, key):
    """
    Decrypt Vigener-ciphered text.

    Args:
        ciphertext (str): Vigener-ciphered text.
        key (int): Secret key.

    Returns:
        str: Decrypted message.
    """

    key_len = len(key)
    message = ''

    for i, ci in enumerate(ciphertext):
        # Note: mi + ki = ci, then mi = ci - ki
        ki = key[i % key_len]
        mi = alphabet_diff(ci, ki)
        message += mi

    return message



# https://github.com/ragunggg/kasiski/blob/master/kasiski.py

f = open('vigenere.txt', 'r')
cipher = f.read()

pattern = re.compile(r'(?=(\w{5}))')

matches = pattern.finditer(cipher)

fragments = [match.group(1) for match in matches]

occurrenceIndexes = {fragment: [m.start(0) for m in re.finditer(fragment, cipher)] for fragment in fragments}

filteredOccurrenceIndexes = dict(filter(lambda item: len(item[1]) > 1, occurrenceIndexes.items()))

t = {}

# https://stackoverflow.com/questions/29194588/python-gcd-for-list
for key, value in filteredOccurrenceIndexes.items():
    d = [value[i] - value[i - 1] for i in range(1, len(value))]
    t[key] = reduce(gcd, d)

N = reduce(gcd, t.values())

findKey(cipher, 7)

