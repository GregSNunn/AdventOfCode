#Main Code
with open('2022/Day4/Day4Input.txt') as f: 
    inputf=f.readlines()

#Split out each Value into Matrix
pairs=[]
for i in inputf:
    i=i.strip()
    pair=i.split(',')
    pairs_init=[]
    for j in pair:
        pair2=j.split('-')
        pairs_init.append(pair2)
    pairs.append(pairs_init)
           
#Determine if one includes the other
incs = []
for x in pairs:
    inc_chk = False
    if x[0][0] <= x[1][0] and x[0][1] >= x[1][1]:
        inc_chk = True
    elif x[1][0] <= x[0][0] and x[1][1] >= x[0][1]:
        inc_chk = True
    incs.append(inc_chk)

print(incs)