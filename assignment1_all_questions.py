
# Assignment: Applied Generative AI - Assignment 1 (Coding Part)
# Author: Miguel Morales mam2670
# Questions 1 to 6 - Solved with Python

import math

# ----------------------------
# Question 1: Independent Events
# ----------------------------

P_A = 0.4
P_B = 0.3
P_A_and_B = P_A * P_B
P_A_or_B = P_A + P_B - P_A_and_B

print("Q1 (a): P(A ∩ B) =", P_A_and_B)  # 0.12
print("Q1 (b): P(A ∪ B) =", P_A_or_B)   # 0.58

# ----------------------------
# Question 2: Check Independence
# ----------------------------

P_A = 0.5
P_B = 0.4
P_A_given_B = 0.7

are_independent = P_A_given_B == P_A
print("Q2: Are A and B independent?", are_independent)

if are_independent:
    print(f"Yes, because P(A|B) = {P_A_given_B} is equal to P(A) = {P_A}.")
else:
    print(f"No, because P(A|B) = {P_A_given_B} is NOT equal to P(A) = {P_A}.")

# ----------------------------
# Question 3: Bayes' Rule
# ----------------------------

P_A = 0.6
P_B_given_A = 0.5
P_B_given_not_A = 0.2
P_not_A = 1 - P_A
P_B = (P_B_given_A * P_A) + (P_B_given_not_A * P_not_A)
P_A_given_B = (P_B_given_A * P_A) / P_B

print(f"Q3: P(B) = {P_B:.4f}")
print(f"Q3: P(A|B) = {P_A_given_B:.4f}")

# ----------------------------
# Question 4: Medical Test (Bayes)
# ----------------------------

P_D = 0.02
P_not_D = 1 - P_D
P_Pos_given_D = 0.95
P_Neg_given_not_D = 0.90
P_Pos_given_not_D = 1 - P_Neg_given_not_D
P_Pos = (P_Pos_given_D * P_D) + (P_Pos_given_not_D * P_not_D)
P_D_given_Pos = (P_Pos_given_D * P_D) / P_Pos

print(f"Q4: P(Pos) = {P_Pos:.4f}")
print(f"Q4: P(D|Pos) = {P_D_given_Pos:.4f}")

# ----------------------------
# Question 5: Expected Value, Variance, Sample Mean
# ----------------------------

x_values = [85, 90, 95, 100]
p_values = [0.375, 0.375, 0.125, 0.125]

# (a) Expected Value
expected_value = sum(x * p for x, p in zip(x_values, p_values))
print(f"Q5 (a): Expected value E[X] = {expected_value}")

# (b) Variance
expected_x2 = sum(x**2 * p for x, p in zip(x_values, p_values))
variance = expected_x2 - expected_value**2
print(f"Q5 (b): E[X^2] = {expected_x2}")
print(f"Q5 (b): Variance Var(X) = {variance}")

# (c) Sample Mean
sample = [85, 90, 85, 95, 90, 85, 100, 90]
sample_mean = sum(sample) / len(sample)
print(f"Q5 (c): Sample mean = {sample_mean}")
print(f"Q5 (c): Expected value (from part a) = {expected_value}")

# ----------------------------
# Question 6: Entropy
# ----------------------------

probs = [0.4, 0.3, 0.2, 0.1]
entropy = -sum(p * math.log2(p) for p in probs)
print(f"Q6 (a): Entropy H(X) = {entropy:.4f} bits")

equal_probs = [0.25, 0.25, 0.25, 0.25]
max_entropy = -sum(p * math.log2(p) for p in equal_probs)
print(f"Q6 (b): New entropy with equal probabilities = {max_entropy:.4f} bits")
