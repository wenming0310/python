import datetime
import time

def timer_function(sched_Timer):
    flag = 0
    while True:
        now = str(datetime.datetime.now())[:-7]
        time.sleep(0.5)
        if (now == str(sched_Timer))&(flag == 0):
            #print(now)
            run_task()
            flag = 1
        else:
            if flag == 1:
                sched_Timer = sched_Timer + datetime.timedelta(minutes=1)
                flag = 0

def run_task():
    text = 'xxxx'
    print('{0} ,run the timer task at {1}\n'.format(text, datetime.datetime.now()))

if __name__ == '__main__':
    sched_Timer = datetime.datetime(2018,3,21,20,35,0)
    #print(sched_Timer)
    #print('run the timer task at {0}'.format(sched_Timer))
    print(str(sched_Timer))
    timer_function(sched_Timer)