import re,itertools

class Solution(object):
    def diffWaysToCompute(self, instr):
        nums=re.split('[\+\-\*]',instr)
        ops=re.split('\d+',instr)
        ops=ops[1:-1]
        print nums, ops
        retval=[]
        for it in itertools.permutations(range(0,len(ops)),len(ops)):
            print it
            stack=[]
            for j in it:
                if ops[j]=="+":
                    if nums[j]!="s" and nums[j+1]!="s":
                        stack.append(int(nums[j])+int(nums[j+1]))
                        nums[j]=nums[j+1]="s"
                elif ops[j]=="-":
                    if nums[j]!="s" and nums[j+1]!="s":
                        stack.append(int(nums[j])-int(nums[j+1]))
                        nums[j]=nums[j+1]="s"
                elif ops[j]=="*":
                    if nums[j]!="s" and nums[j+1]!="s":
                        stack.append(int(nums[j])*int(nums[j+1]))
                        nums[j]=nums[j+1]="s"
            retval.append(stack[0])
        return retval
        
s=Solution()
print s.diffWaysToCompute("2*3-4*5")