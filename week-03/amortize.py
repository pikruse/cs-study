import sys
xs = []
for i in range(64):
    xs.append(i)
    print(len(xs), sys.getsizeof(xs))