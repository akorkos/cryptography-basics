ALPHABET = 'αβγδεζηθικλμνξοπρστυφχψω'


def decrypt(cipher: str, n: int) -> str:
    dec = ''
    for char in cipher:
        dec += ALPHABET[(ALPHABET.index(char) - n) % len(ALPHABET)]
    return dec


if __name__ == '__main__':
    cipher = 'οκηθμφδζθγοθχυκχσφθμφμχγ'

    print('[1] Decrypted message:', decrypt(cipher, 3))
