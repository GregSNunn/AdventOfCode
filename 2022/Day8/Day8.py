#Main Code
filea='2022/Day8/Day8Input.txt'

with open(filea, 'r') as f: 
    inputf=f.readlines()

forest_init=[]
for i in inputf:
    forest_init.append([*i.strip()])

visible=[]
forest=[]
for i in forest_init:
    line=[]
    fline=[]
    for j in i:
        fline.append(int(j))
        line.append(False)
    visible.append(line)
    forest.append(fline)

def tree_chk(x,y):
    max1,max2,max3,max4 = 0,0,0,0
    for ix in range(0, x):
        if forest[ix][y] > max1: max1=forest[ix][y]
    for iy in range(x+1, len(forest)):
        if forest[iy][y] > max2: max2=forest[iy][y]
    for jx in range(0, y):
        if forest[x][jx] > max3: max3=forest[x][jx]
    for jy in range(y+1, len(forest[i])):
        if forest[x][jy] > max4: max4=forest[x][jy]
    if forest[x][y] > min(max1,max2,max3,max4): visible[x][y] = True

def tree_sce(x,y):
    up,left,right,down=[],[],.[],[]
    for ix in range(0, x):
         left.append(forest[ix][y])
    for iy in range(x+1, len(forest)):
         right.append(forest[iy][y])
    for jx in range(0, y):
         up.append(forest[x][jx])
    for jy in range(y+1, len(forest[i])):
         down.append(forest[x][jy])

#Part 1
for i in range(0, len(forest)):
    for j in range(0, len(forest[i])):
        if i == 0 or i == len(forest)-1:
            visible[i][j] = True
        elif j==0 or j == len(forest[i])-1:
            visible[i][j] = True
        else:
            tree_chk(i, j)

tot=0
for line in visible:
    #print(line)
    tot = tot + sum(line)
print(tot)