"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

My approach:
    1. sort the list and loop through it with range(0, len(nums)+1)
    2. check each number against the index + 1: 
        - if they're equal, continue
        - if they're not equal, return the index (number missing)
    3. edge case: the last number in the range does not exist
        - at the loop's end, return len(nums) (last number)

Complexity:
    1. the time complexity should be O(n), growing linearly with the list

Alternative approaches:
    1. sum the given list, and sum the list created by range(1, list_maximum). take the difference, and that should be the missing number.
    2. store items in a set and check for the missing hash?
"""
import math

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        # sort nums
        nums.sort()
        for i in range(0, len(nums)):
            if i != nums[i]:
                return i
        return len(nums)

    def missingNumberSum(self, nums: list[int]) -> int:
        num_sum = sum(nums)
        range_sum = sum([i for i in range(0, len(nums)+1)])
        return range_sum - num_sum

    def missingNumberSumImproved(self, nums: list[int]) -> int:
        num_sum = sum(nums)
        n = len(nums)
        range_sum = int(n*(n+1)/2)
        return range_sum - num_sum

    def missingNumberSet(self, nums: list[int]) -> int:
        numset = set(nums)
        rangeset = set(i for i in range(0, len(nums)+1))
        return rangeset.difference(numset).pop()



if __name__ == "__main__":
    sol = Solution()
    print("naive solution:")
    print(sol.missingNumber(nums = [3, 0, 1]))
    print(sol.missingNumber(nums = [0, 1]))
    print(sol.missingNumber(nums = [9,6,4,2,3,5,7,0,1]))
    print("")
    
    print("sum solution:")
    print(sol.missingNumberSum(nums = [3, 0, 1]))
    print(sol.missingNumberSum(nums = [0, 1]))
    print(sol.missingNumberSum(nums = [9,6,4,2,3,5,7,0,1]))
    print("")

    print("improved sum solution:")
    print(sol.missingNumberSumImproved(nums = [3, 0, 1]))
    print(sol.missingNumberSumImproved(nums = [0, 1]))
    print(sol.missingNumberSumImproved(nums = [9,6,4,2,3,5,7,0,1]))
    print("")

    print("set solution:")
    print(sol.missingNumberSet(nums = [3, 0, 1]))
    print(sol.missingNumberSet(nums = [0, 1]))
    print(sol.missingNumberSet(nums = [9,6,4,2,3,5,7,0,1]))
    print("") 