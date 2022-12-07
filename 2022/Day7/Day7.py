
#Convert Stream Into Directory
def directory(dir, start):
    #Used to Build Current Direct
    ndir = []

    #Used to note indices of current directory
    cdir=[]
    for i in range(start, len(stream)):
        stream[i]=stream[i].strip()
        if stream[i] == "$ cd " + dir:
            #Move into Current Dir
            cdir.append(i)
            j = i+1
            #Loop until end of processing of current directory
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
    #Remove Used Stream Lines
    for index in reversed(cdir):
        del stream[index]
    return ndir

#Part 1
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

#Part 2
def sysred(sys, ans, tot):
    dir=0
    for i in sys:
        if type(i) != int:
            subdir,ans=sysred(i, ans, tot)
            dir += subdir
        else:
            dir += i
    if tot <= dir < ans:
        ans = dir
    return (dir, ans)

#Main Code
filea='2022/Day7/Day7Input.txt'

with open(filea, 'r') as f: 
    inputf=f.readlines()

stream =[]
for i in inputf:
    i=i.strip()
    #Remove ls statements
    if i != '$ ls':
        stream.append(i)

system=directory('/', 0)
print(system)

part1=syssize(system, 0)
print(part1)

part2=sysred(system, float('inf'), 30000000-70000000+part1[0])
print(part2)



                    