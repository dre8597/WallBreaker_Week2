"""
We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Return a list of all uncommon words.

You may return the list in any order.



Example 1:

Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]
Example 2:

Input: A = "apple apple", B = "banana"
Output: ["banana"]
"""
import collections


def uncommonFromSentences(A: str, B: str):
    together = collections.Counter(A.split())
    together.update(collections.Counter(B.split()))
    difference = []
    for i in together:
        if together[i] == 1:
            difference.append(i)
    return difference


print(uncommonFromSentences("fd kss fd"
                            , "fd fd kss"))
