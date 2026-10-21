"""
Problem:
    A staircase has n steps (n ≥ 1). each move climbs either 1 or 2 steps.
    Return how many different ordered sequences of moves reach the top exactly.
    For example, n=3 has 3 ways: 1+1+1, 1+2, 2+1

Approach:
    0. check that n >= 1:
    1. init a global variable to count remaining_steps at n, and a num_steps var at 0
    2. check if remaining_steps == 0
        - if yes return num_steps (which will have been incremented recursively)
        - if no, run stairs(n-1) and stairs (n-2); this will recursively call
    3. at the end of the function call, increment num_steps by 1
"""
def stairs(n: int) -> int:
    """return the number of ways to climb up n steps by taking 1 or 2 steps at a time"""
    num_ways = 0
    if n == 1:
        return 1 
    if n == 2:
        return 2 
    if n >= 3:
        num_ways += stairs(n-1)
        num_ways += stairs(n-2)
    return num_ways

def stairs2(n: int) -> int:
    num_ways = 0
    n1 = 1
    n2 = 2
    if n == 1:
        return 1
    if n == 2:
        return 2
    for _ in range(2, n):
        num_ways = (n1 + n2)
        n1, n2 = n2, n1+n2
    return num_ways
        
if __name__ == "__main__":
    print("Checking test cases...")
    assert stairs2(1) == 1
    assert stairs2(2) == 2
    assert stairs2(3) == 3
    assert stairs2(4) == 5
    assert stairs2(5) == 8
    assert stairs2(6) == 13
    print("All cases passed!")
