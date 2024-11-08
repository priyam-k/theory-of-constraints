# theory-of-constraints

Theory of Constraints Visualizer/Simulator
by Priyam K.

requested by @sanrav2016

---
![Visualiser start position, 1 full bowl and 6 empty ones](https://github.com/priyam-k/theory-of-constraints/blob/0d953a44d137fa67eab8e2255a365a1301e6a96a/images/start.png "Start position of visualiser")

### A basic visualizer to demonstrate the Theory of Constraints, and how bottlenecks can form when processes work at different rates and rely on the outputs of other processes.
This visualizer shows 6 processes, each depending on the one before. The initial process draws from an infinite reservoir of materials (RP), and the processes continue until the final process (FG). Each "day", a dice is rolled, representing the amount of units each step will process, working from the final step back to the initial. Each step has its number of units (represented by matchsticks in a bowl) shown above it, and can only process up to however many units the previous step has. Ex: M3 can process up to 5 units, but M2 only has 3 units available, so M3 only processes 3 units. This project aims to show how bottlenecking (shown below) can affect the efficiency of a chain of processes, and how a single ineffient process can slow down the entire chain.


![Bottlenecking example](https://github.com/priyam-k/theory-of-constraints/blob/0d953a44d137fa67eab8e2255a365a1301e6a96a/images/bottlenecking.png "Bottlenecking example")


### Controls:
- Right arrow: go to the next step
- Left arrow: go to the previous step
