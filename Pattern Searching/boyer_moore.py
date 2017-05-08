'''
Boyer moore is a combination of two approaches:
1. Bad character heuristic: character comparison in right to left order to skip pointless alignments.

rule1: skip alignments untill
1) mismatch becomes a match
2) or pattern moves past mismatched character

*** it tries to turn a mismatch into a match

it takes O(n/m) time in the best case and O(mn) time in worst case


2. good suffix heuristic
rule2: skip untill:
1) there are no mismatches between pattern and substring matched by inner loop
2) or pattern moves past that substring

*** tries to keep the match as match and doesn't have them turn into mismatch

'''

