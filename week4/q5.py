# predict the output

l=[]
l.append(1)
l.append(2)
l.append(3)
print(l)
x=[]
print(len(x))
x.append(l)
print(x)
print(len(x),"len(x)")
print(len(x[0]),"len(x[0])")
m=[4,5,6]
x.append(m)
print(x) 
t=[]
t.append(x)
t.append([100,200,300])
print(t)
print(t[0])
print(t[1])

#answer  [1, 2, 3]
#0
#[[1, 2, 3]]
#1 len(x)
#3 len(x[0])
#[[1, 2, 3], [4, 5, 6]]
#[[[1, 2, 3], [4, 5, 6]], [100, 200, 300]]
#[[1, 2, 3], [4, 5, 6]]
#[100, 200, 300]