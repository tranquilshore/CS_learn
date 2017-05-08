#Moore's Voting algorithm
#idea: cancel an element with other different element which would leave us an uncanelled majority element, next step is just to check if its the majority or not

def majorityCandidate(a, size):
    maj_index = 0
    count = 1
    for i in range(1,size):
        if a[maj_index] == a[i]:
            count += 1
        else:
            count -= 1
        if count == 0:
            maj_index = i
            count = 1
    return a[maj_index]

'''
O(n) time complexity
O(1) auxiliary space
'''