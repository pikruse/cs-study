"""search.py"""

# if target is in xs, its index is in lo, hi
# 
def binary_search(xs, target) -> int:
    """returns index of target in the sorted list xs, or -1 if not found"""
    lo, hi = 0, len(xs) - 1
    # invariant: if the target is in xs, its index is in [lo, hi]
    while lo <= hi:
        mid = (lo + hi) // 2
        if target == xs[mid]:
            return mid
        elif target > xs[mid]:
            lo = mid + 1
        else:
            hi = mid - 1 
    return -1

def contains(xs, target):
    xs.sort()
    return binary_search(xs, target) != -1

print(binary_search([1,3,5,7], 5))
print(binary_search([1,3,5,7], 7))
print(binary_search([1,3,5,7], 4))
print(binary_search([], 1))
print(binary_search([2], 2))
