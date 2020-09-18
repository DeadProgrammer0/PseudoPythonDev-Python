# Requirements.

import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import time 
from datetime import datetime,timedelta
import threading
from pygame import mixer


# Main code.

if __name__ == "__main__":
    
    # Variables
    number_of_drinks = 10 # 350 ml Glass
    water_int = 2880
    eyes_int = 1800
    physical_int = 2700
    status = 0
    water_mp3 = "water.mp3"
    eyes_mp3 = "eyes.mp3"
    physical_mp3 = "physical.mp3"
    water_input = 0
    eyes_input = 0
    physical_input = 0


    # Function to get time.
    def gettime():
        return datetime.now().strftime("%d %b 20%y %H:%M %p")

    # Function to get Input.
    def inputs(n):
        global water_input
        global eyes_input 
        global physical_input

        if n == "water":
            water_input = input("\n-------------------------------------------\nTime to Drink some Water.\nIf you drank water please enter \"Done\" to log the details.\nEnter Here : ").lower()
        if n == "eyes":
            eyes_input = input("\n-------------------------------------------\nTime to do some Eye Exercise.\nIf you did Eye Execise enter \"Done\" to log the details.\nEnter Here : ").lower()
        if n == "physical":
            physical_input = input("\n-------------------------------------------\nTime to do some Exercise.\nIf you did Execise enter \"Done\" to log the details.\nEnter Here : ").lower()

#---------------------------------------------------------------------------------------------------------------------

    def main():


        mixer.init()

#-----------------------------------------------------DRINK-WATER------------------------------------------------------------

        def water():
            global status
            global number_of_drinks

            if status == "running":
                time.sleep(60)
                water()

            else:
                if number_of_drinks > 0:    
                    status = "running"

                    mixer.music.load(water_mp3)
                    mixer.music.play(loops=-1)
                    threading.Timer(water_int,water).start()


                    inputs("water")

                    while water_input != "done":
                        if water_input != "done":
                            print("Oops! Wrong Input. Try again.")
                            inputs("water")
                        

                    if water_input == "done":
                        mixer.music.stop()
                        with open("Healthy_Programmer.txt","a") as f:
                            f.write(f"\n-------------------------------------------\nDrank water at {gettime()}.\n-------------------------------------------\n")

                
                    status = 0
                    number_of_drinks -= 1

                    
            
                elif number_of_drinks == 0:
                    exit()
            
#-----------------------------------------------------EYES-EXERCISE-------------------------------------------------------

        def eyes():
            global status

            if status == "running":
                time.sleep(60)
                eyes()

            else:
                if status == 0:    
                    status = "running"

                    mixer.music.load(eyes_mp3)
                    mixer.music.play(loops=-1)
                    threading.Timer(eyes_int,eyes).start()


                    inputs("eyes")

                    while eyes_input != "done":
                        if eyes_input != "done":
                            print("Oops! Wrong Input. Try again.")
                            inputs("eyes")
                        

                    if eyes_input == "done":
                        mixer.music.stop()
                        with open("Healthy_Programmer.txt","a") as f:
                            f.write(f"\n-------------------------------------------\nDid Eye Exercise at {gettime()}.\n-------------------------------------------\n")

                
                    status = 0
            
#----------------------------------------------------PHYSICAL-EXERCISE----------------------------------------------------                

        def physical():
            global status

            if status == "running":
                time.sleep(60)
                physical()

            else:
                if status == 0:    
                    status = "running"

                    mixer.music.load(physical_mp3)
                    mixer.music.play(loops=-1)
                    threading.Timer(physical_int,physical).start()


                    inputs("physical")

                    while physical_input != "done":
                        if physical_input != "done":
                            print("Oops! Wrong Input. Try again.")
                            inputs("physical")
                        

                    if physical_input == "done":
                        mixer.music.stop()
                        with open("Healthy_Programmer.txt","a") as f:
                            f.write(f"\n-------------------------------------------\nDid Exercise at {gettime()}.\n-------------------------------------------\n")

                
                    status = 0
            
#---------------------------------------------------------------------------------------------------------------------

        temp = 1        
        while temp == 1:
            ct = (datetime.now()).strftime("%H:%M")

            if ct > "09:00" and ct < "17:00":
                print("Started...")
                time.sleep(eyes_int) 
                eyes()
                time.sleep(900)
                physical()
                time.sleep(180)
                water()
                temp -= 1

    main()


#------------------------------------------------------END------------------------------------------------------------
    
    