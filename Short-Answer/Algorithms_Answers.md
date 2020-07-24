#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
This function is O(n) (or linear), because for the value of n is the number of times the loop will run.

b)
This function is logn, because the second the variable j is being doubled every time it goes through the while loop.

c)
This function is O(n) or linear, because the value of n will determine how many times the function will call itself.

* not positive about this one

## Exercise II

building:
    stories = n
    egg_crack_floor = n >= f
    egg_not_cracked_floor = n < f

want to determine what floor f is equal to.

my plan:  I would use the binary search method.  

step1: This means I will test if an egg breaks when dropped from the middle floor first.  If it does, then I know that every floor above the middle floor is not the egg cracking floor.  If it does not break then I know that the middle floor and every floor below it is not egg cracking floor.

step2: Based on my first drop I will then find the middle floor of all of the floors that I have not yet eliminated. For example, if the egg cracked in the middle, the next floor I test from would be the floor directly in the middle of the middle floor and the bottom floor.

step3: Continue eliminating half of the floors until the floor I'm looking for has been found.

bigO runtime for solution:   O(logn)