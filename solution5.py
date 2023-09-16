# Write code for algorithm 5 below

def is_palindrome(s):
    s = s.lower()
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return is_palindrome(s[1:-1])
    
# Test the function
print(is_palindrome('Deleveled'))
print(is_palindrome('Delevveled'))