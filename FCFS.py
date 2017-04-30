n= int(input('Enter the Number of processes'))
at=[]
wt=[]
tat=[]
bt=[]
bt.insert(0,0)
wt.insert(0,0)
tat.insert(0,0)
at.insert(0,0)
avgwt=0
avgtat=0

for i in range(1,n+1):
    at.insert(i,i+1)
    bt.insert(i,int(input('Enter Burst time for process',i)))
for i in range(1,n+1):
    wt.append(wt[i-1]+bt[i-1]+at[i-1]-at[i])
    if(wt[i]<0):
        wt[i]=0
    tat.append(wt[i]+bt[i])
    avgwt+=wt[i]
    avgtat+=tat[i]

avgwt/=n
avgtat/=n

print('average waiting time is: ',avgwt)
print('average turnaround time is: ',avgtat)

