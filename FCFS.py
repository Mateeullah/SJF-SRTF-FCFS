n= int(input('Enter the Number of processes'))
arrival_time=[]
waiting_time=[]
turnaround_time=[]
burst_time=[]
burst_time.insert(0,0)
waiting_time.insert(0,0)
turnaround_time.insert(0,0)
arrival_time.insert(0,0)
avg_waiting_time=0
avg_turnaround_time=0

for i in range(1,n+1):
    arrival_time.insert(i,i+1)
   burst_time.insert(i,int(input('Enter Burst time for process',i)))
for i in range(1,n+1):
   waiting_time.append(waiting_time[i-1]+burst_time[i-1]+arrival_time[i-1]-arrival_time[i])
    if(waiting_time[i]<0):
        waiting_time[i]=0
    tat.append(waiting_time[i]+burst_time[i])
    avg_waiting_time+=waiting_time[i]
    avg_turnaround_time+=turnaround_timet[i]

avg_waiting_time/=n
avg_turnaround_time/=n

print('average waiting time is: ',avg_waiting_time)
print('average turnaround time is: ',avg_turnaround_time)

