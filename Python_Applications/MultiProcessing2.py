import os
import time
import multiprocessing

def SumEven(No):
    print(f"PId of SumEven : {os.getpid()} PPId of SumEven is : {os.getppid()}")
    Sum = 0

    for i in range(2,No,2):
        Sum = Sum+i
    
    print("Summation of even : ", Sum)
def SumOdd(No):
    print(f"PId of SumOdd : {os.getpid()} PPId of SumOdd is : {os.getppid()}")
    Sum = 0

    for i in range(1,No,2):
        Sum = Sum+i
    
    print("Summation of odd : ", Sum)

def main():
    print(f"PId of Main : {os.getpid()} PPId of Main is : {os.getppid()}")

    start_time = time.perf_counter()
    
    t1 = multiprocessing.process(target=SumEven, args=(1000000,))
    t2 = multiprocessing.process(target=SumOdd, args=(1000000,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end_time = time.perf_counter()

    print(f"Time required is : {end_time-start_time:.4f}")

if __name__ == "__main__":
    main()