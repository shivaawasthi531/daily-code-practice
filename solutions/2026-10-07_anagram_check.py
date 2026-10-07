"""
Check if two strings are anagrams
Auto-generated daily practice solution.
"""

def is_anagram(a, b):
    return sorted(a.replace(" ", "").lower()) == sorted(b.replace(" ", "").lower())

if __name__ == "__main__":
    print(is_anagram("listen", "silent"))  # True
