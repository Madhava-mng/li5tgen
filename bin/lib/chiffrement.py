#!/bin/env pyhton3
from hashlib import blake2s
from hashlib import blake2b
from lib.core import Element

def enc(string):
    return blake2s(blake2b(
            blake2s(string.encode()).hexdigest().encode()
            ).hexdigest().encode()
            ).hexdigest()


def dec(hash_string):
    for i in range(1, 40):
        if enc(str(i)+Element["KEYS"]) == hash_string:
            return str(i)

