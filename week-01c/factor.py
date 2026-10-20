def factor(n: int) -> list[int]:
    """given an integer n, return primes whose product is n, for n ≥ 2."""
    # check n ≥ 2
    assert n >= 2, "n must be ≥ 2!"

    # base case: n is 2
    if n == 2:
        return [n]

    # prime case: k+1 prime (try divisors d from 2 while d*d ≤ n)
    d = 2
    while d*d <= n:
        if n % d == 0:
            # using the strong hypothesis: vals smaller than n are recursed upon
            return factor(d) + factor(n//d)
        else:
            d+=1 
    return [n]

if __name__ == "__main__":
    # test cases
    print("testing...")
    assert factor(2) == [2]
    assert sorted(factor(12)) == [2, 2, 3]
    assert sorted(factor(97)) == [97]
    assert sorted(factor(360)) == [2, 2, 2, 3, 3, 5]
    from math import prod
    assert all(prod(factor(n)) == n for n in range(2, 2000))
    print("all tests passed!")