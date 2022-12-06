i=open("day06/input", "r").read()[:-1]
r=[x for x in range(4,len(i)) if len(set(i[x-4:x]))==4][0]
print(r)