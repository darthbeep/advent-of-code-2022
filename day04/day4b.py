import re
i = [list(map(int, y)) for y in [re.split(',|-', x) for x in ((open("day04/input", "r")).read()[:-1]).split('\n')]]
r = len([x for x in i if bool(set(range(x[0],x[1]+1))&set(range(x[2],x[3]+1)))])
print(r)