# Write code for algorithm 2 below

def print_natural_numbers(n):
    if n < 1:
        return  # Stop recursion when n is less than 1
    print_natural_numbers(n - 1)
    print(n)

# Test the function
print_natural_numbers(5)
# Output: 1 2 3 4 5