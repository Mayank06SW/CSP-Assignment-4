# Australia Map Coloring Problem (CSP)

This program solves the map coloring problem for Australia using a Constraint Satisfaction Problem approach.

---

## Problem Statement

Assign colors to the regions of Australia such that:

- Every region has one color  
- Adjacent regions must not share the same color  

Regions included:
WA, NT, QLD, SA, NSW, V, T  

---

## Methodology

The problem is modeled as a CSP with:

- **Variables**: Regions of Australia  
- **Domain**: {Red, Green, Blue}  
- **Constraints**: Neighboring regions cannot have identical colors  

Backtracking is used to explore valid assignments.

---

## Neighbor Relationships

Each region is connected to specific neighboring regions, and constraints are applied accordingly.

---

## Output

The program prints a valid coloring combination where all constraints are satisfied.

---

## Concepts Applied

- Backtracking  
- Constraint checking  
- Graph-based modeling  