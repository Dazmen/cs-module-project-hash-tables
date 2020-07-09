import math
import random

# Your code here
fun_cache = {}

def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here
    if (x, y) not in fun_cache:
        fun_cache[(x, y)] = slowfun_too_slow(x, y)
    
    return fun_cache[(x, y)]



# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')

### Planning ###

# How to improve performance
## There is ~36 possible combinations with the random ranges given
## could build a cache that pre calculates those values, using the x, y combo as a key

### ---- Best Approach ----
## or we could store them in a cache as we see the x, y values passed in (like the fib example)
### ^^^^ Best approach ^^^^
##### Could further improve by caching aspects of the equation(such as the factorial numbers)
##### This could help improve performance if a greater number of ranges were selected

## Other option would be to create a cache for specific aspects of the function such as factorial. It would not be as performant as the first option but may be better from a programming point of view since we wouldnt be able to 
