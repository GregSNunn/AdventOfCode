import pandas as pd
import re

#Crane 9000 Moves the top of Stack1 to top of Stack2
def crane9000(stack1, stack2):
    crate = stack1[0]
    stack1.remove(stack1[0])
    stack2.insert(0, crate)

#Crane 9001 Moves the top of Stack1 to top of Stack2
def crane9001(no, stack1, stack2):
    for x in range(0, no):
        crate = stack1[no-x-1]
        stack1.remove(stack1[no-x-1])
        stack2.insert(0, crate)

def topcrate(crate_set):
    top=''
    for sublist in crate_set:
        if len(sublist) != 0:
            top = top+sublist[0]
        else:
            top = top+' '
    top2=re.sub(r"[\[\]]","", top)
    return top2

#Main Code
filea='2022/Day5/Day5Input.txt'

with open(filea, 'r') as f: 
    inputf=f.read()

#Crate Input
crates_chk_init = inputf.split("\n\n")[0]
crates_chk=crates_chk_init.splitlines()
crates_lines=len(crates_chk)

#Find the Number of Crates
ncrates = int((crates_chk[crates_lines-1].split())[-1])
print(ncrates)

#Converting Each Crate into List
crates_init=pd.read_fwf(filea, colspecs='infer', infer_nrows=crates_lines, header=None).head(crates_lines-1)
crates,crates9001=[],[]
for i in range(0, ncrates):
    crates.append([x for x in crates_init.iloc[:, i].tolist() if str(x)!='nan'])
    crates9001.append([x for x in crates_init.iloc[:, i].tolist() if str(x)!='nan'])

#Pulling Information out of Move lines
moves_init = inputf.split("\n\n")[1]
moves=moves_init.splitlines()

#Using Crane 9000
for move in moves:
    move_info = [int(s) for s in re.findall(r'-?\d+\.?\d*', move)]
    for i in range(0, move_info[0]):
        crane9000(crates[move_info[1]-1], crates[move_info[2]-1])
print(topcrate(crates))

#Using Crane 9001
for move in moves:
    move_info = [int(s) for s in re.findall(r'-?\d+\.?\d*', move)]
    crane9001(move_info[0], crates9001[move_info[1]-1], crates9001[move_info[2]-1])
print(topcrate(crates9001))


