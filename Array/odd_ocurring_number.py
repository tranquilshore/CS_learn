#XOR of all elements gives us odd occurring element.
def getOddOccurrence(arr):
    res = 0
    for i in arr:
        res = res^i
    return res
'''
time complexity : O(n)
space complexity : O(1)
'''