# Quantifiers
---
## Task 1:
1. Write the following claims as $\forall n \geq __, P(n)$, and write $P(n)$ in full with every variable introduced with a quantifier:
   * Every integer $n \geq 12$ can be paid exactly with 3c and 7c stamps. 
     * **rewrite:** $\forall$ integers $n \geq 12$, $\exists$ some integers $a,b \geq 0$ such that $n = 3a + 7b$.
     * **claim:** $\forall n \geq 12, P(n)$.
   * Every integer $n \geq 2$ is a product of primes. 
     * **rewrite**: $\forall$ integers $n \geq 2$, $\exists$ some integer $t \geq 1$ and primes $p_1, ..., p_t$, such that $n = p_1 \cdot p_2 \cdots p_t$.
     * **claim:** $\forall n \geq 2, P(n)$.

2. TwoSum's guarantee is written as the following claim: "for every list of integers and every target, there exist two different positions whose values sum to the target."
   * Negate the claim
     * "There exist a list of integers and a target such that no two different positions sum to the target."
   * Decide whether the original claim is true. If it's not, give a counterexample.
     * The claim is not true. with list `[0, 0]` and target `1`, $0 + 0 \neq 1$.
    
3. What quantifier is TwoSum searching for, and why can it stop at the first match?
   * two sum is searching for an existential quantifier, $\exists$. It can stop once it finds a single example, because it knows that a single true case exists, and proving all cases (as in $\forall$) is not required.

---

## Task 2:
For every integer $n$, $n^2 + n$ is even.

**Definitions.** $n$ is even means there exists some integer $k$ such that $n = 2k$. $n$ is odd means there exists some integer $k$ such that $n = 2k+1$.

**Case Coverage.** Every integer $n$ can be written as $n=2k+r$, where $k$ is an integer and $r = 0$ or $1$ (by the quotient-remainder theorem). If $r=0$, then $n$ is even, and if $r=1$, then $n$ is odd. So all integers $n$ must be even or odd.

**Case 1: n is even.** Assume $n$ is even. Then there exists some integer $k$ such that $n=2k$. So
$$
\begin{aligned}
n^2 + n &= (2k)^2 + 2k \\
  &= 4k^2 + 2k \\
  &= 2(2k^2 + k).\\
\end{aligned}
$$
Let $q = 2k^2 + k$. Since $k$ is some integer, then $q$ must also be an integer. So, there exists an integer $q$ such that $n^2+n = 2q$. Therefore, when $n$ is even, $n^2+n$ is also even.

**Case 2: n is odd.** Assume $n$ is odd. Then there exists some integer $k$ such that $n = 2k+1$. So
$$
\begin{aligned}
n^2 + n &= (2k+1)^2 + 2k+1 \\
  &= 4k^2 + 4k + 1 + 2k +1 \\
  &= 4k^2 + 6k + 2\\
  &= 2(2k^2 + 3k + 1).\\
\end{aligned}
$$

Let $q = (2k^2 + 3k + 1)$. Since $k$ is an integer, $q$ must also be an integer. So, there exists an integer $q$ such that $n^2+n = 2q$. Therefore when $n$ is odd, $n^2+n$ is even. 

**Conclusion.** In both cases, $n^2+n$ is even. Therefore, for all integers $n$, $n^2+n$ is even. $\blacksquare$