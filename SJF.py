#ASSUME ALL PROCESSES ARRIVED AT TIME 0
n= int(input('Enter the Number of processes'))
wt=[]
tat=[]
bt=[]
bt.insert(0,0)
wt.insert(0,0)
tat.insert(0,0)
avgwt=0
avgtat=0

for i in range(1,n+1):
    wt.insert(i,0)
    bt.insert(i,int(input('Enter Burst time for process',i)))

bt.sort()

for i in range(1,n+1):
    wt.append(wt[i-1]+bt[i-1])
    tat.append(wt[i]+bt[i])
    avgwt+=wt[i]
    avgtat+=tat[i]

avgwt/=n
avgtat/=n

print('average waiting time is: ',avgwt)
print('average turnaround time is: ',avgtat)

