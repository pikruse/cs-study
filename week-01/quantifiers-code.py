import random

def has_pair(nums, t):
    # there exists an i < j such that nums[i] + nums[j] == t
    return any(nums[i] + nums[j] == t
               for i in range(len(nums))
               for j in range(i+1, len(nums))
               )


def not_has_pair(nums, t):
    # for all i < j: nums[i] + nums[j] != t
    return all(nums[i] + nums[j] != t
               for i in range(len(nums))
               for j in range(i+1, len(nums))
               )

for _ in range(1000):
    nums = [random.randint(-5, 5) for _ in range(random.randint(0,6))]
    t = random.randint(-10, 10)
    assert (not has_pair(nums, t)) == not_has_pair(nums, t)

print("negation checks passed on 1,000 random lists")

