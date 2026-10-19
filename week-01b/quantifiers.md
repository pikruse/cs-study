# Week 1b: Quantifiers

## Task 1:
1. Write the following claims as $\forall n \geq \__, P(n)$, and write $P(n)$ in full with every variable introduced with a quantifier:
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

**Case Coverage.** Every integer $n$ can be written as $n=2k+r$, where $k$ is an integer and $r = 0$ or $1$ by the quotient-remainder theorem (QRT). If $r=0$, then $n$ is even, and if $r=1$, then $n$ is odd. So all integers $n$ must be even or odd.

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

---

## Task 3:

### Proof 3.1
Prove that for every integer $n$, $n^2$ leaves a remainder of 0 or 1 when divided by 3.

**Claim.** For every integer $n$, $n^2$ leaves a remainder of 0 or 1 when divided by 3. That is, $\forall n \in \mathbb{Z}$, $\exists k \in \mathbb{Z}$ such that $n^2 = 3k+0$ or $n^2 = 3k+1$.

**Cases.** There are 3 cases we will consider: $n$ divided by 3 has a remainder of 0, 1, or 2. Since all integers $n$ leave a remainder of either 0, 1, or 2 when divided by 3 by the QRT, these cases cover all integers $n$.

**Case 1.** Suppose $n$ leaves a remainder of 0 when divided by 3, so $n = 3q$ for some integer $q$. So

$$
\begin{aligned}
n^2 &= (3q)^2 \\
  &= 9q^2 \\
  &=3(3q^2). \\ 
\end{aligned}
$$

Let $3q^2 = k$. Since $q$ is an integer, then $k$ is also an integer. So, $\exists k \in \mathbb{Z}$ such that $n^2 = 3k$, and case 1 is true.

**Case 2.** Suppose $n$ leaves a remainder of 1 when divided by 3, so $n = 3q + 1$ for some integer $q$. So
$$
\begin{aligned}
n^2 &= (3q+1)^2 \\
  &= 9q^2 + 6q + 1 \\
  &= (9q^2 + 6q) + 1 \\
  &= 3(3q^2 + 2q) + 1. \\
\end{aligned}
$$ 

Let $3q^2 + 2q = k$. Since $q$ is an integer, $k$ is also an integer. So $\exists k \in \mathbb{Z}$ such that $n^2 = 3k + 1$, and case 2 is true.

**Case 3.** Suppose $n$ leaves a remainder of 2 when divided by 3, so $n = 3q + 2$ for some integer $q$. So
$$
\begin{aligned}
n^2 &= (3q + 2)^2 \\
  &= 9q^2 + 12q + 4 \\
  & = 9q^2 + 12q + 3 + 1 \\
  &= (9q^2 + 12q + 3) + 1 \\
  &= 3(3q^2 + 4q + 1) + 1. \\
\end{aligned}
$$

Let $3q^2 + 4q + 1 = k$. Since $q$ is an integer, $k$ is also an integer. So $\exists k \in \mathbb{Z}$ such that $n^2 = 3k + 1$, and case 3 is true.

**Conclusion.** Since all 3 cases are true, $\forall n \in \mathbb{Z}$, $\exists k \in \mathbb{Z}$ such that $n^2 = 3k+0$ or $n^2 = 3k+1$. Therefore $\forall n \in \mathbb{Z}$, $n^2$ leaves a remainder of 0 or 1 when divided by 3. $\blacksquare$  

### Corollary 3.2
No integer of the form $3m+2$ is a perfect square.

Suppose, for contradiction, that $N=3m+2$ is a perfect square for some integer $m$, so $N = n^2$ for some integer $n$. By Proof 3.1, $n^2 = 3k + r$ for some integer $k$ and some $r \in \{0, 1\}$. So $N$ leaves a remainder of 2 and also remainder $r \neq 2$ when divided by 3. This is a contradiction because remainders are unique based on the QRT, so we can conclude that no integer of the form $3m+2$ is a perfect square. $\blacksquare$

---

## Task 4:
Prove that $\sqrt 2$ is irrational.

### Lemma 4.1
For every integer $a$, if $a^2$ is even, then $a$ is even. We will prove the contrapositive: if $a$ is not even, then $a^2$ is not even. By the QRT, every integer is either even or odd, and not both, so "not even" means "odd." So we must show that if $a$ is odd, then $a^2$ is odd.

Assume $a$ is odd. That means $\exists k \in \mathbb{Z}$ such that $a = 2k+1$. So 

$$
\begin{aligned} 
a^2 &= (2k+1)^2 \\
  &= 4k^2 + 4k + 1 \\
  &= (4k^2 + 4k) + 1 \\
  &= 2(2k^2 + 2k) + 1. \\
\end{aligned}
$$

Let $p = 2k^2 + 2k$. Since $k$ is an integer, $p$ is also an integer. So $\exists p \in \mathbb{Z}$ such that $a^2 = 2p + 1$, so $a^2$ is odd by the definition of odd. So when $a$ is odd, $a^2$ is also odd. Taking the contrapositive of this statement, we know that if $a^2$ is even, then $a$ is also even. $\blacksquare$

### Proof 4.2
We will prove that $\sqrt 2$ is irrational by contradiction. Assume $\sqrt 2$ is rational. That is, $\exists a,b \in \mathbb{Z}$, with $b \neq 0$, such that $\sqrt 2 = \frac{a}{b}$, and the fraction is in lowest terms (any fraction can be reduced to lowest terms), so $a$ and $b$ share no common factor. So

$$
\begin{aligned}
\sqrt 2 &= \frac{a}{b} \\
2 &= (\frac{a}{b})^2 \\
2 &= \frac{a^2}{b^2}\\
2b^2 &= a^2.\\ 
\end{aligned}
$$

