#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) This first problem is not a function and there is nothing happening recursively, so the runtime of this snippet of code is linear to the mutation of a. The while conditional breaks whenever `a >= n^3`. The value is then constantly checked in linear time as we mutate a with `a + n^2.` Although factorials are implemented in this code, this does not change our linear runtime complexity of `o(n)`

b) This second problem includes a for loop with a specific range defined by n. Inside this for loop we are defining a variable j inside the scope and creating a conditional loop for j against the value of n. Mutating then j and sum until the condition breaks. What this code is doing is creating a loop for every element of i in the range of n, which runs at linear time so `o(n)` for the first loop and `o(n)` for the second one. This makes the total runtime = `o(n^2)`

o(n logn)

c)

## Exercise II

We could devise a strategy by first declaring what some of our possible variables are:

curr = current floor
low = lowest floor
high = highest floor

We could now maybe try a divide and conquer strategy where

curr = n/2
low = 0
high = n
breakable = []
not_breakable = []

now we have split the n-story building into two halves
we can now check if the egg will break.

if the egg breaks:
add floor to breakable
change the high to now be current floor
change current floor to halfway (curr + low)/2

if the egg doesn't break:
add floor to not_breakable
change the low to now be at the current floor
change the current floor to now be (curr + high)/2

The runtime complexity of this proposed algorithm would be linear unless we were using a data structure that could be traversed at faster than constant time.

There would be two checks and loops inside of those checks.
Therefore the runtime complexity would be o(logn)
