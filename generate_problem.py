import json
import os
import random
from datetime import date

PROBLEMS_FILE = "used_problems.json"
SOLUTIONS_DIR = "solutions"

PROBLEMS = [
    {"slug": "factorial", "title": "Factorial of a number",
     "code": '''def factorial(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    print(factorial(5))  # 120
'''},
    {"slug": "fibonacci", "title": "Nth Fibonacci number",
     "code": '''def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

if __name__ == "__main__":
    print(fibonacci(10))  # 55
'''},
    {"slug": "is_prime", "title": "Check if a number is prime",
     "code": '''def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    print(is_prime(29))  # True
'''},
    {"slug": "palindrome", "title": "Check if a string is a palindrome",
     "code": '''def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

if __name__ == "__main__":
    print(is_palindrome("A man a plan a canal Panama"))  # True
'''},
    {"slug": "reverse_string", "title": "Reverse a string",
     "code": '''def reverse_string(s):
    return s[::-1]

if __name__ == "__main__":
    print(reverse_string("hello"))  # olleh
'''},
    {"slug": "bubble_sort", "title": "Bubble sort an array",
     "code": '''def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

if __name__ == "__main__":
    print(bubble_sort([5, 2, 9, 1, 5, 6]))
'''},
    {"slug": "binary_search", "title": "Binary search in sorted array",
     "code": '''def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

if __name__ == "__main__":
    print(binary_search([1, 3, 5, 7, 9, 11], 7))  # 3
'''},
    {"slug": "gcd", "title": "Greatest common divisor",
     "code": '''def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    print(gcd(48, 18))  # 6
'''},
    {"slug": "count_vowels", "title": "Count vowels in a string",
     "code": '''def count_vowels(s):
    return sum(1 for ch in s.lower() if ch in "aeiou")

if __name__ == "__main__":
    print(count_vowels("Hello World"))  # 3
'''},
    {"slug": "max_subarray", "title": "Maximum subarray sum (Kadane's algorithm)",
     "code": '''def max_subarray(arr):
    max_sum = curr_sum = arr[0]
    for num in arr[1:]:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)
    return max_sum

if __name__ == "__main__":
    print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
'''},
    {"slug": "anagram_check", "title": "Check if two strings are anagrams",
     "code": '''def is_anagram(a, b):
    return sorted(a.replace(" ", "").lower()) == sorted(b.replace(" ", "").lower())

if __name__ == "__main__":
    print(is_anagram("listen", "silent"))  # True
'''},
    {"slug": "linked_list_reverse", "title": "Reverse a singly linked list",
     "code": '''class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    prev = None
    while head:
        nxt = head.next
        head.next = prev
        prev = head
        head = nxt
    return prev

if __name__ == "__main__":
    head = Node(1, Node(2, Node(3)))
    new_head = reverse_list(head)
    out = []
    while new_head:
        out.append(new_head.val)
        new_head = new_head.next
    print(out)  # [3, 2, 1]
'''},
    {"slug": "two_sum", "title": "Two Sum",
     "code": '''def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
'''},
    {"slug": "power_of_two", "title": "Check if a number is a power of two",
     "code": '''def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

if __name__ == "__main__":
    print(is_power_of_two(64))  # True
'''},
    {"slug": "merge_sorted_arrays", "title": "Merge two sorted arrays",
     "code": '''def merge_sorted(a, b):
    result = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i]); i += 1
        else:
            result.append(b[j]); j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result

if __name__ == "__main__":
    print(merge_sorted([1, 3, 5], [2, 4, 6]))
'''},
]


def load_used():
    if os.path.exists(PROBLEMS_FILE):
        with open(PROBLEMS_FILE) as f:
            return json.load(f)
    return []


def save_used(used):
    with open(PROBLEMS_FILE, "w") as f:
        json.dump(used, f, indent=2)


def main():
    used = load_used()
    available = [p for p in PROBLEMS if p["slug"] not in used]

    if not available:
        used = []
        available = PROBLEMS

    problem = random.choice(available)
    used.append(problem["slug"])
    save_used(used)

    os.makedirs(SOLUTIONS_DIR, exist_ok=True)
    filename = f"{SOLUTIONS_DIR}/{date.today()}_{problem['slug']}.py"
    with open(filename, "w") as f:
        f.write(f'"""\n{problem["title"]}\nAuto-generated daily practice solution.\n"""\n\n')
        f.write(problem["code"])

    print(f"Generated: {filename}")


if __name__ == "__main__":
    main()
