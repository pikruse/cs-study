"""
twosum.py
You're given a list of integers and a target value. Return the indices of the two different positions whose values add up to the target. 
Each input has exactly one valid answer, and you can't use the same element twice. Indices can come back in any order.
"""

# twoSum function
class Solution:
    def myTwoSum(self, nums: list[int], target: int) -> list[int]:
        """my naive solution for twosum"""
        # loop through all numbers
        for idx1, num1 in enumerate(nums):
            for idx2 in range(idx1+1, len(nums)):
                if num1 + nums[idx2] == target:
                    return [idx1, idx2]


def is_valid(nums: list[int], target: int, answer: list[int]) -> bool:
    """an answer is valid if it names two different positions summing to target"""
    if len(answer) != 2:
        return False
    i, j = answer
    return i != j and nums[i] + nums[j] == target


if __name__ == "__main__":
    sol = Solution()
    cases = [
        ([2, 7, 11, 15], 9),
        ([3, 2, 4], 6),        # answer isn't at the front
        ([3, 3], 6),           # duplicates, and only two elements
        ([1, 5, 3], 4),        # sorting moves the answer's indices
        ([0, 4, 3, 0], 0),     # zeros
        ([-3, 4, 3, 90], 0),   # negatives
    ]
    # add faster solutions here as you build them (binary search in Week 3,
    # hash map in Week 7), and every one gets checked against the same cases
    solutions = [
        ("naive", sol.myTwoSum),
    ]
    for name, func in solutions:
        for nums, target in cases:
            original = list(nums)
            answer = func(nums, target)
            assert is_valid(original, target, answer), (name, original, target, answer)
            assert nums == original, f"{name} changed its input list"
        print(f"{name}: all {len(cases)} tests passed")


    
    
"""
approach:
    I used the naive approach here:
    1. initialize an outer index tracker from 0 and loop through nums in an outer loop
    2. initialize an inner index tracker from 0 and loop through nums in an inner loop
        - if indexes are the same, continue and raise inner index by one, moving to next num + index
        - if indexes aren't the same check the sum of outer and inner nums
            - if sum = target, return the indices
            - if sum ≠ target, increment the index
    3. the inner index tracker is reset to 0 each time through the loop

big-O:
    the big-O for this should be O(n^2), because as the length of nums grows, the processing time will quadruple due to the two loops.
    in order to improve the big-O, I can see a few possible avenues. using a search algorithm may improve the speed of checking each list.
    additionally, maybe a hash table can be used for faster checking? 
"""
