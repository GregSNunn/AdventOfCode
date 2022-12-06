
def packet_chk(list, start, low):
    pack_chk=list[start-low:start+1]
    if len(pack_chk) == len(set(pack_chk)):
        return True
    else:
        return False


#Main Code
filea='2022/Day6/Day6Input.txt'

with open(filea, 'r') as f: 
    inputf=f.read()
stream=([*inputf])

for x in range(3, len(stream)):
    chk=packet_chk(stream, x, 3)
    if chk == True:
        print(x+1)
        break
    else: 
        continue

for y in range(14, len(stream)):
    chk2=packet_chk(stream, y, 14)
    if chk2 == True:
        print(y)
        break
    else: 
        continue
