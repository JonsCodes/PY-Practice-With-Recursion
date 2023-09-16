# Write code for algorithm 3 below

def fibonacci(n):
    if n < 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)
    # Test the function
    print(fibonacci(5)) # Output: 2
    print(fibonacci(2)) # Output: 1