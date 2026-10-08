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
analysis:

As n increases, the unique_list function gets noticeably slower than the unique_set one.
I believe that this is because, for each seen number, a set will remove duplicates, and a list won't,
meaning that checking the seen numbers is much faster when they're stored in a set.
"""