with open('Day1Input.txt') as f: 
    inputf=f.readlines()

records=len(inputf)

maxcal = 0;
elfcal = 0;

for i in inputf:
    
    if i != '\n':
        elfcal= elfcal + int(i)
    else: 
      if maxcal < elfcal:
        maxcal = elfcal
      elfcal = 0

print(maxcal)

