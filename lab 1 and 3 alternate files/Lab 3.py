import random as rad
u=99999
v=-99999
def minimax(dep, p, wd,ap,bt,lis):
    if dep == 3:
        return lis[p]
    if wd:
        tep = v
        for i in range(0, 2):
            val = minimax(dep+1, p * 2 + i,False, ap, bt,lis)
            tep = max(tep, val)
            ap = max(ap, tep)
            if bt <= ap:
                break
        return tep

    else:
        tep = u
        for i in range(0, 2):
            val = minimax(dep+1, p * 2 + i,True, ap, bt,lis)
            tep = min(tep, val)
            bt = min(bt, tep)
            if bt <= ap:
                break
        return tep



id='28181236'
minval= int(id[4])
target=id[::-1]
target=int(target[0:2])
maxval= (target*3)//2
lis = []

for i in range(8):
    lis.append(rad.randint(minval,maxval))



final= minimax(0, 0, True, v, u,lis)

print('Generated 8 random points between the minimum and maximum point limits:',lis)
print('Total points to win:',target)
print('Achieved point by applying alphabeta pruning = ', final)

if target>final:
    print('The Winner is Megatron')

else:
    print('The winner is Optimus Prime')

#task2
no =int(id[3])
lis2=lis
lis3=[final]
for i in range(no-1):
    rad.shuffle(lis2)
    f=minimax(0, 0, True, v, u,lis2)
    lis3.append(f)

print()
print('After the shuffle')
print('List of all points lis from each shuffles:',lis3)
print('The maximum value of all shuffles:',max(lis3))
times=0
for i in range(len(lis3)):
    if lis3[i]>=target:
        times+=1
print('Won '+str(times)+' times out of '+str(len(lis3))+' number of shuffles')