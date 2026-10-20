# Week 1c: Strong induction

**Idea:** Ordinary induction proves $P(k+1)$ from $P(k)$ alone. Sometimes induction needs an earlier case, like $P(k-2)$. Strong induction assumes all cases instead of just $P(k)$.

**Template:**
1. Prove the base case(s).
2. Fix $k \geq$ (last base case)
3. Assume $P(m)$ for every $m$ with (first base case) $\leq m \leq k$
4. Prove $P(k+1)$
5. Conclude: for all $n \geq$ base, $P(n)$.

---

## Example 1:
$P(n)$: there exist integers $a, b \geq 0$ with $n = 7a + 3b$. Claim: for all $n \geq 12$, $P(n)$.
* Base cases: $12 = 7 \cdot 0 + 3 \cdot 4$, $13 = 7 \cdot 1 + 3 \cdot 2$, $14 = 7 \cdot 2 + 3 \cdot 0$.
* Step: fix $k \geq 14$ and assume $P(m)$ for every $12 \leq m \leq k$. Since $12 \leq k - 2 \leq k$, $P(k-2)$ gives integers $a, b \geq 0$ with $k - 2 = 7a + 3b$. Then $k+1 = 7a + 3(b+1)$, and $b+1 \geq 0$. So $P(k+1)$.

The proof needs 3 base cases because the step for $k+1$ uses $P(k-2)$, the case three below $k+1$. If we only proved 12 and 13, we wouldn't have information to prove 14, because it relies on information from 11, which isn't part of the claim. Therefore, we must prove all of these values to ensure the pattern holds.

--- 

## Task 2:
### Proof 2.1
All postage values $n \geq 12$ can be made from a combination of 3c and 7c stamps. 

**Predicate.** $P(n)$: $\exists$ integers $a,b \geq 0$ such that $n = 3a + 7b$.

**Base Cases.** $P(12)$: $12 = 3 \cdot 4 + 7 \cdot 0$. $P(13)$: $13 = 3 \cdot 2 + 7 \cdot 1$. $P(14)$: $14 = 3 \cdot 0 + 7 \cdot 2$.

**Inductive Hypothesis.** Fix an integer $k \geq 14$, and assume $P(m)$ for every $12 \leq m \leq k$. 

**Inductive Step.** We must show that $k+1 = 3a'+ 7b'$ for some integers $a', b' \geq 0$. Since $k \geq 14$, we know that $k-2 \geq 12$, and $k-2 \leq k$. So $k-2$ is covered by the strong inductive hypothesis. So we know $P(k-2)$: $k-2 = 3a + 7b$ for some integers $a,b \geq 0$. By adding one 3-cent stamp, we know that

$$
\begin{aligned}
k-2+3 &= 3a + 7b + 3 \\
k+1 &= 3a + 7b + 3 \\
k+1 &= 3(a+1) + 7b \\
\end{aligned}
$$

Let $a' = a+1$ and $b' = b$. These are integers with $a' \geq 1 \geq 0$ and $b' \geq 0$, and $k+1 = 3a' + 7b'$, so $P(k+1)$ holds. Since $P(12)$, $P(13)$, and $P(14)$ hold, and $P(k+1)$ follows for every $k \geq 14$, $P(n)$ is true for all integers $n \geq 12$ by strong induction. $\blacksquare$

### Analysis 2.2:
The amounts $1 \leq n < 12$ that can't be made from 7s and 3s are 1, 2, 4, 5, 8, and 11. This doesn't contradict the claim because we specify that it holds only for $n \geq 12$. 

--- 

## Task 3:
Every integer $n \geq 2$ is a product of primes. That is, $n = p_1 \cdot p_2 \cdot \dots \cdot p_r$ for some $r \geq 1$ and primes $p_1, \dots p_r$. A prime on its own counts, with $r=1$.

**Predicate.** $P(n): n = p_1 \cdot \dots \cdot p_r$ for some $r \geq 1$ and primes $p_1, \dots, p_r$.

**Base Case.** $P(2):$ 2 is prime. So, by definition of a prime, the base case is true. 

**Inductive Hypothesis.** We fix $k \geq 2$ and assume $P(m)$ for every $m$ where $2 \leq m \leq k$.

**Inductive Step.** We will prove 2 cases: $k+1$ is prime, and $k+1$ is not prime. By definition, a number must be either prime or not prime (composite). So these cases cover all possibilities for $k+1$.

*Case 1.* Let $k+1$ be prime. Then, by definition of a prime, $k+1$ is a product of a prime with $r=1$. So case 1 is true.

