from math import dist

def Hmove(H, T, Tpos, direction, no):
    for moves in range(0, no):
        if direction == 'D': 
            H = [H[0], H[1]-1]
        if direction == 'U':
            H = [H[0], H[1]+1]
        if direction == 'L': 
            H = [H[0]-1, H[1]]
        if direction == 'R':
            H = [H[0]+1, H[1]]
        for i in range(0, len(T)):
            if i > 0:
                T[i],Tpos[i]=Tmove(T[i-1],T[i],Tpos[i])
            else:
                T[i],Tpos[i]=Tmove(H,T[i],Tpos[i])

    return (H, T, Tpos)



def Tmove(H, T, Tpos=[]):
    dr = (H[0]-T[0])
    dc = (H[1]-T[1])
    if abs(dr)<=1 and abs(dc)<=1:
        # ok
        pass
    elif abs(dr)>=2 and abs(dc)>=2:
        #2       2       2 
        # 1   ->  1   ->  .   -> 2
        #  H       .H      1H     1H
        T = (H[0]-1 if T[0]<H[0] else H[0]+1, H[1]-1 if T[1]<H[1] else H[1]+1)
    elif abs(dr)>=2:
        # T     T       .
        #  H ->  .H  ->  TH
        T = (H[0]-1 if T[0]<H[0] else H[0]+1, H[1])
    elif abs(dc)>=2:
        T = (H[0], H[1]-1 if T[1]<H[1] else H[1]+1)
    Tpos.append(T) 
    return(T, Tpos)

        
#Main Code
filea='2022/Day9/Day9Input.txt'

with open(filea, 'r') as f: 
    inputf=f.read().strip().split('\n')

#Starting Places
H = [0, 0]
T = [[0, 0]]
Tpos = [[[0,0]]]

for line in inputf:
    #Part 1
    H,T,Tpos = Hmove(H, T, Tpos, line.split()[0], int(line.split()[1]))

print(H,T)
print(len(set(tuple(i) for i in Tpos[0])))

H = [0, 0]
T = [[0, 0] for i in range(0,9)]
Tpos = [[[0,0]] for i in range(0,9)]
for line in inputf:
    H,T,Tpos = Hmove(H,T, Tpos, line.split()[0], int(line.split()[1]))

print(H,T)
print(len(set(tuple(i) for i in Tpos[8])))
