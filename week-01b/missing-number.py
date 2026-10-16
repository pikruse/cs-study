"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

My approach:
    1. sort a copy of the list and loop through it with range(0, len(nums))
    2. check each number against its index:
        - if they're equal, continue
        - if they're not equal, return the index (number missing)
    3. edge case: the last number in the range (n) is missing
        - at the loop's end, return len(nums) (last number)

Complexity:
    1. sorting is O(n log n) and the loop is O(n), so the sort dominates: O(n log n) time overall

Alternative approaches:
    1. sum the given list, and sum the list created by range(0, len(nums)+1). take the difference, and that should be the missing number.
        - building the range as a list: O(n) time, O(n) extra space
        - using the formula n(n+1)/2 instead (Proof 5.1): O(n) time, O(1) extra space
    2. store items in a set and take the difference with the full range: O(n) time, O(n) extra space
"""
import random

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        # sort a copy, so the caller's list isn't changed
        nums_sorted = sorted(nums)
        for i in range(0, len(nums_sorted)):
            if i != nums_sorted[i]:
                return i
        return len(nums_sorted)

    def missingNumberSum(self, nums: list[int]) -> int:
        num_sum = sum(nums)
        range_sum = sum([i for i in range(0, len(nums)+1)])
        return range_sum - num_sum

    def missingNumberSumImproved(self, nums: list[int]) -> int:
        num_sum = sum(nums)
        n = len(nums)
        # n(n+1) is always even (quantifiers Task 2), so // is exact.
        # / would make a float, which loses precision for large n.
        range_sum = n*(n+1)//2
        return range_sum - num_sum

    def missingNumberSet(self, nums: list[int]) -> int:
        numset = set(nums)
        rangeset = set(i for i in range(0, len(nums)+1))
        return rangeset.difference(numset).pop()



if __name__ == "__main__":
    sol = Solution()
    cases = [
        ([3, 0, 1], 2),
        ([0, 1], 2),                       # n itself is missing
        ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
        ([], 0),                           # empty list
        ([1], 0),                          # 0 is missing
    ]
    # random cases: remove one number from 0..n, then shuffle
    for _ in range(1000):
        n = random.randint(0, 50)
        m = random.randint(0, n)
        nums = [x for x in range(n + 1) if x != m]
        random.shuffle(nums)
        cases.append((nums, m))

    solutions = [
        ("naive (sort)", sol.missingNumber),
        ("sum", sol.missingNumberSum),
        ("sum formula", sol.missingNumberSumImproved),
        ("set", sol.missingNumberSet),
    ]
    for name, func in solutions:
        for nums, expected in cases:
            original = list(nums)
            answer = func(nums)
            assert answer == expected, (name, original, expected, answer)
            assert nums == original, f"{name} changed its input list"
        print(f"{name}: all {len(cases)} tests passed")
