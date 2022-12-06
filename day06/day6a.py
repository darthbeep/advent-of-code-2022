i = [x for x in ((open("day06/input", "r")).read()[:-1])]
r=[x+4 for x in range(len(i)-4) if len(set(i[x:x+4]))==len(i[x:x+4])][0]
print(r)