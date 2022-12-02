##############
#Part 1
##############

#Bring in Data
with open('Day2Input.txt') as f: 
    inputf=f.readlines()

games = []

for i in inputf:
    games.append(i.split())

scores = []

####################
# A/X = Rock (1 point)
# B/Y = Paper (2 points)
# C/Z = Scissors (3 points)
####################

for j in games:
    if j[0] == 'A':
        if j[1] == 'X': 
            scores.append(4)
        elif j[1] == 'Y':
            scores.append(8)
        elif j[1] == 'Z':
            scores.append(3)
    elif j[0] == 'B':
        if j[1] == 'X': 
            scores.append(1)
        elif j[1] == 'Y':
            scores.append(5)
        elif j[1] == 'Z':
            scores.append(9)
    elif j[0] == 'C':
        if j[1] == 'X': 
            scores.append(7)
        elif j[1] == 'Y':
            scores.append(2)
        elif j[1] == 'Z':
            scores.append(6)
    else:
        scores.append(0)
        
print(sum(scores))
