
class Process:
    def __init__(self,name,arrival_time,burst_time):
        self.name=name
        self.arrival_time=arrival_time
        self.burst_time=burst_time
        self.remaining_time=burst_time
        self.add_status=0
        self.waitingtime=None
        self.turnaroundtime=None

    def __repr__(self):
        return '{}-{}'.format(self.name,self.arrival_time,self.waitingtime,self.turnaroundtime)





 def remaining_time_sort(Process):
    return Process.remaining_time

n=int(input('Enter the nuber of processes') )
TimeQuantum=int(input('Enter the time Quantum'))

Processes=[]
for i in range (n):
    arrivaltime = int(input('Enter the arrival time for process: ',i))
    bursttime = int(input('Enter the burst time for process: ',i))
    P=Process(i,arrivaltime,bursttime)
    Processes.append(P)

avg_waiting_time=0
avg_turnaround_time=0
Operations=True
time=0
current=0
while (Operations==True):
    increment_current = True
    if(current>=n):
        current=0
    if(time>=Processes[current].arrivaltime and Processes[current].remaining_time>0):
        increment_current=False
        for i in range (TimeQuantum):
            Processes[current].remaining_time-=1
            time+=1
            if(Processes[current].remaining_time==0):
                Processes[current].waiting_time = time - Processes[current].arrival_time - Processes[current].burst_time
                Processes[current].turnaroundtime = time - Processes[current].arrival_time
                avg_waiting_time += Processes[current].waiting_time
                avg_turnaround_time += Processes[current].turnaround_time
                Processes.remove(current)
        Processes.sort(key=remaining_time_sort)
        current=0


    for i in range(n):
        if(len(Processes)==0):
            Operations=False
            break
        if (Processes[i].remaining_time > 0):
            Operations=True
            break
        else:
            Operations = False
    if(increment_current == True):
        current+=1





avg_waiting_time/=n
avg_turnaround_time/=n

print('Average Waiting Time = ',avg_waiting_time)
print('Average Turnaround Time = ',avg_turnaround_time)
















