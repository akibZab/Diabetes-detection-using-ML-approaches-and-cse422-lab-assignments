import random
def start(no):
    st=''
    for j in range(4):
        for i in range(int(no)):
            st+=str(random.randint(0,1))
        if j!=3:
            st+=' '
    st=st.split(' ')
    return st

def crossover(st):
    new=[]
    l=len(st[0])
    for i in range(len(st)):
        for j in range(i+1,len(st)):
            huh=st[i][0:l//2]+st[j][(l//2):l]
            duh=st[j][0:l//2]+st[i][(l//2):l]
            new.append(huh)
            new.append(duh)
    return new
#
def mutation(new,no):
    new2=[]
    for i in new:
        mut=random.randint(0,int(no)-1)
        if i[mut]=='1':
            i=i[:mut]+'0'+i[mut+1:]
        elif i[mut]=='0':
            i=i[:mut]+'1'+i[mut+1:]
        new2.append(i)
    return new2


# #---------------------------
def fitness_check(new2,run,player,total):
    values=[]
    for i in new2:
        whole = 0
        for j in range(len(i)):
            if i[j]=='1':
                whole+=int(run[j])
        values.append(abs(whole-int(total)))

    if 0 in values:
        min_val=min(values)
        minind=values.index(min_val)
        return new2[minind]
    else:
        max_value=max(values)
        maxind=values.index(max_value)
        new2.pop(maxind)
        return new2




f=open('input()1.txt')
s=f.read()
s=s.split('\n')
player=[]
run=[]
no,total=s[0].split(' ')
for i in range(1,len(s)):
    x,y=s[i].split(' ')
    player.append(x)
    run.append(y)
hehe=start(no)

limit=100
for i in range(limit):
    answer=''
    q1= crossover(hehe)
    q2= mutation(q1,no)
    q3 = fitness_check(q2,run,player,total)
    if type(q3)==str:
        print(player)
        answer=q3
        print(answer)
        break
    else:
        hehe=q2[0:4]

if answer=='':
    print(player)
    print('-1')


