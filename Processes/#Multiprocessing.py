import multiprocessing
import time
import concurrent.futures

def sleeper(secs):
    print("Sleeping...")
    time.sleep(secs)
    return (f"{secs} second(s) passed.")



if __name__ == "__main__":
    start = time.perf_counter()

    #* Multiprocessing module

    #? Manually
    # p1 = multiprocessing.Process(target=sleeper)
    # p2 = multiprocessing.Process(target=sleeper)

    # p1.start()
    # p2.start()
    
    # p1.join()
    # p2.join()

    #? Looping
    # processes = []

    # for _ in range(10):
    #     p = multiprocessing.Process(target=sleeper)
    #     p.start()
    #     processes.append(p)
    
    # for process in processes:
    #     process.join()

    #* Concurrent Futures module

    with concurrent.futures.ProcessPoolExecutor() as executor:
    #     p1 = executor.submit(sleeper)

        secs = [6,5,4,3,2,1]
        # results = [executor.submit(sleeper,sec) for sec in secs]

        # for f in concurrent.futures.as_completed(results):
        #     print(f.result())

        results = executor.map(sleeper,secs)    

        for result in results:
            print(result)



    end = time.perf_counter()
    print(f'Finished in {round(end-start,2)} Seconds.')


