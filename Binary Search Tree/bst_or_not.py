import sys

MAX = sys.maxint
MIN = -sys.maxint - 1

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key
        
