class Solution(object):
    def __init__(self):
        self.perfect=[]
        for i in range(1,46341):
            self.perfect.append(i*i)
        
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
    
s=Solution()
print s.numSquares(12)
print s.numSquares(13)