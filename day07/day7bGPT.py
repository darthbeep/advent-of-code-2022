l,s={},{}
d=''
i=0
def f(d):
    sz=s[d]
    for i in l[d]:sz+=f(i)
    return sz

for c in[x.split()for x in open("day07/input")]:
    if c[0]=='$':
        if c[1]=='cd':
            if c[2]=='..':d='/'.join(d.split('/')[:-1])
            else:d+='/'+c[2]
        elif c[1]=='ls':
            if d in l:print(d)
            l[d],s[d]=[],0
    elif c[0]=='dir':l[d].append(d+'/'+c[1])
    else:s[d]+=int(c[0])

r={}
for d in l:r[d]=f(d)

print(min([r[d] for d in s if f(d)>=3e7-(7e7-f('//'))]))
