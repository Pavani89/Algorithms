'''
write a python code to generate the fibonacci series
'''
# 0 1 1 2 3 5 8 13 21 34 55

def generate_fibonacci_series(num):
    series = [0, 1]  # Initialize the series with the first two terms

    while series[-1] + series[-2] <= num:
        next_term = series[-1] + series[-2]
        series.append(next_term)

    return series

# Test the function
num = 100
fib_series = generate_fibonacci_series(num)
print(fib_series)