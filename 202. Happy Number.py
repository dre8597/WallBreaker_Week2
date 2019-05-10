"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example:

Input: 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""


# TODO needs a check for duplicate
def isHappy(n: int) -> bool:
    running = 0
    seen = set()
    if set(str(n))==str(n):
        while n != 1:
            for i in set(str(n)):
                running += int(i) * int(i)
                n = running
                if n in seen:
                    return False
            seen.add(n)
            running = 0
        return True
    else:
        return False


print(isHappy(11))
