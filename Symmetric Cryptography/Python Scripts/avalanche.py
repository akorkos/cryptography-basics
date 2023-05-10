from random import randint
from Crypto.Cipher import AES
from bitstring import BitArray
from statistics import mean


def createMessages(N: int = 256) -> list:
    m1 = []
    m2 = []
    for _ in range(N):
        bit = str(randint(0, 1))
        m1.append(bit)
        m2.append(bit)
    pos = randint(0, N - 1)
    if m1[pos] == '0':
        m2[pos] = '1'
    else:
        m2[pos] = '0'
    return [''.join(m1), ''.join(m2)]


# https://stackoverflow.com/questions/32675679/convert-binary-string-to-bytearray-in-python-3
def toBytes(number: str) -> bytes:
    return int(number, 2).to_bytes(len(number) // 8, byteorder='big')


def randomBinaryNumberGenerator(N: int) -> str:
    return ''.join([str(randint(0, 1)) for _ in range(N)])


def diff(a: BitArray, b: BitArray):
    return sum(a[i] != b[i] for i in range(len(a)))


def encrypt(key: bytes, mode: AES, iv: str = '', N: int = 200) -> int:
    changes = [0 for _ in range(N)]
    for i in range(N):
        if mode is AES.MODE_CBC:
            algorithm = AES.new(key, mode, toBytes(iv))
        else:
            algorithm = AES.new(key, mode)
        m = createMessages()
        c1 = BitArray(algorithm.encrypt(toBytes(m[0])))
        c2 = BitArray(algorithm.encrypt(toBytes(m[1])))
        changes[i] = diff(c1, c2)
    return int(mean(changes))


if __name__ == '__main__':
    N = 128
    key = randomBinaryNumberGenerator(N)
    iv = randomBinaryNumberGenerator(N)
    print('[ECB] Average bits changed:', encrypt(toBytes(key), AES.MODE_ECB))
    print('[CBC] Average bits changed:', encrypt(toBytes(key), AES.MODE_CBC, iv))
