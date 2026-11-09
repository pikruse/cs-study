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

if __name__ == "__main__":
    # tests
    print("testing binary search...")
    assert binary_search([], 0) == -1
    assert binary_search([1, 3, 5, 7, 9], 1) == 0
    assert binary_search([1, 3, 5, 7, 9], 3) == 1
    assert binary_search([1, 3, 5, 7, 9], 5) == 2
    assert binary_search([1, 3, 5, 7, 9], 7) == 3
    assert binary_search([1, 3, 5, 7, 9], 9) == 4
    assert binary_search([1, 3, 5, 7, 9], 0) == -1
    assert binary_search([1, 3, 5, 7, 9], 4) == -1
    assert binary_search([1, 3, 5, 7, 9], 10) == -1
    assert binary_search([2], 2) == 0
    print("10 tests passed!")

    print("testing contains...")
    xs = [3,1,2]
    assert contains(xs, 2) == True
    print("1 test passed!")
