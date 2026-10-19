def stamps(n):
    """
    Return (a, b) with n = 3a + 7b and a, b >= 0, for n >= 12.
    """
    # the claim only covers n >= 12 (11, 8, 5, 2 can't be made)
    if n < 12:
        raise ValueError(f"{n} is below 12, so it isn't covered by the claim")

    # base cases: checked by hand
    if n == 12:
        return (4, 0)   # 3*4 + 7*0
    if n == 13:
        return (2, 1)   # 3*2 + 7*1
    if n == 14:
        return (0, 2)   # 3*0 + 7*2

    # inductive hypothesis: P(n-3) holds, so stamps(n - 3) gives its (a, b)
    a, b = stamps(n - 3)

    # inductive step: add one 3c stamp
    return (a + 1, b)


if __name__ == "__main__":
    # check the claim: every n from 12 to 199 gets valid, nonnegative a and b
    for n in range(12, 200):
        a, b = stamps(n)
        assert a >= 0 and b >= 0 and 3*a + 7*b == n, (n, a, b)
    print("stamps: valid (a, b) for every n from 12 to 199")
    print("stamps(20) =", stamps(20))   # (2, 2): 3*2 + 7*2 = 20
