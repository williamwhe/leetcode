class Solution:
    # @return a boolean
    def isValid(self, s):
    	stack = []
    	for ch in s:
    		if ch == '{' or ch == '(' or ch == '[':
    			stack.append(ch)
    		elif ch == '}' and (len(stack) > 0 and stack[-1] == '{'):
    			stack.pop()
    		elif ch == ')' and (len(stack) > 0 and stack[-1] == '('):
    			stack.pop()
    		elif ch == ']' and (len(stack) > 0 and stack[-1] == '['):
    			stack.pop()
    		else:
    			return False
    	if len(stack) == 0:
    		return True
    	return False

s = Solution()
print s.isValid("()[]{}")
print s.isValid("([)]")
print s.isValid("]")
print s.isValid("{")