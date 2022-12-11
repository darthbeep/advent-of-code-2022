input = open("day10/input", "r").read()[:-1].split('\n')

states = []
x = 1

for i in input:
    if i == 'noop' or i == 'noo':
        states.append(x)
    else:
        print(i)
        n = int(i.split(' ')[1])
        states.append(x)
        states.append(x)
        x += n

s = (states[19] * 20) + (states[59] * 60) + (states[99] * 100) + (states[139] * 140) + (states[179] * 180) + (states[219] * 220)
print(s)
