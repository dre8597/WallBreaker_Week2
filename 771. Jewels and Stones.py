"""
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3
Example 2:

Input: J = "z", S = "ZZ"
Output: 0
"""


# Runtime of 48ms and O(n^2)
def numJewelsInStones_unoptimized(J: str, S: str) -> int:
    count = 0
    for i in J:  # O(n)
        for k in S:  # O(n)
            if i == k:
                count += 1
    return count


# Runtime of 40ms and O(n)
def numJewelsInStones_optimized(J: str, S: str) -> int:
    jewels = set(J)  # O(1) operations
    count = 0
    for i in S:  # O(n) operation
        if i in jewels:
            count += 1
    return count
