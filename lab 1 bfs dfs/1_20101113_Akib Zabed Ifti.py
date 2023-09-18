#----------------------------- TASK 1 --------------------------------------------------------------------------------------------------------

rws = [1, 1, 1, 0, 0, -1, -1, -1]
cws = [1, 0, -1, 1, -1, 1, 0, -1]
def final(graph):
    row = len(graph)
    col = len(graph[0])
    explored=[]
    count=[0]
    track=[]
    neigh=[]
    for i in range(row):
        explored.append([0]*col)
    for i in range(row):
        for j in range(col):
            if graph[i][j]=="Y" and explored[i][j]==0:
                count[0]=1
                neigh.append([i,j])
                explored[i][j] = 1
                while neigh:
                    x,y=neigh.pop(0)
                    for (k, l) in zip(rws, cws):
                        if y + l >= 0 and y + l < col and x + k >= 0 and x + k < row and graph[x + k][y + l] == "Y" and explored[x + k][y + l] == 0:
                            count[0] += 1
                            if explored[x+k][y+l]!= 1:
                                neigh.append([x+k,y+l])
                                explored[x+k][y+l] = 1

                track.append(count[0])
    return max(track)


file = open("input()1.txt")
graph=[]
s=file.read()
s=s.split('\n')
for i in s:
    graph.append(i.split(' '))
print(final(graph))

#---------------------------------------TASK 2---------------------------------------------------------------------------

def bfs(graph, explored,r,c):
    count=0
    cut=0
    q=[]
    q.append((r, c))
    explored[r][c]=1
    while len(q) > 0:
        x,y= q.pop(0)
        for i in range(4):
            ax = x + rws[i]
            ay = y + cws[i]
            if ay>=0 and ay<col and ax>=0 and ax<row and graph[ax][ay]=='H' and explored[ax][ay]==0:

                if graph[r][c]=='A':
                    graph[ax][ay]='A'

                q.append((ax, ay))
                explored[ax][ay]=1
            elif ay>=0 and ay<col and ax>=0 and ax<row and graph[ax][ay]=='T' and explored[ax][ay]==0:
                for i in range(4):
                    aix=ax+rws[i]
                    aiy=ay+cws[i]
                    if aiy >= 0 and aiy < col and aix >= 0 and aix < row and graph[aix][aiy] == 'A' and explored[aix][aiy] == 0:
                        q.append((aix, aiy))
                        explored[aix][aiy] = 1
            cut+=1
        count += 1
    return graph,cut//count





file = open("Question2 input1.txt")
graph=[]
s=file.read()
s=s.split('\n')
for i in range(0,len(s)):
    if i==0:
        row=int(s[i])
    elif i==1:
        col=int(s[i])
    else:
        graph.append(s[i].split(' '))
explored = [[0]*col for i in range(row)]

rws=[-1,0,1,0]
cws=[0,1,0,-1]
a=bfs(graph,explored,0,0)
g=a[0]
surv=0
for i in range(row):
    for k in range(col):
        if g[i][k]=='H':
            surv+=1
if surv==0:
    print("No one survived")
else:
    print(surv,'survived')
print('Time:',a[1],'minutes')


