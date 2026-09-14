"""
Check if a number is a power of two
Auto-generated daily practice solution.
"""

def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

if __name__ == "__main__":
    print(is_power_of_two(64))  # True
