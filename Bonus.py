def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# Test the function


print(gcd(12, 8))  # Output: 4
