# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

class Solution(object):
    def maxPoints(self, points):
        if len(points)<3: return len(points)
        retval,line_map=2,{}
        for i in xrange(len(points)-1):
            for j in xrange(i+1,len(points)):
                if points[i].x==points[j].x:
                    slope="x"+str(points[i].x)
                elif points[i].y==points[j].y:
                    slope="y"+str(points[i].y)
                else:
                    x,y=points[j].x-points[i].x,points[j].y-points[i].y
                    if x!=0 and y!=0:
                        g=gcd(x,y)
                        x,y=x/g,y/g
                    xx,yy=x,x*points[i].y-y*points[i].x
                    if xx!=0 and yy!=0:
                        g=gcd(xx,yy)
                        xx,yy=xx/g,yy/g
                    slope=",".join(map(str,[x,y,xx,yy]))
                if slope not in line_map:
                    line_map[slope]=set()
                line_map[slope].add((i,points[i].x,points[i].y))
                line_map[slope].add((j,points[j].x,points[j].y))
                retval=max(retval,len(line_map[slope]))
        return retval

print Solution().maxPoints([Point(0,0),Point(1,1),Point(2,2),Point(3,3)])