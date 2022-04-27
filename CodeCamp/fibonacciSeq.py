'''
Fibonacci Sequence using recursion
'''
'''
# Python program to display the Fibonacci sequence
def fibonacci(n):
   if n <= 1:
       return n
   else:
       return(fibonacci(n-1) + fibonacci(n-2))

'''
'''
# Fibonacci sequence using cache or memoization
def fibonacci(n):
    cache = {0: 0, 1: 1}
    if n in cache:  # Base case
        return cache[n]

    # Compute and cache the Fibonacci number
    cache[n] = fibonacci(n - 1) + fibonacci(n - 2)  # Recursive case
    return cache[n]

# Main
item = 10
print("Fibonacci sequence:")
for i in range(item):
    print(fibonacci(i))
'''


# Fibonacci generator using py genertor code

def fibonacci(num):
    a, b = 0, 1
    for i in range(0, num):
        yield "{}: {}".format(i + 1,
                              a)  # Use generators to display the list; yeild is the keywprd to identify generators
        a, b = b, a + b


for item in fibonacci(10):
    print(item)
