class Solution(object):
    def delList(self, prerequisites, prev):
        retval=[]
        for p in prerequisites:
            if p[1]==prev:
                del p
                continue
            retval.append(p[1])
        return retval
    
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        prevs=range(numCourses)
        all=range(numCourses)
        for p in prerequisites:
            next=p[0]
            prevs.remove(next)
        while len(prevs)>0:
            curr=prevs.pop();
            all.remove(curr)
            prevs=self.delList(prerequisites, curr)
        return True
    
s=Solution()
print s.canFinish(3, [])
print s.canFinish(2, [[1,0]])
print s.canFinish(2, [[1,0],[0,1]])