*Case 2.* Let $k+1$ be composite. So $k+1=a \cdot b$ for some integers $a, b$ with $1 < a < k+1$ and $1 < b < k+1$. Since $a,b$ are integers and $1 < a$, $1 < b$, we know that $2 \leq a$ and $2 \leq b$. Additionally, since $a < k+1$ and $b < k+1$, we know $a \leq k$ and $b \leq k$. So $2 \leq a \leq k$ and $2 \leq b \leq k$. Then, by the inductive hypothesis, we know that $a$ and $b$ are products of primes. That is, $a = p_1 \cdot \dots \cdot p_r$ for some $r \geq 1$ and primes $p_1, \dots, p_r$, and $b = q_1 \cdot \dots \cdot q_t$ for some $t \geq 1$ and primes $q_1, \dots, q_t$. So
$$
\begin{aligned}
a \cdot b &= (p_1 \cdot \dots \cdot p_r) \cdot (q_1 \cdot \dots \cdot q_t) \\
    &= p_1 \cdot \dots \cdot p_r \cdot q_1 \cdot \dots \cdot q_t. \\ 
\end{aligned}
$$

This is a product of $r + t \geq 1$ primes. Since $k+1 = a \cdot b$, $k+1$ is also a product of primes.

Therefore, $k+1$ is a product of primes when $k+1$ is composite, and case 2 is true. So, if $P(m)$ holds for every $2 \leq m \leq k$, then $P(k+1)$ holds.

**Conclusion.** Since $P(2)$ holds, and $P(2), \dots, P(k)$ together imply $P(k+1)$ for every $k \geq 2$, every integer $n \geq 2$ is a product of primes by strong induction. $\blacksquare$

---

## Task 4:
Every integer $n \geq 8$ can be written as $n=3a+5b$ for some integers $a,b \geq 0$.

**Predicate.** $P(n): n = 3a+5b$ for some integers $a,b \geq 0$.

**Base Cases.**
*Case 1.* $P(8): 8 = 3 \cdot 1 + 5 \cdot 1$.

*Case 2.* $P(9): 9 = 3 \cdot 3 + 5 \cdot 0$.

*Case 3.* $P(10): 10 = 3 \cdot 0 + 5 \cdot 2$.

**Inductive Hypothesis.** Fix $k \geq 10$. Then for an integer $m$, where $8 \leq m \leq k$, $P(m)$ is true.

**Inductive Step.** We begin with $P(k-2)$. Since $k \geq 10$, we know $8 \leq k-2 \leq k$. So, by the inductive hypothesis, we know

$$
\begin{aligned}
k-2 &= 3a + 5b \\
k-2+3 &= 3a + 5b + 3\\
k+1 &= 3(a+1) + 5b \\
\end{aligned}
$$

Let $a' = a+1$ and $b' = b$. Since $a, b \geq 0$, $a', b'$ also $\geq 0$. So $k+1 = 3a' + 5b'$. Therefore, $P(k+1)$ is true.

**Conclusion.** So, by strong induction, we know there exist $a,b \geq 0$ such that $\forall n \geq 8$, $n = 3a+5b$. $\blacksquare$

---

## Task 5:
Fibonacci numbers: $F(0) = 0, F(1) = 1$, and $F(n) = F(n-1) + F(n-2)$ for $n \geq 2$. For every integer $n \geq 0$, $F(n) < 2^n$.

We will prove that $\forall n \in \mathbb{Z^+}$, $F(n) < 2^n$. 

**Predicate** $P(n)$: $F(n) < 2^n$.

**Base Cases.** $P(0)$: $F(0) = 0 < 2^0 = 1$, and $P(1)$: $F(1) = 1 < 2^1 = 2$.

**Inductive Hypothesis.** Fix $k \geq 1$. Then for every integer $m$ where $0 \leq m \leq k$, we assume $P(m)$ is true.

**Inductive Step.** Since $k \geq 1$, we know $k-1 \geq 0$. So $0 \leq k-1 \leq k$. By definition, we know $F(k+1) = F(k) + F(k-1)$, since $k+1 \geq 2$. So

$$
\begin{aligned}
F(k+1) &= F(k) + F(k-1) && \text{by the definition of } F\\
    &< 2^{k} + 2^{k-1} && \text{by the strong inductive hypothesis } P(k) \text{ and } P(k-1)\\
    &= 2 \cdot 2^{k-1} + 2^{k-1} \\
    &= (2+1)2^{k-1} \\
    &= 3 \cdot 2^{k-1} \\
    &< 4 \cdot 2^{k-1} \\
    &= 2 \cdot 2 \cdot 2^{k-1} \\
    &= 2^{k+1}.
\end{aligned}
$$

So $F(k+1) < 2^{k+1}$, and $P(k+1)$ is true.

**Conclusion.** Therefore, $\forall$ integers $n$, $F(n) < 2^n$. $\blacksquare$



