# Week 1: Proof refresher

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

## Task 4: Product of Primes

**Claim:** Every integer $n \geq 2$ is a product of primes. A prime on its own counts as a product of one prime.

### Proof (strong induction)

**Predicate:** Let $P(n)$ be the claim that every integer $n$ is a product of primes. That is, $n$ is the product of $p$ primes:

$$
n = p_1 \cdot p_2 \cdots p_r
$$

for some $r \geq 1$ and primes $p_1, ..., p_r$.

**Base Case P(2):** We will show that 2 is a product of primes. Assume $n = 2$ is not prime. Then, 2 can be written as $2 = a \cdot b$, with $1 < a < 2$ and $1 < b < 2$ and $a, b \in \mathbb{Z}$. However, there are no integers between $1$ and $2$, so $2$ cannot be written this way. Therefore, $n=2$ must be prime. So 2 is a product of one prime, and $P(2)$ holds.

**Strong Inductive Hypothesis:** Fix some $k \geq 2$, and assume that $P(m)$ holds for every $m$ with $2 \leq m \leq k$. $m$ is the product of primes:

$$
m = p_1 \cdot p_2 \cdots p_r
$$

for some $r \geq 1$ and primes $p_1, ..., p_r$. 
