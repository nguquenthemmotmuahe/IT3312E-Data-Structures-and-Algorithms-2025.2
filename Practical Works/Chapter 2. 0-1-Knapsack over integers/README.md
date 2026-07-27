# Chapter 2. 0-1-Knapsack over integers

## Description
Given items $1, 2, \dots, n$. Item $i$ has weight $w_i$ and value $v_i$ ($i = 1, 2, \dots, n$). Given a capacity $B$, select a subset of $\{1, 2, \dots, n\}$ such that the total weight is less than or equal to $B$ and the total value is maximal.

## Input
* **Line 1:** Contains 2 positive integers $n$ and $B$ ($1 \le n \le 1000$, $1 \le B \le 10000$).
* **Line $i + 1$ ($i = 1, 2, \dots, n$):** Contains 2 positive integers $w_i$ and $v_i$ ($1 \le w_i, v_i \le 10000$).

## Output
Write the total value of the items selected.

## Example

**Input:**
> 5 10
> 3 10
> 1 8
> 6 6
> 2 3
> 1 4

**Output:**
> 25
