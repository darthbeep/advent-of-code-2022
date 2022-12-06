i=open("day06/input", "r").read()[:-1]
r=[len({*i[x-14:x]})for x in range(len(i))].index(14)
print(r)