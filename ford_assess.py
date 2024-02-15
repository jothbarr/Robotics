#10:15 to 11:05, without checking out and checking in steps
class Circle():
    def __init__(self, xpos,ypos,radius):
        self.xpos=xpos
        self.ypos=ypos
        self.radius=radius
    
    def __str__(self):
        return f"'\t X: {self.xpos} Y: {self.ypos} Radius: {self.radius} \n'"

    def isInside(self,x,y):
        d = ((x-self.xpos)**2+((y-self.ypos))**2)**0.5
        if self.radius==0:
            return 2
        elif d>self.radius:
            return 0
        elif d<=self.radius:
            return 1
    
    def translateReturnCode(self,ans):
        return (f'{ans}')
    
if __name__=='__main__':

    for (x,y,r) in [(1,1,1),(-2,1,0.5),(3,-1,5),(-4,-2,0)]:
        c=Circle(x,y,r)
        print('\n')
        print(c)
        for (x1,y1) in [(0.5,0.25),(5,2),(-1,2),(.25,1.35),(-1,6),(-2,2)]:
            ans=c.isInside(x1,y1)
            temp=c.translateReturnCode(ans)
            print(f'{temp},{x1},{y1}')