class conversion:
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        self.array = []
        self.output = []
        self.precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
        
    def isempty(self):
        return True if self.top == -1 else False
    
    def peek(self):
        return self.array[-1]
    
    def pop(self):
        if not self.isempty():
            self.top -= -1
            return self.array.pop()
        else:
            return "$"
        
    def push(self, op):
        self.top += 1
        self.array.append(op)
        
    def isoperand(self,ch):
        return ch.isalpha()
    
    def notgreater(self,i):
        try:
            a = self.precedence[i]
            b = self.precedence[self.peek()]
            return True if a <= b else False
        except KeyError:
            return False
        
    def infixtopostfix(self, exp):
        for i in exp:
            if self.isoperand(i):
                self.output.append(i)
            elif i == '(':
                self.push(i)
            elif i == ')':
                while (not self.isempty()) and self.peek() != '(':
                    a = self.pop()
                    self.output.append(a)
                if not self.isempty() and self.peek() != '(':
                    return -1
                else:
                    self.pop()
            
            else:
                while not self.isempty() and self.notgreater(i):
                    self.output.append(self.pop())
                self.push(i)
        
        #popping all the operator from the stack
        while not self.isEmpty():
            self.output.append(self.pop())
            