from sys import maxsize

def createstack():
    stack = []
    return stack

def isempty(stack):
    return len(stack) == 0

def push(stack,item):
    stack.append(item)
    
def pop(stack):
    if isempty(stack):
        return str(-maxsize-1) #minus infinite
    return stack.pop()

'''
1. easy to implement. memory is saved
2. it is not dynamic. can not grow n shrink at runtime
'''