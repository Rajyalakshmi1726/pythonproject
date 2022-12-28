"""import time
start=time.perf_counter()
def calculateTime():
    print("sleep for 5seconds")
    time.sleep(5)
    print("completed sleep")
calculateTime()
calculateTime()
calculateTime()
finish=time.perf_counter()
print(f'Finishedin{finish-start} seconds')"""

"""import threading
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
print(f'Finished in{finish - start} seconds')"""




####context::
import concurrent.futures
import time
start=time.perf_counter()
def calculateTime(seconds):
    print(f"sleep for{seconds} seconds\n")
    time.sleep(seconds)
    print(f"completed{seconds} sleep\n")
with concurrent.futures.ThreadPoolExecutor() as executor:
    results=[executor.submit(calculateTime,2)for _ in range(5)]
    for r in concurrent.futures.as_completed(results):
        #print(r)
        print(r.result())
finish=time.perf_counter()
print(f'finished in {finish-start}seconds')
