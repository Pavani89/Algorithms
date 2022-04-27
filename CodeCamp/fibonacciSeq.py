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
