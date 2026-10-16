# Review: Writing proofs: quantifiers, predicates, cases, contradiction

## Question 1:
Negate this statement, moving the "not" all the way inside: "For every $\varepsilon > 0$, there exists $N$ such that for all $n \geq N$, $\mid a_n \mid < \varepsilon$."

**Answer:** There exists an $\varepsilon > 0$ such that $\forall N$, $\exists n \geq N$ such that $\mid a_n \mid \geq \varepsilon$.

## Question 2:
What's wrong with this predicate: $P(n)$: for all $n \geq 1$, $1+2+ \dots + n = \frac{n(n+1)}{2}$. Rewrite $P(n)$ and the full claim correctly.

**Answer:** The predicate includes "for all $n \geq 1$." This belongs in the claim. The correct rewrite is:

*Claim.* For all $n \geq 1$, $1+2+ \dots + n = \frac{n(n+1)}{2}$.

*Predicate.* $P(n)$: $1+2+ \dots + n = \frac{n(n+1)}{2}$.

## Question 3:
To prove $n^3 - n$ is divisible by 3 for every integer n by cases, which cases do you use, and why do they cover each integer?

**Answer:** To prove this, we must consider all of the cases that $n$ falls into by the quotient remainder theorem: $\exists k \in \mathbb{Z}$ such that $n = 3k+0$, $n=3k+1$, or $n=3k+2$.

## Question 4:
Why does "every integer $n \geq 2$ is a product of primes" need *strong* induction rather than ordinary induction?

**Answer:** If $k+1$ is composite, $k+1 = a \cdot b$ with $2 \leq a, b \leq k$. So you need both $P(a)$ and $P(b)$, which can be any values below $k+1$, not just $P(k)$.

## Question 5:
In the inductive step for $1 + \dots + n = n(n+1)/2$, state exactly what you assume and exactly what you prove.

**Answer:** In the inductive step, we assume $P(n): 1 + \dots + n = \frac{n(n+1)}{2}$ for some arbitrary $n \geq 1$, and we prove $P(n+1): 1 + \dots + n + (n+1) = \frac{(n+1)(n+2)}{2}$.