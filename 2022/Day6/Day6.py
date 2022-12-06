
def packet_chk(list, start, low):
    pack_chk=list[start-low:start+1]
    if len(pack_chk) == len(set(pack_chk)):
        return True
    else:
        return False

def pack_loop(msglen):
    for x in range(msglen-1, len(stream)):
        chk=packet_chk(stream, x, msglen-1)
        if chk == True:
            print(x+1)
            break
        else: 
            continue

#Main Code
filea='2022/Day6/Day6Input.txt'

with open(filea, 'r') as f: 
    inputf=f.read()
stream=([*inputf])

pack_loop(4) #Part 1
pack_loop(14) # Part 2