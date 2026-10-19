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


