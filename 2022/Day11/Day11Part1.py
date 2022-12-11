#Main Code
filea='2022/Day11/Day11Input.txt'

with open(filea, 'r') as f: 
    inputf=f.read()

info=[i.split('\n') for i in inputf.split('\n\n')]

items  = [i[1].split(':')[1].strip().split(',') for i in info]
ops    = [i[2].split(':')[1].strip() for i in info]
test   = [i[3].split(':')[1].strip().split()[2] for i in info]
trues  = [i[4].split(':')[1].strip().split()[3] for i in info]
falses = [i[5].split(':')[1].strip().split()[3] for i in info]

#print(items)
#print(ops)
#print(test)
#print(trues)
#print(falses)

inspecs=[0 for i in ops]

def operation(op, old):
    new = eval(op.split('=')[1]) // 3
    return new

for round in range(0,20):
    for turn in range(0, len(ops)):
        for i in range(0, len(items[turn])):
            items[turn][i] = int(items[turn][i] )
            x = operation(ops[turn], items[turn][i] )
            inspecs[turn] +=1
            if x % int(test[turn]) == 0:
                items[int(trues[turn])].append(x)
            else:
                items[int(falses[turn])].append(x)
        items[turn] = []

inspecs.sort(reverse=True)

print(inspecs[0]*inspecs[1])


