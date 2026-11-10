"""
leetcode_binary_search.py
    - Given an array of integers nums which is sorted in ascending order,
    and an integer target, write a function to search target in nums. 
    If target exists, then return its index. Otherwise, return -1.

analysis
    - set 
"""

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """search for target in nums. if target exists, return its index. otherwise, return -1"""
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1

if __name__ == "__main__":
    soln = Solution()
    assert soln.search([-1,0,3,5,9,12], 9) == 4
    assert soln.search([-1,0,3,5,9,12], 2) == -1
    assert soln.search([5], 5) == 0
    assert soln.search([2,5], 5) == 1
    assert soln.search([-1,0,5], 5) == 2
    print("All tests passed.")
