# Telangana District Coloring using CSP

This project models the Telangana map coloring problem as a Constraint Satisfaction Problem.

---

## Problem Statement

The goal is to assign colors to all districts of Telangana such that:

- Each district receives exactly one color  
- No two adjacent districts have the same color  

---

## CSP Model

- **Variables**: Districts of Telangana  
- **Domain**: {Red, Green, Blue, Yellow}  
- **Constraints**: Adjacent districts must differ in color  

A backtracking algorithm is used to find a valid solution.

---

## District List

Adilabad, Bhadradri, Hyderabad, Jagtial, Jangaon, Jayashankar,  
Jogulamba, Kamareddy, Karimnagar, Khammam, Komaram Bheem,  
Mahabubabad, Mahabubnagar, Mancherial, Medak, Medchal,  
Mulugu, Nagarkurnool, Nalgonda, Narayanpet, Nirmal,  
Nizamabad, Peddapalli, Rajanna, Rangareddy, Sangareddy,  
Siddipet, Suryapet, Vikarabad, Wanaparthy, Warangal Rural,  
Warangal Urban, Yadadri  

---

## Notes

- Adjacency relationships are simplified  
- Multiple valid colorings are possible  
- Four colors are sufficient to solve the problem  

---

## Output

Displays a valid assignment of colors to districts.

---

## Concepts Used

- Constraint Satisfaction Problems  
- Backtracking Search  
- Graph representation  