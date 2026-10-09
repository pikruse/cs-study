import time
import random

def unique_list(nums):
    seen = []
    for num in nums:
        if num not in seen:
            seen.append(num)
    return seen

def unique_set(nums):
    seen = set()
    result = []
    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result

if __name__ == '__main__':
    print("Testing functions...")
    assert unique_list([3, 1, 3, 2, 1]) == [3, 1, 2]
    assert unique_set([3, 1, 3, 2, 1]) == [3, 1, 2]

    assert unique_list([]) == []
    assert unique_set([]) == []

    assert unique_list([7,7,7]) == [7]
    assert unique_set([7,7,7]) == [7]
    print("Tests passed.")

    # make a list of n, doubling from 1000 to 32000
    n = 1000
    while n <= 32000:
       print(f"n = {n}")
       numbers = random.choices(range(n), k=n)

       # time unique_list
       start = time.perf_counter()
       unique_list(numbers)
       end = time.perf_counter()
       ul_time = end - start
       print(f"unique_list time: {ul_time}")

       # time unique set
       start = time.perf_counter()
       unique_set(numbers)
       end = time.perf_counter()
       us_time = end - start
       print(f"unique_set time: {us_time}")

       n += n 

"""
# analysis:
unique_set is faster than unique_list, due to how each structure handles checks
in a list, python checks elements one-by-one until it finds a match or reaches the end, so that takes time proportional to how many values have been seen so far - O(k)
in a set, python hashes the number and jumps straight to the slot where it would be, which takes O(1) on average

# hashing
hashing lets a set check items without looking through everything.
instead of comparing elements one at a time, a set decides in advance where each value is stored, so a lookup can go straight to that spot

## step 1: a hash function turns a value into a number.
a hash function takes a value and returns an integer; the same value always gives the same number.
python has a built in hash function

## step 2: the number picks a slot
under the hood, a set is an array of slots. python takes the hash modulo the number of slots
"""