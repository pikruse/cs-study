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

    # time best case for each data structure
    tl_best = time_membership(l, 0) / 1000
    ts_best = time_membership(s, 0) / 1000
    td_best = time_membership(d, 0) / 1000

    # time worst case for each data structure
    tl_worst = time_membership(l, -1) / 1000
    ts_worst = time_membership(s, -1) / 1000
    td_worst = time_membership(d, -1) / 1000

    # print
    print(f"n={n}")
    print(f"BEST CASE | list time: {tl_best} | set time: {ts_best} | dict time: {td_best}") 
    print(f"WORST CASE | list time: {tl_worst} | set time: {ts_worst} | dict time: {td_worst}")