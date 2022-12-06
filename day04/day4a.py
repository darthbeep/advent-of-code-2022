import re
i = [list(map(int, y)) for y in [re.split(',|-', x) for x in ((open("day04/input", "r")).read()[:-1]).split('\n')]]
r = len([x for x in i if (x[0]>=x[2] and x[1]<=x[3]) or (x[0]<=x[2] and x[1]>=x[3])])
print(r)