commands = [x.split(' ') for x in open("day07/input", "r").read()[:-1].split('\n')]

dir_list = {}
dir_size = {}

dirname = ''
i = 0

def get_dir_size_full(dir):
    size = dir_size[dir]
    for d in dir_list[dir]:
        size += get_dir_size_full(d)
    return size

while i < len(commands):
    cmd = commands[i]
    if cmd[0] == '$' and cmd[1] == 'cd':
        if cmd[2] == '..':
            dirname = '/'.join(dirname.split('/')[:-1])
        else:
            dirname += '/' + cmd[2]
    elif cmd[0] == '$' and cmd[1] == 'ls':
        if dirname in dir_list:
            print(dirname)
        dir_list[dirname] = []
        dir_size[dirname] = 0
    elif commands[i][0] == 'dir':
        dir_list[dirname].append(dirname + '/' + cmd[1])
    else:
        dir_size[dirname] += int(cmd[0])
    i+=1

dir_size_full = {}
for d in dir_list:
    dir_size_full[d] = get_dir_size_full(d)

size_sum = 0
for d in dir_size_full:
    if dir_size_full[d] <= 100000:
        size_sum += dir_size_full[d]

print(size_sum)