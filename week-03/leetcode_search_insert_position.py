"""
leetcode_search_insert_position.py

Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.
"""

class Solution:

    def searchInsert(self, nums:list[int], target:int) -> int:
        lo, hi = 0, len(nums)-1
        # search for the target in the list
        while lo <= hi:
            mid = (lo+hi)//2
            if target == nums[mid]:
                # if target found, return in
                return mid
            elif target > nums[mid]:
                lo = mid + 1
            else:
                hi = mid - 1  
        # if target not found, return the index where it would be inserted
        # lo is the index where it would be inserted where the loop ends, because it's the index right above the not found target due to floor div
        return lo

if __name__ == "__main__":
    sol = Solution()
    assert sol.searchInsert([1,3,5,6], 5) == 2
    assert sol.searchInsert([1,3,5,6], 2) == 1
    assert sol.searchInsert([1,3,5,6], 7) == 4
    print("all tests passed")