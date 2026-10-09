# Task 1:
Given this broken induction proof, find the step that fails, and explain why:

> **Claim:** in any group of n >= 1 horses, all the horses are the same color.
> **Base Case (n = 1):** a group of one horse is trivially all one color
> **Inductive step:** Assume every group of k horses is all one color. Take a group of k + 1 horses. Remove the first horse, and the remaining k horses are all one color. Put it back and remove the last horse instead, and those k horses are also all one color. The two groups overlap, so all k + horses must be the same color.

## Answer
The proof is false because P(1) does not imply P(2). A single horse being one color does not imply a group of two horses being one color. Therefore, the proof is incorrect.

# Task 2:
Prove by ordinary induction that for every integer $n \leq 1$, $1^2 + 2^2 + \cdots + n^2 = \frac{n(n+1)(2n+1)}{6}$.

1. **The predicate $P(n)$**: we will prove $n \leq 1$, $1^2 + 2^2 + \cdots + n^2 = \frac{n(n+1)(2n+1)}{6}$ by induction.

2. **The base case $P(0)$**: first, we will prove the base case. $0^2 = \frac{0(0+1)(0+1)}{6} = 0$. So, the base case holds.

3. **The inductive hypothesis $P(n) \rightarrow P(n+1)$**: Assume $P(n)$ holds. That is, $n \leq 1$, $1^2 + 2^2 + \cdots n^2 = \frac{n(n+1)(2n+1)}{6}$. Then, we will prove $n \leq 1$, $1^2 + 2^2 + \cdots + n^2 + (n+1)^2 = \frac{(n+1)(n+2)(2n+3)}{6}$, showing that $P(n)$ implies $P(n+1)$.

4. **The inductive step**: We begin with $n \leq 1$, $1^2 + 2^2 + \cdots n^2 = \frac{n(n+1)(2n+1)}{6}$. Adding $(n+1)^2$ to both sides satisfies the right side of $P(n+1)$: $n \leq 1$, $1^2 + 2^2 + \cdots + n^2 + (n+1)^2 = \frac{(n)(n+1)(2n+1)}{6} + (n+1)^2$. Then with algebra, we transform the right side: $\frac{2n^3 + 3n^2+ n}{6} + (n+1)^2 = \frac{2n^3 + 3n^2+ n}{6} + \frac{6n^2 + 12n + 6}{6} = \frac{2n^3 + 9n^2 + 13n + 6}{6} = \frac{n(n+1)(2n+3)}{6}$. Therefore, $P(n)$ implies $P(n+1)$. So, we know $n \leq 1$, $1^2 + 2^2 + \cdots n^2 = \frac{n(n+1)(2n+1)}{6} \forall n \in N$ from induction.