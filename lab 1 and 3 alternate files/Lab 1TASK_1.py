with open('input.txt') as inp:
    a=inp.read()
khali=[]
ok= a.split('\n')
for i in range(len(ok)):
        khali.append(ok[i].split(' '))
l1=[]
for i in range(len(khali)):
    for j in range(len(khali[i])):
        if khali[i][j]=='Y':
            l1.append([i,j])


row=[-1,1,0,0,-1,-1,1,1]
col=[0,0,-1,1,1,-1,1,-1]

def bfs(l1):
    count=0
    vis = []
    q=[]
    q.append(l1)
    vis.append(l1)

    while q:
        count+=1
        f,t=q.pop(0)

        for i in range(8):
           if f+row[i]>=0 and f+row[i]<len(khali) and t+col[i]>=0 and t+col[i]<len(khali[0]) and khali[f+row[i]][t+col[i]]=='Y':
                if [f+row[i],t+col[i]] not in vis:
                    vis.append([f+row[i],t+col[i]])
                    q.append([f+row[i],t+col[i]])
    return count

result=[]
for i in l1:
    result.append(bfs(i))
print(max(result))
