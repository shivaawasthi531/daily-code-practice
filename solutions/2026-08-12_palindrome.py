"""
Check if a string is a palindrome
Auto-generated daily practice solution.
"""

def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

if __name__ == "__main__":
    print(is_palindrome("A man a plan a canal Panama"))  # True
