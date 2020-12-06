
import concurrent.futures 
import time

start = time.perf_counter()

def sleeper(secs):
    print("Sleeping...")
    time.sleep(secs)
    return (f"{secs} second(s) passed.")


#* Threading module

#? Doing Manually
# t1 = threading.Thread(target=somecode)
# t2 = threading.Thread(target=somecode)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

#? Looping
# threads = []

# for _ in range(10):
#     t = threading.Thread(target=sleeper,args=[2])
#     t.start()
#     threads.append(t)


# for thread in threads:
#     thread.join()

#* Concurrent.futures module

with concurrent.futures.ThreadPoolExecutor() as excutor:

    #? Doing Manually
    # f1 = excutor.submit(sleeper,2)
    # f2 = excutor.submit(sleeper,2)

    # print(f1.result())
    # print(f2.result())


    #? Looping
    # secs = [5,4,3,2,1]
    # results = [excutor.submit(sleeper,sec) for sec in secs]

    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())

    #? Mapping
    secs = [5,4,3,2,1]
    results = excutor.map(sleeper,secs)

    for result in results:
        print(result)

end = time.perf_counter()

print(f'Finished in {round(end-start,2)} Seconds.')

