import math
import random as rd
m, n = math.inf, -math.inf

def abprun(depth, pos, bool,values, alpha, beta):
    if depth == 0:
        return values[pos]
    if bool:
        maxeval = n
        for i in range(0, 2):
            val = abprun(depth - 1, pos * 2 + i,False, values, alpha, beta)
            maxeval = max(maxeval, val)
            alpha = max(alpha, maxeval)
            if beta <= alpha:
                break
        return maxeval

    else:
        mineval = m
        for i in range(0, 2):
            val = abprun(depth - 1, pos * 2 + i,True, values, alpha, beta)
            mineval = min(mineval, val)
            beta = min(beta, mineval)
            if beta <= alpha:
                break
        return mineval

Id='28181113'
s=int(Id[3])
mini=int(Id[4])
mv=int(Id[-1]+Id[-2])
maxi= (mv*3)//2


values = []
for i in range(8):
    values.append(rd.randint(mini,maxi))
print('Generated 8 random points between the minimum and maximum point limits:',values)

sol= abprun(0, 0, True, values, n, m)

print('Total points to win:',mv)
print('Achieved point by applying alpha-beta pruning =',sol)

if sol >= mv:
    print('The winner is Optimus Prime')
else:
    print('The Winner is Megatron')

#========================================= Task 2 =====================================================================
track=[]
count=0
for i in range(s):
    rd.shuffle(values)
    sol2 = abprun(3, 0, True, values, n, m)
    track.append(sol2)

print('\nAfter the shuffle\nList of all points values from each shuffles:',track,'\nThe maximum value of all shuffles:',max(track))
for i in track:
    if i>=mv:
        count+=1
print('Won', count ,'times out of', len(track) ,'number of shuffles')