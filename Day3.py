#Split the Bag into Compartments
def compartments(fullbag):
    fullbag2=fullbag.strip()
    items=len(fullbag2)
    comps=[fullbag2[0:int(items/2)], fullbag2[int(items/2):items]]
    return comps

def priority(letter):
    priority=ord(letter)
    if priority >= 97:
        priority = priority - 96
    elif priority >= 65:
        priority = priority - 38
    return priority

#Main Code
with open('Day3Input.txt') as f: 
    inputf=f.readlines()

comps = []

for i in inputf:
    comps.append(compartments(i))

letters = []
for j in comps:
    s1=j[0]
    s2=j[1]
    slet=list(set(s1)&set(s2))
    letters.append(priority(slet[0]))

print(sum(letters))

badges = []
groups=int((len(inputf))/3)

for j in range(0, groups):
    x=j*3
    s1=inputf[x].strip()
    s2=inputf[x+1].strip()
    s3=inputf[x+2].strip()
    sletg=list(set(s1)&set(s2)&set(s3))
    badges.append(priority(sletg[0]))

print(sum(badges))