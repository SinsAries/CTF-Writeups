import string
import random

flag = "W1{s0m3_r3ad4ble_5tr1ng_like_7his}" # Test flag

alphabet = string.ascii_letters + string.digits + "!{_}?"
assert all(i in alphabet for i in flag)


for i in range(3):
    k = random.randint(0, len(alphabet))
    alphabet = alphabet[:k] + alphabet[k+1:]


key = random.randint(0, 2**256)

ct = ""
for i in flag:
    ct += (alphabet[(alphabet.index(i) + key) % len(alphabet)])

print(f"{ct=}")


"""
ct = 'RV5tUp6{?Zo6Ht6xvY0ZM6{p26CiR44947'
"""
