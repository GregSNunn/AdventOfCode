##############
#Part 1
##############

#Bring in Data
with open('Day1Input.txt') as f: 
    inputf=f.readlines()

records=len(inputf)

#Initial Variables
maxcal = 0;
elfcal = 0;

#Loop to Determine Max Calories
for i in inputf:
    
    if i != '\n':
        elfcal= elfcal + int(i)
    else: 
      if maxcal < elfcal:
        maxcal = elfcal
      elfcal = 0

print(maxcal)

##############
#Part 2
##############

elfcals = []
elfcal2 = 0
for j in inputf:

    if j != '\n': 
        elfcal2 = elfcal2 + int(j)
    else: 
        elfcals.append(elfcal2)
        elfcal2 = 0

elfcals.sort(reverse=True)
top3=elfcals[0:3]

sum=sum(top3)
print(sum)
