# Sliding Puzzle Solver
![Gif](https://miro.medium.com/max/1400/1*W7jg4GmEjGBypd9WPktasQ.gif)
## Problem
Our task is to find an 8-puzzle solution. The puzzle consists of 8 numbered squares and one blank space. Fields can be moved up, down, left or right, but only if there is free space in that direction. There is always a starting and a target position and it is necessary to find a sequence of steps that lead from one position to another.

## Solved using:
### Heuristic Function
1. Number of fields that are not in place.
2. The sum of the distances of the individual fields from their target position.
3. A combination of previous estimates.
### Greedy Search Algorithm
**The greedy search algorithm** is an algorithmic strategy that makes the best optimal choice in each small phase in order to ultimately lead to a globally optimal solution.
The operation of the greedy search algorithm can be described by the **following steps**:
1. Create an initial node and put it among the created and not yet processed nodes.
2. If there is no node created and not yet processed, it will fail - there is no solution.
3. Select the most suitable node from the created and not yet processed, mark it current.
4. If this node represents the target state, finish process.
5. Create followers of the current node and put it among the processed nodes.
6. Sort followers and put it among created and not yet processed.
7. Go to step 2.
