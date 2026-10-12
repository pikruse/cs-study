# Review: Proof Refresher
Goal: review proof techniques from this week without any external resources.

---

## Question 1:
In an ordinary induction proof of "for all $n \geq n_0, P(n)$, what exactly do you prove in the base case? In the inductive step, what do you assume and what do you prove?

**Answer:** In an ordinary induction proof, the base case is proving that the initial case $P(n_0)$ is true. In the inductive step, you then assume that $P(n)$ is true, and use that to prove $P(n+1)$.

## Question 2:
In the "all horses of the same color" proof, which sentence is false, and for which value of $k$?



## Question 3:
Write the predicate $P(n)$ for this claim: "every integer $n \geq 8$ can be written as $3a + 5b$ with $a, b$ being nonnegative integers.

**Answer:** The predicate $P(n)$ is $n = 3a+5b$, $a, b$ integers $\geq 0$.

## Question 4:
How does the inductive hypothesis in strong induction differ from the one in ordinary induction? Why does the product-of-primes proof need the strong version?

## Question 5:
Why is `x in some_list` $O(n)$, while `x in some_set` is $O(1)$ on average?