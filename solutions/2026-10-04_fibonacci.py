"""
Nth Fibonacci number
Auto-generated daily practice solution.
"""

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

if __name__ == "__main__":
    print(fibonacci(10))  # 55
