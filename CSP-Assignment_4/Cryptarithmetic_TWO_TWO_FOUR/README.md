# Cryptarithmetic Puzzle (TWO + TWO = FOUR)

This project solves a classic cryptarithmetic puzzle using Constraint Satisfaction techniques.

---

## Problem Statement

Find digits for letters such that:

  T W O  
+ T W O  
--------  
F O U R  

The equation must hold true numerically.

---

## CSP Model

- **Variables**: T, W, O, F, U, R  
- **Domain**: {0–9}  
- **Constraints**:
  - Each letter has a unique digit  
  - Leading digits cannot be zero  
  - Arithmetic equation must be valid  

---

## Approach

- Generate permutations of digits  
- Assign digits to letters  
- Check constraints  
- Stop when a valid solution is found  

---

## Output

Displays the correct numerical substitution satisfying the equation.

---

## Concepts Used

- CSP formulation  
- Backtracking / brute-force search  
- Permutation generation  