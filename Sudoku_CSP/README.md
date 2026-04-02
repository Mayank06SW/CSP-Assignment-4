# Sudoku Solver using CSP

This program solves a standard 9×9 Sudoku puzzle using a Constraint Satisfaction approach.

---

## Problem Statement

Fill the Sudoku grid such that:

- Each row contains numbers from 1 to 9 without repetition  
- Each column contains numbers from 1 to 9 without repetition  
- Each 3×3 box contains numbers from 1 to 9 without repetition  

---

## CSP Representation

- **Variables**: Empty cells in the grid  
- **Domain**: Numbers from 1 to 9  
- **Constraints**:
  - Row uniqueness  
  - Column uniqueness  
  - Subgrid uniqueness  

---

## Approach

The algorithm uses backtracking:

1. Find an empty cell  
2. Try placing a number  
3. Check if it satisfies constraints  
4. Continue recursively  

---

## Output

Prints the completed Sudoku grid.

---

## Concepts Used

- Backtracking  
- Recursive search  
- Constraint validation  