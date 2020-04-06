'''
What is an array and how does it work?
* Stores a sequence of elements
* Each element must be the same data type
* Occupies a contiguous block of memory
* Can access access data in constant time with this equation: memory_address = starting_address + index * data_size
What is an hash function and how does it work?
* Deterministic: For a given input, the output will always be the same.
* Defined output range: For a hash table of size 16, all keys must hash to a value 0-15. For smaller values, this is usually accomplished using the modulo % operation.
* Predictable Speed: Hash functions for hash tables should be lightning fast while cryptographic hashes (like bcrypt) should be very slow.
* Non-invertible: You should not be able to reconstruct the input value from the output. This trait is important in cryptographic hashes but not necessary for general hash tables.




What is a hash table and how does it work?
* Hash Tables have an underlying Array structure
* This is why they are as fast at accessing elements as arrays
* The main difference is that Hash Tables are indexed using a hash function in an unordered fashion, whereas arrays are indexed via a contiguous ordered indeces
* HashTable code is fairly similar to DynamicArray code



'''

import time
import hashlib
import bcrypt
​
n = 1000000
key = b"STR"
​
print(f"Hashing {n}x")
​
start_time = time.time()
for i in range(n):
    hash(key)
end_time = time.time()
print(f"  Python hash runtime: {end_time - start_time} seconds")
​
​
start_time = time.time()
for i in range(n):
    hashlib.sha256(key)
end_time = time.time()
print(f"  SHA256 hash runtime: {end_time - start_time} seconds")
​
​


def djb2(key):
    # Start from an arbitrary large prime
    hash_value = 5381
    # Bit-shift and sum value for each character
    for char in key:
        hash_value = ((hash_value << 5) + hash_value) + char
    return hash_value


​
start_time = time.time()
for i in range(n):
    djb2(key)
end_time = time.time()
print(f"  DJB2 hash runtime: {end_time - start_time} seconds")
​
​
n = 10
print(f"\nHashing {n}x")
salt = bcrypt.gensalt()
start_time = time.time()
for i in range(n):
    bcrypt.hashpw(b"KEY", salt)
end_time = time.time()
print(f"  bcrypt hash runtime: {end_time - start_time} seconds")
