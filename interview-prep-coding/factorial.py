'''
Write a Python function that takes a positive integer n as input and returns its factorial.
'''

def factorial(n):
    if n < 0:
        return None
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Test the function
n = 5
result = factorial(n)
print(result)  # Output: 120