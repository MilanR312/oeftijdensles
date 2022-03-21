import math

def lenc(a:int,b:int,c:int,d:int) -> float:
    return math.sqrt((a-b)**2 + (c-d)**2)

def calct(x1:int,y1:int,x2:int,y2:int,x3:int,y3:int) -> float:
    a = lenc(x1,x2,y1,y2)
    b = lenc(x1,x3,y1,y3)
    c = lenc(x3,x2,y3,y2)
    s = (a+b+c)/2
    opp = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return opp
print(calct(1,1,2,2,3,1))