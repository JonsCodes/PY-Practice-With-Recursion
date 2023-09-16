def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Test
print(fibonacci_recursive(4))  # Output: 3
print(fibonacci_recursive(2))  # Output: 1
