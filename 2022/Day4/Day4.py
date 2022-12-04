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
    if (int(x[0][0]) <= int(x[1][0])) and (int(x[0][1]) >= int(x[1][1])):
        inc_chk = True
    elif (int(x[1][0]) <= int(x[0][0])) and (int(x[1][1]) >= int(x[0][1])):
        inc_chk = True
    else: 
        inc_chk=False
    incs.append(inc_chk)

print(sum(incs))

#Determine if they don't overlap to determine those that do
ovrlp = []
for x in pairs:
    if (int(x[0][0]) < int(x[1][0])) and (int(x[0][1]) < int(x[1][0])):
        ovrlp_chk = False
    elif (int(x[0][0]) > int(x[1][1])) and (int(x[0][1]) < int(x[1][1])):
        ovrlp_chk = False
    elif (int(x[1][0]) < int(x[0][0])) and (int(x[1][1]) < int(x[0][0])):
        ovrlp_chk = False
    elif (int(x[1][0]) > int(x[0][1])) and (int(x[1][1]) > int(x[0][1])):
        ovrlp_chk = False
    else: 
        ovrlp_chk=True
    ovrlp.append(ovrlp_chk)  

print(sum(ovrlp))