import numpy
t=numpy.array([list(map(int, x)) for x in open("day08/input", "r").read()[:-1].split('\n')])
l,m,r=range(len(t)),lambda x:max(x,default=-1),0
for i in l:
    for j in l:
        if t[i,j]>min(m(t[i,:j]),m(t[i,j+1:]),m(t[:i,j]),m(t[i+1:,j])):r+=1
print(r)