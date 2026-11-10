# Week 3 Exercises:

## Task 1:

### Question 1.1:
Start at capacity 1 and double whenever the list is full. How many item copies do 16 appends cause in total? What about 17? Give the copies per append for each.

* 16 appends require 15 copies (1+2+4+8=15). 17 appends require 5 copies (1+2+4+8+16=31).

* For 16, there are $\frac{15}{16} = 0.94$ copies/append. For 17, there are $\frac{31}{17} \approx 1.82$ copies/append.

### Question 1.2:
```{python}
import sys
xs = []
for i in range(64):
    xs.append(i)
    print(len(xs), sys.getsizeof(xs))
```
Note the lengths where the size jumps. CPython grows the list by about 1/8 plus a few slots, not 2$\times$. Is `append` still amortized by O(1)? What if the list grew by a fixed 100 slots each time?

* The size jumps from 4 to 5, 8 to 9, 16 to 17, 24 to 25, 32 to 33, 40 to 41, and 52 to 53. 

* If CPython grows the list by 1/8 plus a few slots, then each copy adds at least 1.125 times the slots. so working backwards, the resizes add $n, \frac{n}{1.125}, \frac{n}{1.125^2}, \dots$ items. Since this is a geometric series, just like the $2n$ version, it still amortizes to O(1).

* If the list grew by a fixed 100 slots, then each successive copy would add $100, 200, \dots n$ items, which grows quadratically (just like $1 + 2 + \cdots + n$). So per append, this amortizes to $\Theta(n)$ instead of O(1).

---

## Review:
### Question 2.1:
A dynamic array starts at capacity 4 and triples whenever it’s full. How many item copies do the first 40 appends cause in total, and how many is that per append? Is append amortized $O(1)$?

### Question 2.2:
Someone says “append is $O(1)$ on average, because most appends are cheap.” What’s wrong with using the word “average” here? What does “amortized $O(1)$” actually guarantee, and can a single append still be slow?

### Question 2.3:
Your loop keeps “if `target` is in `xs`, its index is in `[lo, hi]`” and runs while `lo <= hi`.
    (a) When `xs[mid] < target`, why is `lo = mid + 1` correct?
    (b) What goes wrong with `lo = mid`?
    (c) In the worst case, how many passes does the loop make for `n = 1,000,000`?

### Question 2.4
Give $T(n)$, the exact number of times `body()` runs when $n=2^k$, and its $\Theta$:
```{python}
i = 1
while i < n:
    for j in range(i):
        body()
    i *= 2
```
* $T(n) = 1 + \log_2 n$
* `body()` runs ___ times when $n=2^k$
* $\Theta$
