import copy,collections,time

class Solution(object):
    def removeInvalidParentheses(self, s):
        if len(s)==0: return [""]
        if self.isValid(s): return [s]
        self.retval,self.invalid=set(),set()
        self.bfs([s])
        if len(self.retval)==0: return [""]
        return list(self.retval)

    def isValid(self, s):
        if len(s)==0: return False
        if s.count("(")==0 and s.count(")")==0: return True
        if s.count("(")!=s.count(")"): return False
        stack=[]
        for i in xrange(len(s)):
            if len(stack)>len(s)-i: return False
            if s[i]!='(' and s[i]!=')': continue
            if s[i]=='(':
                stack.append('(')
                continue
            if s[i]==')':
                if len(stack)==0: return False
                stack.pop()
        return False if len(stack)>0 else True

    def bfs(self, candidate):
        while len(candidate)>0:
            tmp=[]
            for s in candidate:
                for i in xrange(len(s)):
                    subs=s[:i]+s[i+1:]
                    if self.isValid(subs): self.retval.add(subs)
                    elif subs not in self.invalid:
                        tmp.append(subs)
                        self.invalid.add(subs)
            if len(self.retval)>0: return
            candidate=copy.deepcopy(tmp)

a=time.time()
print Solution().removeInvalidParentheses("((z(((fp))()((((((g(")
# print Solution().removeInvalidParentheses(")))())((p((())a(())(")
# print Solution().removeInvalidParentheses("())(())(")
# print Solution().removeInvalidParentheses("()())()")
# print Solution().removeInvalidParentheses("p(r)")
# print Solution().removeInvalidParentheses("(a)())()")
# print Solution().removeInvalidParentheses("v)z())(((")
# print Solution().removeInvalidParentheses(")(f")
# print Solution().removeInvalidParentheses("n")
# print Solution().removeInvalidParentheses("()")
print time.time()-a