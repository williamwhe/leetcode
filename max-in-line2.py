import fractions

class Solution(object):
    def maxPoints(self, points):
        if len(points)<3: return len(points)
        retval,line_map=2,{}
        for i in xrange(len(points)-1):
            for j in xrange(i+1,len(points)):
                if points[i][0]==points[j][0]:
                    slope="x"+str(points[i][0])
                elif points[i][1]==points[j][1]:
                    slope="y"+str(points[i][1])
                else:
                    x,y=points[j][0]-points[i][0],points[j][1]-points[i][1]
                    if x!=0 and y!=0:
                        g=fractions.gcd(x,y)
                        x,y=x/g,y/g
                    xx,yy=x,x*points[i][1]-y*points[i][0]
                    if xx!=0 and yy!=0:
                        g=fractions.gcd(xx,yy)
                        xx,yy=xx/g,yy/g
                    slope=",".join(map(str,[x,y,xx,yy]))
                if slope not in line_map:
                    line_map[slope]=set()
                line_map[slope].add((i,points[i][0],points[i][1]))
                line_map[slope].add((j,points[j][0],points[j][1]))
                retval=max(retval,len(line_map[slope]))
        return retval

# print Solution().maxPoints([[0,-12],[5,2],[2,5],[0,-5],[1,5],[2,-2],[5,-4],[3,4],[-2,4],[-1,4],[0,-5],[0,-8],[-2,-1],[0,-11],[0,-9]])
def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

print gcd(1,2)
print gcd(2,-4)
print gcd(-6,12)