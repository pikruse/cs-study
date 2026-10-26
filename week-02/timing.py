"""
timing.py

returns the seconds `x in container` takes using `timeit`
"""
import timeit

def time_membership(container, x, reps=1000):
    """return the seconds that x in container takes with timeit"""
    t = min(timeit.repeat(lambda: x in container, number=reps, repeat=5))
    return t

for n in (10_000, 20_000, 40_000, 80_000):
    # create data structures
    l = list(range(n))
    s = set(range(n))
    d = dict.fromkeys(range(n))

    # time worst case for each data structure
    tl = time_membership(l, -1) / 1000
    ts = time_membership(s, -1) / 1000
    td = time_membership(d, -1) / 1000

    # print
    print(f"n={n} | list time: {tl} | set time: {ts} | dict time: {td}") 