import numpy
t=numpy.array([list(map(int, x)) for x in open("day08/input", "r").read()[:-1].split('\n')])
l,r=range(len(t)),[]
def f(a, n):
    s=0
    for i in a:
        s+=1
        if i>=n:return s
    return s
for i in l:
    for j in l:
        n=t[i,j]
        r.append(f(t[i,:j][::-1],n)*f(t[i,j+1:],n)*f(t[:i,j][::-1],n)*f(t[i+1:,j],n))
print(max(r))