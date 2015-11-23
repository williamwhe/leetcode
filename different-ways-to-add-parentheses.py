class Solution(object):
    def diffWaysToCompute(self, input):
        if input.isdigit():
            return [int(input)]
        tmp=[]
        for i in xrange(len(input)):
            if input[i] not in "+-*":
                continue
            left=self.diffWaysToCompute(input[:i])
            right=self.diffWaysToCompute(input[i+1:])
            if input[i]=="+":
                for l in left:
                    for r in right:
                        tmp.append(l+r)
            elif input[i]=="-":
                for l in left:
                    for r in right:
                        tmp.append(l-r)
            elif input[i]=="*":
                for l in left:
                    for r in right:
                        tmp.append(l*r)
        return tmp

print Solution().diffWaysToCompute("2*3-4*5")