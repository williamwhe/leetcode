class MinStack:
    def __init__(self):
        self.ms = []
        
    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.ms.append(x)

    # @return nothing
    def pop(self):
        self.ms.pop()

    # @return an integer
    def top(self):
        return self.ms[-1]

    # @return an integer
    def getMin(self):
        return min(self.ms)

ms = MinStack()
ms.push(-3)
print ms.getMin()