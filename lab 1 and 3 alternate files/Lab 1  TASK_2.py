with open('Question2 input1.txt') as inp:
    a=inp.read()
khali=[]
ok= a.split('\n')
for i in range(len(ok)):
    if i>1:
        khali.append(ok[i].split(' '))

l1=[]
for i in range(len(khali)):
    for j in range(len(khali[i])):
        if khali[i][j]=='A':
            l1.append([i,j])


row=[-1,1,0,0]
col=[0,0,-1,1]

def bfs(l1):
    vis = []
    new=l1.copy()
    time=0
    while l1:
        f,t=l1.pop(0)
        new.pop()

        for i in range(4):
           if f+row[i]>=0 and f+row[i]<len(khali) and t+col[i]>=0 and t+col[i]<len(khali[0]) and khali[f+row[i]][t+col[i]]=='H':
                if [f+row[i],t+col[i]] not in vis:
                    khali[f+row[i]][t+col[i]]='A'
                    vis.append([f+row[i],t+col[i]])
                    l1.append([f+row[i],t+col[i]])

        if len(new)==0:
            time+=1
            new=l1.copy()
    return time


print('Total',bfs(l1)-1,'minutes')
s=0
for i in range(len(khali)):
    for j in range(len(khali[i])):
        if khali[i][j]=='H':
            s+=1
if s==0:print('No one survived')
else:print('Total:',s,'survived')