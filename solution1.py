# Write code for algorithm 1 below

def print_numbers(n):
    if n < 0:
        return  # Stop recursion when n is negative
    print(n)
    print_numbers(n - 1)

# Test the function
print_numbers(5)
