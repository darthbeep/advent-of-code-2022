i=open("day06/input", "r").read()[:-1]
r=[x for x in range(14,len(i)) if len(set(i[x-14:x]))==14][0]
print(r)