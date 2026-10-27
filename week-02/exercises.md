# Week 2: Big O Notation

**Idea:** Count basic steps/operations as a function $T(n)$, then keep only the term that dominates as $n$ gets large, dropping constant factors. Formally:
    * $O(g)$ (upper bound): there exist $c > 0$ and $n_0$ such that $T(n) \leq c \cdot g(n)$ for all $n \geq n_0$.
    * $\Omega(g)$ (lower bound): the same, but $T(n) \geq c \cdot g(n)$
    * $\Theta(g)$ (tight bound): both at once.
In order to prove this, pick $c$ and $n_0$ once, and then the bound must hold for *every* $n$ past $n_0$. Interviewers usually say Big-O to mean the tight bound.

---

## Task 1:

### Question 1.1:
Show that $T(n) = 3n^2 + 10n + 7$ is $O(n^2)$. Give explicit values of $c$ and $n_0$ and justify the inequality for all $n \geq n_0$.

To show $T(n)$ is $O(n^2)$, we need $c > 0$ and $n_0$ such that $3n^2 + 10n + 7 \leq cn^2$ for all $n \geq n_0$.

Let $c = 4$ and $n_0 = 17$. For $n \geq 17$, $\frac{10}{n} \leq \frac{10}{17}$ and $\frac{7}{n^2} \leq \frac{7}{289}$, so

$$
3 + \frac{10}{n} + \frac{7}{n^2} \leq 3 + \frac{10}{17} + \frac{7}{289} < 3 + 1 = 4.
$$

Multiplying by $n^2 > 0$ gives $3n^2 + 10n + 7 < 4n^2$ for all $n \geq 17$. So $T(n)$ is $O(n^2)$, with $c = 4$ and $n_0=17$. $\blacksquare$.


### Question 1.2:
Give the Big-O of this function and explain why in one sentence:

```{python}
def f(xs):
    total = 0
    for i in range(len(xs)):
        for j in range(i, len(xs)):
            total += xs[i] * xs[j]
    return total
```

The Big-O of this function is $O(n^2)$. First, we define $T(n)$. There's one variable assignment outside the loop (1). The inner loop runs $n-i$ times for each $i$, so the body runs $n + (n-1) + \cdots + 1 = n(n+1)/2$ times, giving $T(n) = \frac{n(n+1)}{2} + 1$. The $n^2$ term dominates as $n \rightarrow \infty$, so the function is $O(n^2)$.


### Proof 1.3:
Prove that $n^2$ is **not** $O(n)$. Use contradiction: assume $c$ and $n_0$ exist, then find an $n \geq n_0$ that breaks the inequality. Write out the negated quantifiers first.

Suppose, for contradiction, that $n^2$ is $O(n)$. Then $\exists c > 0$ and $\exists n_0$ satisfying $n^2 \leq cn \forall n \geq n_0$. Let $n \geq 0$ and $n > c$. Since $n \geq n_0$, the assumption gives $n^2 \leq cn$, so $n \leq c$. But we chose $n > c$. This is a contradiction, so we can conclude that $n^2$ is not $O(n)$ 


### Question 1.4:
Why is `x in my_list` $O(n)$ while `x in my_set` is $O(1)$ on average?

**Answer:** The difference comes in how the data structures are implemented. The `in` operator for a list checks the list iteratively, so it must traverse each value while `in` for a set in python uses hashing, so it can jump straight to the hash value.

---

## Task 2:

### Question 2.1
Give the worst-case $\Theta$ for each snippet below, with a one-line reason:

```{python}
def f(xs):                       # A
    t = 0
    for i in range(len(xs)):
        for j in range(i, len(xs)):
            t += xs[i] * xs[j]
    return t

def g(n):                        # B
    c, i = 0, 1
    while i < n:
        i *= 2; c += 1
    return c

def h(xs):                       # C
    seen = []
    for x in xs:
        if x not in seen:
            seen.append(x)
    return seen
```

**A:** To find the worst case, fix $n$, then ask which input of that size takes the longest. In A, `xs` is a list. We begin with an assignment (1 operation), then the outer loop runs `i` over `xs`. For each `i`, the inner loop runs `j` from `i` to $n-1$, so the loop body runs $n + (n-1) + \cdots + 2 + 1 = \frac{n(n+1)}{2}$ times in total. Nothing depends on the values in `xs`, so all inputs of the same size do the same work, and the best case equals the worst case. Within the loop body, we perform two indexes and an assignment. The `list` datatype in Python indexes in $O(1)$, so even in the worst case (`i, j` at the end of the list) indexing still takes one operation. So each run of the loop body takes 3 operations. Therefore

$$
\begin{aligned}
T(n) &= 3 \frac{n(n+1)}{2} + 1 \\
    &= \frac{3n^2 + 3n}{2} + 1 \\
\end{aligned}
$$

The $n^2$ term dominates, so the worst-case performance is $\Theta(n^2)$.

*In one line:* Every input of size $n$ runs the loop body $\frac{n(n+1)}{2}$ times, so the worst case is $\Theta(n^2)$.

**B:** In B, the only input is the integer `n`, so for a given `n` there is exactly one input, and the best case equals the worst case. The first line has 2 assignments. Then the loop checks whether `i < n`, and if so, doubles `i` and increments `c`. After $k$ passes, $i = 2^k$, so the loop stops at the first $k$ with $2^k \geq n$, which is $k = \lceil \log_2 n \rceil$ passes. In other words, each time `n` doubles, `i` doubles one more time, so the loop runs one more pass. The runtime therefore grows sublinearly: $T(n)/n$ shrinks as `n` grows. Each pass does a check and two assignments, and the loop ends with one final failing check, so $T(n) = 3\lceil \log_2 n \rceil + 3$.

