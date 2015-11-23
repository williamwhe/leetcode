class Solution(object):
    def calculate(self, s):
        s=s.replace(" ", "")
        retval=0
        stack=[]
        op=''
        for i in xrange(len(s)):
            if s[i]<='9' and s[i]>='0':
                a=int(stack.pop())
                if op=='+':
                    a+=int(s[i])
                elif op=='-':
                    a-=int(s[i])
                stack.append(str(a))
                op=''
            elif s[i]=='+':
                op='+'
            elif s[i]=='-':
                op='-'
            elif s[i]=='(':
                stack.append(s[i])
            elif s[i]==')':
                pass
        return retval
        
s=Solution()
print s.calculate("1 + 1")
print s.calculate(" 2-1 + 2 ")
print s.calculate("(1+(4+5+2)-3)+(6+8)")