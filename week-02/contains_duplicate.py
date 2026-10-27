"""given a list of integers, return True if any value appears at least twice, and False if every value is distinct."""

import timeit
import random
import matplotlib.pyplot as plt

def contains_duplicate_set(lst: list[int]) -> bool:
    seen = set()
    for num in lst:
        if num in seen: 
            return True
        seen.add(num)
    return False

def contains_duplicate_list(lst: list[int]) -> bool:
    seen = []
    for num in lst:
        if num in seen: 
            return True
        seen.append(num)
    return False

def contains_duplicate_sort(lst: list[int]) -> bool:
    lst.sort()
    for i in range(0, len(lst) - 1):
        if lst[i] == lst[i+1]:
            return True
    return False

def time_func(func, repeat=5):
    """seconds for one call of func(), best of `repeat` runs"""
    timer = timeit.Timer(func)
    number, _ = timer.autorange()     # picks a number of calls that takes >= 0.2 s
    return min(timer.repeat(repeat=repeat, number=number)) / number

if __name__ == "__main__":
    # check functions agree
    for xs in ([], [1], [1, 2, 3], [1, 2, 2, 3], [3, 1, 2, 1], [5, 5]):
        assert contains_duplicate_set(xs) == contains_duplicate_list(xs) == contains_duplicate_sort(xs), xs

    # timeit comparison of worst case (distinct) list
    solutions = {
        "set": (contains_duplicate_set, [1_000, 2_000, 4_000, 8_000, 10_000]),
        "sort": (contains_duplicate_sort, [1_000, 2_000, 4_000, 8_000, 10_000]),
        "list": (contains_duplicate_list, [1_000, 2_000, 4_000, 8_000, 10_000])
    }

    for name, (func, sizes) in solutions.items():
        times = []
        for n in sizes:
            xs = random.sample(range(10 * n), n)
            times.append(time_func(lambda: func(xs)))
            print(f"{name:>4} | n={n:>9} | {times[-1]:.2e} s")
        plt.loglog(sizes, times, "o-", label=name)

    plt.xlabel("n (list length)")
    plt.ylabel("seconds per call")
    plt.legend()
    plt.grid(True, which="both", alpha=0.3)
    plt.savefig("contains_duplicate_plot.png", dpi=150, bbox_inches="tight")
    plt.show()


    