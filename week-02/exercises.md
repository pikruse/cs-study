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

The Big-O of this function is $O(n^2)$. First, we define $T(n)$. There's one variable assignment outside the loop (1). The inner loop runs $n-i$ times for each $i$, so the body runs $n + (n-1) + \cdots + 1 = n(n+1)/2$ times, giving $T(n) = \frac{n(n+1)}{2)+1. The $n^2$ term dominates as $n \rightarrow \infty$, so the function is $O(n^2)$.


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

To find the worst case, we must ask if $n$ is fixed, then which input of that size takes the longest?

**A:**  

**B:** 

**C:** 

### Question 2.2:
Write the best-case $T(n)$ and the worst-case $T(n)$ separately (which inputs give each?), then a $\Theta$ for each. Is "$h$ is $O(n^2) on every input" true? Is "$h$ is $\Omega(n^2)$ on every input" true?

---

## Task 3: 

### Question 3.1
Say which case each "column" measures in `membership.py`. Then take the worst case as $T(n) = 2n+3$ and prove

#### Lemma 3.1.1
$T(n) = O(n)$: there exist $c > 0$ and $n_0$ such that $T(n) \leq c \cdot n$ for all $n \geq n_0$

#### Lemma 3.1.2
$T(n) = \Omega(n)$ (Lower bound)

#### Proof 3.1.3 
$T(n) = \Theta(n)$ (Tight bound)

### Question 3.2:
Prove that $n^2$ is not $O(n)$ by contradiction.

### Question