import re
from hashlib import *
from functools import reduce
from pypbc import *

def read_string(filepath):
    with open(filepath, encoding = 'utf-8') as file:
        return file.read()


def read_word(filepath):
    word_list = []
    with open(filepath, encoding = 'utf-8') as file:
        for line in file:
            word_list += re.compile(r'\w+').findall(line)
    return word_list

def read_word_as_bytes(filepath):
    return [bytes(w, encoding = 'utf-8') for w in read_word(filepath)]

def obj2bytes(obj):
    return obj if type(obj) == bytes else str(obj).encode('utf-8')

def bxor(b1, b2):
    """ 字节数组的异或运算 """
    l1, l2 = len(b1), len(b2)
    if l1 < l2:
        return bxor(b2, b1)
    res = bytearray(b1,'utf-8')
    start = l1 - l2
    for i, b in enumerate(b2):
        res[start + i] ^= b
    return bytes(res)

def bytes2bits(b):
    """ 字节数组转二进制串 """
    bit_str = bin(int.from_bytes(b, byteorder = 'big', signed = False))[2:]
    bit_str = '0' * ((len(b) * 8) - len(bit_str)) + bit_str
    return bit_str

def a1_param_generator(bits, n, save_path):
    """
    创建type a1类型的参数，并将其写入指定的save_path，最后返回所有子群的阶
    """
    primes = [get_random_prime(bits) for _ in range(n)]
    param = Parameters(n = reduce(lambda e1, e2: e1 * e2, primes))
    with open(save_path, 'w') as f:
        f.write(str(param))
    return primes

def sha256str(b):
    return sha256(b).hexdigest()

def md5str(b):
    return md5(b).hexdigest()