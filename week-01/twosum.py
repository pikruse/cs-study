"""
twosum.py
You're given a list of integers and a target value. Return the indices of the two different positions whose values add up to the target. 
Each input has exactly one valid answer, and you can't use the same element twice. Indices can come back in any order.
"""

# twoSum function
class Solution:
    def myTwoSum(self, nums: list[int], target: int) -> list[int]:
        """my naive solution for twosum"""
        idx1 = 0
        # loop through all numbers
        for num1 in nums:
            idx2 = 0
            for num2 in nums:
                if idx1 == idx2:
                    idx2 += 1
                    continue
                if num1 + num2 == target:
                    return [idx1, idx2]
                idx2 += 1 
            idx1 += 1

    def BinarySearch(self,nums: list[int], left, right, target):
        """
        Binary search on a sorted array

        Args:
            nums - the list to search
            left - the leftmost index to search from
            right - the rightmost index to search from 
            target - the target value to search for 
        
        """

        # ensure that the leftmost index is leq rightmost
        while left <= right:
            # find the middle index
            mid = left + (right - left) // 2

            # if the midpoint is equal to the target, end
            if nums[mid] == target:
                return mid
            # if the midpoint is less than the target, search only the right side
            elif nums[mid] < target:
                left = mid + 1
            # if the midpoint is greater than the target, search only the left side
            else:
                right = mid - 1
        return False


    def bestTwoSum(self, nums: list[int], target: int) -> list[int]:
        """the best two sum solution, in O(n) time"""
        # sort the array in non-decreasing order
        nums.sort()

        # loop through each element of the list from index 0 to index n - 2 (leaves space for final check)
        for idx in range(0, len(nums)-2):
            # search for the number's complement (target - num1)
            complement = target - nums[idx]

            # perform binary search for the complement from index i+1 to n-1
            binsearch = self.BinarySearch(nums, idx+1, len(nums)-1, complement)
            if binsearch:
                print(idx, binsearch)
                return [idx, binsearch]

if __name__ == "__main__":
    sol = Solution()
    # checks
    """
    print("my two sum")
    if sol.myTwoSum(nums = [2,7,11,15], target = 9) == [0, 1]:
        print("test 1 passed")
    if sol.myTwoSum(nums = [3,2,4], target = 6) == [1, 2]:
        print("test 2 passed")
    if sol.myTwoSum(nums = [3,3], target = 6) == [0, 1]:
        print("test 3 passed")
    """

    print("best two sum")
    sol.bestTwoSum(nums = [2,7,11,15], target = 9)
    sol.bestTwoSum(nums = [3,2,4], target = 6)
    sol.bestTwoSum(nums = [3,3], target = 6)


    
    
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
    the big-O for this should be O^2, because as the length of nums grows, the processing time will double due to the two loops.
    in order to improve the big-O, I can see a few possible avenues. using a search algorithm may improve the speed of checking each list.
    additionally, maybe a hash table can be used for faster checking? 

analysis of the best solution:
    1. first, sort the array
    2. then, for each index in the array, check the complement


"""
