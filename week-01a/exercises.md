# Week 1a: Proof refresher

## Task 1: Find the broken step

Given this broken induction proof, find the step that fails, and explain why.

> **Claim:** In any group of $n \geq 1$ horses, all the horses are the same color.
>
> **Base case ($n = 1$):** A group of one horse is trivially all one color.
>
> **Inductive step:** Assume every group of $k$ horses is all one color. Take a group of $k + 1$ horses. Remove the first horse, and the remaining $k$ horses are all one color. Put it back and remove the last horse instead, and those $k$ horses are also all one color. The two groups overlap, so all $k + 1$ horses must be the same color.

### Answer

The proof is false because $P(1)$ does not imply $P(2)$. A single horse being one color does not imply a group of two horses being one color.

Examining $P(2)$, we have a set of two horses. These horses could be two different colors, according to the proof setup; removing the first horse would lead to a set with horses of all one color, and removing the last horse would do the same, since the sets share no horse. Therefore, the inductive step does not hold.

---

## Task 2: Sum of squares

**Claim.** For every integer $n \geq 1$,

$$
1^2 + 2^2 + \cdots + n^2 = \frac{n(n+1)(2n+1)}{6}.
$$

### Proof (ordinary induction)

**Predicate.** Let $P(n)$ be the statement

$$
1^2 + 2^2 + \cdots + n^2 = \frac{n(n+1)(2n+1)}{6}.
$$

**Base case, $P(1)$.**

$$
1^2 = 1 = \frac{1 \cdot 2 \cdot 3}{6},
$$

so $P(1)$ holds.

**Inductive hypothesis.** Assume $P(n)$ holds for some $n \geq 1$:

$$
1^2 + 2^2 + \cdots + n^2 = \frac{n(n+1)(2n+1)}{6}.
$$

**Inductive step, $P(n) \Rightarrow P(n+1)$.** We want to show

$$
1^2 + 2^2 + \cdots + n^2 + (n+1)^2 = \frac{(n+1)(n+2)(2n+3)}{6}.
$$

Add $(n+1)^2$ to both sides of the inductive hypothesis, then simplify the right side:

$$
\begin{aligned}
1^2 + 2^2 + \cdots + n^2 + (n+1)^2
  &= \frac{n(n+1)(2n+1)}{6} + (n+1)^2 \\
  &= \frac{2n^3 + 3n^2 + n}{6} + \frac{6n^2 + 12n + 6}{6} \\
  &= \frac{2n^3 + 9n^2 + 13n + 6}{6} \\
  &= \frac{(n+1)(n+2)(2n+3)}{6}.
\end{aligned}
$$

The last line holds because

$$
(n+1)(n+2)(2n+3) = (n^2 + 3n + 2)(2n + 3) = 2n^3 + 9n^2 + 13n + 6.
$$

This is exactly $P(n+1)$.

**Conclusion.** $P(1)$ holds, and $P(n) \Rightarrow P(n+1)$ for every $n \geq 1$. By induction, $P(n)$ holds for all integers $n \geq 1$. $\blacksquare$

---
## Task 3: Postage combinations

**Claim.** Using 3¢ and 7¢ stamps, every postage cost $n \geq 12$ can be paid exactly.

### Proof (ordinary induction)

**Predicate.** Let $P(n)$ be the statement: there exist integers $a, b \geq 0$ such that

$$
n = 7a + 3b.
$$

**Base case, $P(12)$.** $12 = 7 \cdot 0 + 3 \cdot 4$, so $P(12)$ holds with $a = 0$ and $b = 4$.

**Inductive hypothesis.** Assume $P(n)$ holds for some $n \geq 12$, so

$$
n = 7a + 3b
$$

for some integers $a, b \geq 0$.

**Inductive step, $P(n) \Rightarrow P(n+1)$.** We want to show that

$$
n + 1 = 7c + 3d
$$

for some integers $c, d \geq 0$. Since $b$ is a nonnegative integer, either $b \geq 2$ or $b \leq 1$, so there are two cases.

*Case 1: $b \geq 2$.* Trade two 3¢ stamps for one 7¢ stamp:

$$
n + 1 = 7(a + 1) + 3(b - 2).
$$

Let $c = a + 1$ and $d = b - 2$. Since $a \geq 0$, $c \geq 1$, and since $b \geq 2$, $d \geq 0$. So $P(n+1)$ holds.

*Case 2: $b \leq 1$.* Trade two 7¢ stamps for five 3¢ stamps:

$$
n + 1 = 7(a - 2) + 3(b + 5).
$$

Let $c = a - 2$ and $d = b + 5$. Since $b \geq 0$, $d \geq 5$. It remains to show that $c \geq 0$, that is, $a \geq 2$. Since $b \leq 1$, we have $3b \leq 3$, and $n \geq 12$ by the inductive hypothesis. Therefore

$$
\begin{aligned}
7a &= n - 3b \\
   &\geq 12 - 3 \\
   &= 9,
\end{aligned}
$$

so $a \geq \frac{9}{7} > 1$. Since $a$ is an integer, $a \geq 2$, and so $c \geq 0$. So $P(n+1)$ holds.

In either case, $P(n+1)$ holds.

**Conclusion.** $P(12)$ holds, and $P(n) \Rightarrow P(n+1)$ for every $n \geq 12$. By induction, $P(n)$ holds for all integers $n \geq 12$. $\blacksquare$

---

## Review: Proof Refresher
Goal: review proof techniques from this week without any external resources.

### Question 1:
In an ordinary induction proof of "for all $n \geq n_0, P(n)$, what exactly do you prove in the base case? In the inductive step, what do you assume and what do you prove?

**Answer:** In an ordinary induction proof, the base case is proving that the initial case $P(n_0)$ is true. In the inductive step, you then assume that $P(n)$ is true, and use that to prove $P(n+1)$.

### Question 2:
In the "all horses of the same color" proof, which sentence is false, and for which value of $k$?

**Answer:** The sentence, "the two groups overlap, so all $k + 1$ horses must be the same color." is false for $k=1$, because at $k=1$, the groups don't overlap.


### Question 3:
Write the predicate $P(n)$ for this claim: "every integer $n \geq 8$ can be written as $3a + 5b$ with $a, b$ being nonnegative integers.

**Answer:** The predicate $P(n)$ is that $\exists$ integers $a,b \geq 0$ such that $n = 3a+5b$.

### Question 4:
How does the inductive hypothesis in strong induction differ from the one in ordinary induction? Why does the product-of-primes proof need the strong version?

**Answer:** The inductive hypothesis is based on some or all previous values less than $n$ in addition to $n$. In the product-of-primes proof, if $k+1$ isn't prime, then $k+1 = a \cdot b$ with $2 \leq a, b \leq k$. So we need $P(a)$ and $P(b)$, which the strong hypothesis provides and the oridinary (only $P(k)$) does not.

### Question 5:
Why is `x in some_list` $O(n)$, while `x in some_set` is $O(1)$ on average?

**Answer:** Lists do not use hashing, while sets do. Therefore, you need to go through a list sequentially, but a set allows you to find the exact location of an item