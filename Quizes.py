# Quiz 1 : Create a program that takes two numbers as input from the user and then prints the sum of these numbers.
# Solution in #4.


# Quiz 2 : Create a program that takes a test for Driving Lincence.
# The participant should be above 18 and Below 75 to get the Licence if he is still 18 then ask him to give a physical Driving test.
# Solution in #9.


# Quiz 3 : Create a program which filters a list containing varios Datatypes and only prints Integers which are greater than 6.
# By using For Loop.
# Solution in #10.


# Quiz 4 : Create a program which takes Input from user and asks to enter a Number greater than 100.
# Untill the user doesn't enter a number greater than 100 program continues.
# Solution in #13. 


# Quiz 5 : Create a program which takes Input from user and asks for to enter A number then create a function that 
# Generates Fibunacci sequence and give the Fibunacci for the the numbers which was taken from user earlier.
# Solution in #23.



import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import time
from datetime import datetime,timedelta
from pygame import mixer
from multiprocessing import Process
import sys

import threading

eyes1 = 60
pe1 = 120

ct = 0


    

water_time = []
eyes_time = []
pe_time = []


# def timepass():
#     global water_time
#     global eyes_time
#     global pe_time


#     t3 = datetime(year=2020,month=9,day=11,hour=9,minute=10)

#     for i in range(1,19 ):
#         m3 = 20 * i
#         h3 = timedelta(minutes=m3,seconds=1)
#         f3 = (t3 + h3).strftime("%H:%M:%S")
#         water_time.append(f3)
        

#     t = datetime(year=2020,month=9,day=11,hour=9)


    

#     for i in range(1,17):
#         m1 = 30*i
#         h = timedelta(minutes=m1,seconds=1)
#         f = (t + h).strftime("%H:%M:%S")
#         eyes_time.append(f)


    
#     t2 = datetime(year=2020,month=9,day=11,hour=9)

#     for i in range(1,11):
#         m2 = 45 * i
#         h2 = timedelta(minutes=m2,seconds=1)
#         f2 = (t2 + h2).strftime("%H:%M:%S")
#         pe_time.append(f2)


def timepass():
    global water_time
    global eyes_time
    global pe_time


    t = datetime.time()

    for i in range(1,24 ):
        m3 = 20 * i
        h3 = timedelta(minutes=m3,seconds=1)
        f = (t + h3).strftime("%H:%M")
        print(f)
        water_time.append(f)
        


    print('-----------------------------------------------')

    

    for i in range(1,17):
        m1 = 3*i
        h = timedelta(minutes=m1,seconds=1)
        f = (t + h).strftime("%H:%M")
        print(f)
        eyes_time.append(f)


    print('---------------------------------------------------------')


    for i in range(1,11):
        m2 = 6 * i
        h2 = timedelta(minutes=m2,seconds=1)
        f = (t + h2).strftime("%H:%M")
        print(f)
        pe_time.append(f)



timepass()

def gettime():
        return datetime.now()  



mixer.init()

# while True:
#     ctime = time.strftime("%H:%M:%S")



                    
#     watertime = ["19:23","22:39:40"] 
#     if ctime in watertime:
#         mixer.music.load("water.mp3")
#         mixer.music.play(loops=-1)


#         i = input("Water Here : ")
#         if i == "done":
#             mixer.music.stop()
#             with open("Healthy Programmer.txt","a") as f:
#                 f.write(f"\nDrank water at [{gettime()}].")

                        
def eyes():
    global eyes1
    print(datetime.now())    
    mixer.music.load("eyes.mp3")
    mixer.music.play(loops=-1)

    threading.Timer(eyes1,eyes).start()

    i2 = input("Eyes Here : ")
    if i2 == "done":
        mixer.music.stop()
        with open("Healthy Programmer.txt","a") as f1:
            f1.write(f"Did Eye Exercise at [{gettime()}].")
        

                
def pe():
    global pe1
    print(datetime.now())
    mixer.music.load("physical.mp3")
    mixer.music.play(loops=-1)
    threading.Timer(pe1,pe).start()  

    i3 = input("PE Here : ")
    if i3 == "done":
        mixer.music.stop()
        with open("Healthy Programmer.txt","a") as f2:
            f2.write(f"Did Physical Exercise at [{gettime()}].")



        
# while True:  
#     ct = (datetime.now()).strftime("%H:%M:%S")


#     time.sleep(eyes1)
#     eyes()
#     if ct in eyes_time and ct in pe_time:
#         time.sleep(60)
#         time.sleep(eyes1)
#         pe()
#     else:
#         time.sleep(eyes1)
#         pe()
        




# while True:
#     ct1 = time.strftime("%H:%M:%S")

#     if ct1 == "17:35:00":
#         main()
#         break

# l1 = []

# while True:
#     ct = (datetime.now()).strftime("%H:%M:%S")



#     if ct == "18:12:35":
#         h = (datetime.now() + timedelta(minutes=30)).strftime("%H:%M:%S")
#         l1.append(h)
#         print(l1)
#         break


