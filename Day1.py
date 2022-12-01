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


