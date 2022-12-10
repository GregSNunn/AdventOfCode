#Main Code
filea='2022/Day10/Day10Input.txt'

with open(filea, 'r') as f: 
    inputf=f.read().strip().split('\n')

x=1
cycles=[x]

for i in inputf:
    if i == 'noop':
        cycles.append(x)
    else:
        cycles.append(x)
        x = x+int(i.split()[1]) 
        cycles.append(x)

sigs = [20,60,100,140,180,220]
sigstr = [cycles[i-1]*i for i in sigs]
print(sigstr)
print(sum(sigstr))

CRT=[]
for i in range(0, len(cycles)):
    if cycles[i] <= (i+1)%40 <= cycles[i]+2:
        CRT.append('#')
    else:
        CRT.append('.')

with open('2022/Day10/Day10Part2Sol.txt', 'w') as sol:
    for i in range(0,6):
        print(CRT[i*40:(i+1)*40-1], file=sol)

