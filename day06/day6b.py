i = [x for x in ((open("day06/input", "r")).read()[:-1])]
r=[x+14 for x in range(len(i)-14) if len(set(i[x:x+14]))==len(i[x:x+14])][0]
print(r)