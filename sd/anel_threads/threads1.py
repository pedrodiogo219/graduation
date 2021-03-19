#!/usr/bin/python

import threading
import time

exitFlag = 0

ActiveThread = 0
TotalThreads = 5
globalstring = "Hello Word"

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter


    def run(self):
        self.executeTask(self.name)


    def executeTask(self,threadName):
        # time.sleep(1)
        global ActiveThread
        global TotalThreads
        global globalstring

        while True:

            if self.checkCompleteTask():
                break


            if ActiveThread == self.threadID:
                # Se é a vez dessa thread fazer a tarefa, ela executará
                for i in range(0,len(globalstring)):
                    if globalstring[i].isupper():
                        if i != 0 and i != (len(globalstring)-1):
                            globalstring = globalstring[0:i:]+globalstring[i].lower()+globalstring[i+1::]
                        elif i == 0:
                            globalstring = globalstring[0].lower()+globalstring[1::]
                        else:
                            globalstring = globalstring[:len(globalstring)-1:]+globalstring[i].lower()
                        
                        print(globalstring)
                        
                        ActiveThread = (ActiveThread+1) % TotalThreads
                        break

            else:
                pass
                # time.sleep(1)

    def checkCompleteTask(self):
        global globalstring
        for i in globalstring:
            if i.isupper():
                return False

        return True

    def print_time(self,threadName, counter, delay):
        while counter:
            if exitFlag:
                threadName.exit()
            time.sleep(delay)
            print(threadName, time.ctime(time.time()))
            counter -= 1

# Create new threads
thread0 = myThread(0, "Thread-0", 0)
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)
thread3 = myThread(3, "Thread-3", 3)
thread4 = myThread(4, "Thread-4", 4)


globalstring = input("Digite a sting: ")

# Start new Threads

thread0.start()
thread1.start()
thread2.start()
thread3.start()
thread4.start()