*In one line:* `i` doubles each pass until it reaches `n`, so the loop runs $\lceil \log_2 n \rceil$ times, and the worst case is $\Theta(\log n)$.

**C:** In C, the input is a list `xs`. The check `x not in seen` is a hidden loop: list membership scans `seen` until it finds `x`. The worst case is when all elements of `xs` are distinct (in any order), because then `x` is never found, so every check scans all of `seen`, and `seen` grows by one each time. There is 1 assignment on line 1, and the for loop runs $n$ times. When the $k$-th element is checked, `seen` holds the $k-1$ elements before it, so the scans cost $0 + 1 + 2 + \cdots + (n-1) = \frac{n(n-1)}{2}$ comparisons in total, one comparison per element of `seen`. Each new `x` is also appended once, which adds $n$ operations. So $T(n) = \frac{n(n-1)}{2} + n + 1$, and the worst case is $\Theta(n^2)$.

*In one line:* If all elements are distinct, each `x not in seen` scans all of `seen`, which grows to $n-1$ elements, so the hidden loop inside `in` makes the code act like two nested loops, and the worst case is $\Theta(n^2)$.

### Question 2.2:
Write the best-case $T(n)$ and the worst-case $T(n)$ separately (which inputs give each?), then a $\Theta$ for each. Is "$h$ is $O(n^2)$ on every input" true? Is "$h$ is $\Omega(n^2)$ on every input" true?

* As defined in Question 2.1.C, the worst-case scenario is $T(n) = \frac{n(n-1)}{2} + n + 1$. However, the best-case scenario occurs when all values of `xs` are the same, because then `seen` never holds more than one element, so each scan is a single comparison. Counting the same way as the worst case: the first `x` scans an empty `seen` (0 comparisons) and is appended once, and each of the other $n-1$ checks makes 1 comparison and finds `x`. Therefore, the best-case $T(n) = (n-1) + 1 + 1 = n + 1$.

* The worst case is $\Theta(n^2)$, while the best case is $\Theta(n)$.

* "$h$ is $O(n^2)$ on every input" is true. $O$ is an upper bound, and every input takes at most as many steps as the worst case, which is at most $c \cdot n^2$ for all $n \geq n_0$. So every input is too.

* "$h$ is $\Omega(n^2)$ on every input" is false, because $\Omega$ is a lower bound, and the best-case input (all values the same) takes only $n + 1$ steps, which falls below $c \cdot n^2$ for any fixed $c > 0$ once $n$ is large enough.

---

## Task 3:

### Question 3.1
Say which case each "column" measures in `timing.py`. Then take the worst case as $T(n) = 2n+3$ and prove

* For the list, the worst case is `-1 in container`, since it's not found, and the entire list must be checked.

* For the list, the best case is `0 in container`, since it's the very first item checked.

* For the set and dict columns, `-1` is an ordinary lookup (the average case), not a worst case.

#### Lemma 3.1.1
*Scratch work (finding $c$):* we need $2 + \frac{3}{n} \leq c$, and $\frac{3}{n} \leq 3$ for $n \geq 1$, so $c = 5$ works.

**Proof.** We show $T(n) = O(n)$. Let $c = 5$ and $n_0 = 1$. For all $n \geq 1$, $3 \leq 3n$, so $T(n) = 2n + 3 \leq 2n + 3n = 5n$. So $T(n) \leq c \cdot n$ for all $n \geq n_0$, and by definition $T(n) = O(n)$. $\blacksquare$

#### Lemma 3.1.2
*Scratch work (finding $c$):* we need $c \leq 2 + \frac{3}{n}$, and $2 \leq 2 + \frac{3}{n}$ for every $n \geq 1$, so $c = 2$ works.

**Proof.** We show $T(n) = \Omega(n)$. Let $c = 2$ and $n_0 = 1$. For all $n \geq 1$, $2n \leq 2n + 3 = T(n)$, since $3 > 0$. So $T(n) \geq c \cdot n$ for all $n \geq n_0$, and by definition $T(n) = \Omega(n)$. $\blacksquare$

#### Proof 3.1.3
We show $T(n) = \Theta(n)$. By Lemma 3.1.1, $T(n) \leq 5n$ for all $n \geq 1$, and by Lemma 3.1.2, $2n \leq T(n)$ for all $n \geq 1$. Let $c_1 = 2$, $c_2 = 5$ and $n_0 = \max(1, 1) = 1$, so that both bounds hold. Then $c_1 n \leq T(n) \leq c_2 n$ for all $n \geq n_0$, and by definition $T(n) = \Theta(n)$. $\blacksquare$

### Question 3.2
Covered by Proof 1.3.

---

## Task 4:

### Question 4.1:
Given a list of integers, return `True` if any value appears at least twice, and `False` if every value is distinct. 
1. Write your approach and its big O.
    * Make a set called `seen` to track the seen integers
    * Loop through the input list
      * Within the loop, check if each item is in seen (O(1))
        * If seen, return `True`
        * If not seen, add the item to the list
    * Upon the loop's completion, return `False`

2. Note one alternative approach and its big O.
   * It would also be possible to sort the list and check if any pairs of adjacent indices are equal.

3. Which input of size $n$ is the worst case? Which is the best case?
   * The worst case is a completely distinct list
   * The best case is a list with two starting entries that are the same

4. What's the $\Theta$ of each case?
   * The worst case is $\Theta(n)$. Since `x in set` is O(1), there's only a single loop `n` times, and everything else is constant runtime.
   * The best case is actually $\Theta(1)$. In this case, the loop only goes through a single iteration, so it essentially acts as a single assignment.
