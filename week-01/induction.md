# Task
Given this broken induction proof, find the step that fails, and explain why:

> **Claim:** in any group of n >= 1 horses, all the horses are the same color.
> **Base Case (n = 1):** a group of one horse is trivially all one color
> **Inductive step:** Assume every group of k horses is all one color. Take a group of k + 1 horses. Remove the first horse, and the remaining k horses are all one color. Put it back and remove the last horse instead, and those k horses are also all one color. The two groups overlap, so all k + horses must be the same color.

# Answer
The proof is false because P(1) does not imply P(2). A single horse being one color does not imply a group of two horses being one color. Therefore, the proof is incorrect.