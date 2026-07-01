x=int(input())
pre=None
op=""

while x!=-1:
    if pre!=None and pre>x:
        op="desc"
    if pre!=None and pre<x:
        op="asec"
    else:
        op="False"
    pre=x
    x=int(input())
print(op)
