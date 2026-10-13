# Quantifiers
---
## Task 1:
1. Write the following claims as $\forall n \geq __, P(n)$, and write $P(n)$ in full with every variable introduced with a quantifier:
   * Every integer $n \geq 12$ can be paid exactly with 3c and 7c stamps. 
     * **rewrite:** $\forall$ integers $n \geq 12$, $\exists$ some integers $a,b \geq 0$ such that $n = 3a + 7b$.
     * **claim:** $\forall n \geq 12, P(n)$.
   * Every integer $n \geq 2$ is a product of primes. 
     * **rewrite**: $\forall$ integers $n \geq 2$, $\exists$ some primes $p_1, ..., p_t$, $t \geq 1$, such that $n = p_1 \cdot p_2 \cdots p_t$.
     * **claim:** $\forall n \geq 2, P(n)$.

2. TwoSum's guarantee is written as the following claim: "for every list of integers and every target, there exist two different positions whose values sum to the target."
   * Negate the claim
     * "There exist a list of integers and a target such that no two different positions sum to the target."
   * Decide whether the original claim is true. If it's not, give a counterexample.
     * The claim is not true. with list `[0, 0]` and target `1`, $0 + 0 \neq 1$.
    
3. What quantifier is TwoSum searching for, and why can it stop at the first match?
   * two sum is searching for an existential quantifier, $\exists$. It can stop once it finds a single example, because it knows that a single true case exists, and proving all cases (as in $\forall$) is not required.