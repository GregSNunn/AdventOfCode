import sys
sys.setrecursionlimit(1000)

#Main Code
filea='2022/Day7/Day7Input.txt'

with open(filea, 'r') as f: 
    inputf=f.readlines()

stream =[]
for i in inputf:
    i=i.strip()
    if i != '$ ls':
        stream.append(i)

def directory(dir, start):
    ndir = []
    cdir=[]
    for i in range(start, len(stream)):
        stream[i]=stream[i].strip()
        if stream[i] == "$ cd " + dir:
            cdir.append(i)
            j = i+1
            while j <= len(stream)-1:             
                if stream[j] == "$ cd ..":
                    cdir.append(j)
                    break
                elif stream[j][0] == 'd':
                    subdir=(directory(stream[j][4:], i+1))
                    ndir.insert(j, subdir)
                elif stream[j][2] == 'c':
                    break
                else:
                    ndir.insert(j, int(stream[j].split()[0]))
                cdir.append(j)
                j = j+1
            break
    for index in reversed(cdir):
        del stream[index]
    return ndir

system=directory('/', 0)
print(system)

ans=0
def syssize(sys, ans):
    dir=0
    for i in sys:
        if type(i) != int:
            subdir,ans=syssize(i, ans)
            dir += subdir
        else:
            dir += i
    if dir <= 100000:
        ans +=dir
    return (dir, ans)

print(syssize(system, ans))





                    