class Process:
    def __init__(self,name,arrival_time,burst_time,exec_time_before_IO):
        self.name=name
        self.arrival_time=arrival_time
        self.burst_time=burst_time
        self.burst=burst_time
        self.add_status=0
        self.waitingtime=None
        self.turnaroundtime=None
        self.IO=0
        self.IO_status=0
        if (name%2==1):
             self.exec_t_before_IO=exec_time_before_IO
             self.IO=1
             self.remaining_time=0
             self.comeback_time = -1
             self.IO_status=0

    def __repr__(self):
        return '{}-{}'.format(self.name,self.arrival_time,self.waitingtime,self.turnaroundtime)





 def arrival_sort(Process):
    return Process.arrival_time

n=int(input('Enter the nuber of processes') )
I=int(input('Enter the time I/O takes'))
TimeQuantum=int(input('Enter the time Quantum'))
T=int(input('Enter the time after processes go for I/O'))

Processes=[]
for i in range (n):
    arrivaltime = int(input('Enter the arrival time for process',i))
    bursttime = int(input('Enter the burst time for process',i))
    P=Process(i,arrivaltime,bursttime,T)
    Processes.append(P)

avg_waiting_time=0
avg_turnaround_time=0
Processes.sort(key=arrival_sort)
Operations=True
time=0
current=0
while (Operations==True):
    op1=False
    increment_current = True
    if(current>=n):
        current=0
    for i in range (n):
        if(time==Processes[i].comeback_time or time<Processes[i].arrival_time):
            Processes[i].IO_status = 0
            Pro=Processes[i]
            Processes.pop(i)
            Processes.append(Pro)

    if(time>=Processes[current].arrival_time  and Processes[current].IO_status==0 and Processes[current].burst_time>0):
        if(Processes[current].add_status==0):
          Processes[current].add_status = 1

        if(Processes[current].IO==1 and Processes[current].remaining_time>0):
            for i in range (Processes[current].remaining_time):
                Processes[current].burst_time -= 1
                if (Processes[current].IO == 1):
                  Processes[current].exec_t_before_IO -= 1
                time += 1

                for i in range(n):
                    if (time == Processes[i].comeback_time or time == Processes[i].arrival_time):
                        Processes[i].IO_status = 0
                        Pro = Processes[i]
                        Processes.pop(i)
                        Processes.append(Pro)
                if(Processes[current].burst_time==0):
                    Processes[current].waitingtime = time - Processes[current].arrival_time - Processes[current].burst
                    Processes[current].turnaroundtime = time - Processes[current].arrival_time
                    avg_waiting_time += Processes[current].waitingtime
                    avg_turnaround_time += Processes[current].turnaroundtime
        else:

          for i in range (TimeQuantum):
            Processes[current].burst_time-=1
            if(Processes[current].IO==1):
                Processes[current].exec_t_before_IO-=1
            time+=1
            for i in range(n):
                if (time == Processes[i].comeback_time or time == Processes[i].arrival_time):
                     Processes[i].IO_status=0
                     Pro = Processes[i]
                     Processes.pop(i)
                     Processes.append(Pro)
            if (Processes[current].burst_time == 0):
                Processes[current].waitingtime=time-Processes[current].arrival_time - Processes[current].burst
                Processes[current].turnaroundtime=time-Processes[current].arrival_time
                avg_waiting_time+=Processes[current].waitingtime
                avg_turnaround_time += Processes[current].turnaroundtime
                break
            if(Processes[current].IO==1 and Processes[current].exec_t_before_IO==0):
			    op1=True
                Processes[current].IO_status = 1
                Processes[current].comeback_time = time + I
                Processes[current].exec_t_before_IO = T
                Processes[current].remaining_time=TimeQuantum-1-i
                break


        increment_current = False
        Pro=Processes[current]
        Processes.pop(current)
        Processes.append(Pro)



    op=False
    for i in range(n):
        if(Processes[i].burst_time<=0 or Processes[i].IO_status==1):
            op=False
        else:
            op=True
			break
    if(op==False and op1==False):
        time+=1

    for i in range(n):
        if (Processes[i].burst_time > 0):
		    Operations=True
            break
        else:
            Operations = False
    if(increment_current==True):
        current += 1

avg_waiting_time/=n
avg_turnaround_time/=n

print('Average Waiting Time = ',avg_waiting_time)
print('Average Turnaround Time = ',avg_turnaround_time)