Let $p = b^2$. Since $b$ is an integer, $p$ is also an integer. So $a^2 = 2p$ for some integer $p$. By definition, $a^2$ is even. By Lemma 4.1, since $a^2$ is even, $a$ is also even. So $a = 2k$ for some integer $k$. Substituting $a = 2k$ into $2b^2 = a^2$ yields

$$
\begin{aligned}
2b^2 &= (2k)^2 \\
2b^2 &= 4k^2 \\
b^2 &= 2k^2. \\
\end{aligned}
$$

Let $q = k^2$. Since $k$ is an integer, $q$ is also an integer. So $b^2 = 2q$ for some integer $q$. By definition, $b^2$ is even. By Lemma 4.1, since $b^2$ is even, $b$ is also even. Since $a$ and $b$ are both even, they share a common factor of 2. Therefore, $\frac{a}{b}$ is not in lowest terms. This is a contradiction, since we assumed that the fraction was in lowest terms. Therefore, we can conclude that $\sqrt 2$ is irrational. $\blacksquare$

---

## Task 5

### Proof 5.1
**Claim.** For all $n \geq 0$, $0 + 1 + \dots + n = \frac{n(n+1)}{2}$.

**Predicate.** $P(n)$: $0 + 1 + \dots + n = \frac{n(n+1)}{2}$.

**Base Case.** For $n = 0$, the left side is $0$ and the right side is $\frac{0(0+1)}{2} = 0$, so $P(0)$ holds.

**Inductive Hypothesis.** Assume $P(n)$ holds for some arbitrary $n \geq 0$. We will prove $P(n+1)$:

$$
\begin{aligned}
0 + 1 + \dots + n + (n + 1) &= \frac{(n+1)((n+1)+1)}{2}.
\end{aligned}
$$

**Inductive Step.** Adding $(n+1)$ to both sides of $P(n)$ yields:

$$
\begin{aligned}
0 + 1 + \dots + n + (n + 1) &= \frac{n(n+1)}{2} + (n+1)\\
  & = \frac{n^2 + n}{2} + \frac{2n + 2}{2} \\
  &= \frac{n^2 + 3n + 2}{2} \\
  &= \frac{(n+1)(n+2)}{2} \\
  &= \frac{(n+1)((n+1)+1)}{2}. \\
\end{aligned}
$$

So, $P(n+1)$ is true.

**Conclusion.** Since $P(0)$ holds and $P(n) \Rightarrow P(n+1)$ for all $n \geq 0$, $0 + 1 + \dots + n = \frac{n(n+1)}{2}$ for all $n \geq 0$ by induction. $\blacksquare$

### Corollary 5.2
Let $A = \{0, 1, \dots, n\}$, and let $S$ be $A$ with some entry $m$ removed. Then $\frac{n(n+1)}{2} - \sum_{x \in S} x = m$.

Since $S$ is $A$ with $m$ removed, $\sum_{x \in S} x = \sum_{x \in A} x - m$. From Proof 5.1, we know $\sum_{x \in A} x = 0 + 1 + \dots + n = \frac{n(n+1)}{2}$ for all $n \geq 0$. So $\sum_{x \in S} x = \frac{n(n+1)}{2} - m$. Then, by algebra, $\frac{n(n+1)}{2} - \sum_{x \in S} x = m$. $\blacksquare$

---

## Task 6
We will prove $n^3 - n$ is divisible by 3 for every integer $n$ by cases. That is, for every $n$, $\exists$ a $k \in \mathbb{Z}$ such that $n^3 - n = 3k$. We will consider 3 cases: $n = 3p$, $n=3p+1$, and $n=3p+2$ for some integer $p$. By the quotient remainder theorem, we know that all integers $n$ must fall into one of these cases.

**Case 1.** Let $n=3p$ for some integer $p$. Then 
$$
\begin{aligned}
n^3 - n &= (3p)^3 - (3p) \\
  &= 27p^3 - 3p \\
  &= 3(9p^3 - p).
\end{aligned}
$$

Let $9p^3 - p = k$. Since $p$ is an integer, $k$ is also an integer. So $n^3-n=3k$, and case 1 is true.

**Case 2.** Let $n = 3p+1$ for some integer $p$. Then
$$
\begin{aligned}
n^3 - n &= (3p+1)^3 - (3p+1)\\
  &= (3p)^3 + 3(3p)^2 + 3(3p) + 1 - 3p - 1 \\
  &= 27p^3 + 27p^2 + 9p + 1 - 3p -1 \\
  &=27p^3 + 27p^2 + 6p \\
  &=3(9p^3 + 9p^2 + 2p). \\
\end{aligned}
$$

Let $9p^3 + 9p^2 + 2p = k$. Since $p$ is an integer, $k$ is also an integer. So $n^3-n=3k$, and case 2 is true. 

**Case 3.** Let $n = 3p + 2$ for some integer $p$. Then
$$
\begin{aligned}
n^3 - n &= (3p+2)^3 - (3p+2) \\
  &= (3p)^3 + 3((3p)^2(2)) + 3(3p(2^2)) + 8 - 3p - 2 \\
  &= 27p^3 + 54p^2 + 36p + 8 - 3p - 2 \\
  &= 27p^3 + 54p^2 + 33p + 6 \\
  &= 3(9p^3 + 18p^2 + 11p + 2). \\
\end{aligned}
$$

Let $9p^3 + 18p^2 + 11p + 2 = k$. Since $p$ is an integer, $k$ is also an integer. So $n^3-n=3k$, and case 3 is true. 

Since $n^3-n=3k$ for some integer $k$ in all cases, $n^3 - n$ is divisible by 3 for every integer $n$. $\blacksquare$ 