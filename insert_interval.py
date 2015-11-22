class Solution(object):
    def insert(self, intervals, newInterval):
        retval=[]
        if len(intervals)==0: return [newInterval]
        for i in xrange(len(intervals)):
            if newInterval.start>intervals[i].end or newInterval.end<intervals[i].start:
                retval.append(intervals[i])
                continue
            newInterval.start=min(intervals[i].start,newInterval.start)
            newInterval.end=max(intervals[i].end,newInterval.end)
        retval.append(newInterval)
        return sorted(retval,key=lambda x:x.start)