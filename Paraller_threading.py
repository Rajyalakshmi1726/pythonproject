import time

import Tools.scripts.pindent

start=time.perf_counter()
def calculateTime():
    print("sleep for 5seconds")
    time.sleep(5)
    print("completed sleep")
calculateTime()
calculateTime()
calculateTime()
finish=time.perf_counter()
print(f'Finishedin{finish-start} seconds')


import threading
import time
start = time.perf_counter()
def calculateTime():
    print("sleep for 5seconds")
    time.sleep(5)
    print("completed sleep")
t1=threading.Thread(target=calculateTime)
t2=threading.Thread(target=calculateTime)
t3=threading.Thread(target=calculateTime)
t4=threading.Thread(target=calculateTime)
t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()
finish = time.perf_counter()
print(f'Finished in{finish - start} seconds')