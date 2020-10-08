# Health Managment program.


def main():

    import time
    import datetime


    def sub_main3log():
        """For Loging."""
        log = input("Enter Your Log here : ")
        with open(f"{ab}{op}.txt","a") as f:
            f.write(f"\n----------------------------------------------------\nDate and Time - [{t}]\nParticipant's Name - {ab}\n{a1} - {log}\n----------------------------------------------------\n")

    def sub_main3ret():
        """For Retrieving."""
        with open(f"{ab}{op}.txt") as f:
            print(f.read())

    def getdate():
        """For noting the time in the file."""
        return datetime.datetime.now()
    t = getdate()

    dc = {"1":"Harry","2":"Rohan","3":"Hamad"}

    def name():
        """Prints Contestent's names"""
        print("\nName of the current Participants are :-\n")
        for key,value in dc.items():
            time.sleep(0.5)
            print(f"{key}. {value}")

    def the_main_p():

        em = [".quit",".start",".info",".help"]

        print("\nThis is a Health Managment Program Enter .start to Run the main program.\n.quit to Quit program, can't be quited after .start.\nEnter .info to know more.\nEnter .help to know all commands to use this program.")
        mai_n = input()

        if mai_n == ".help":
            print("\nThese are all commands to use this program.\n\nEnter .start to start the full program.\nEnter .name for Participant's names.\nEnter .log to Log data.\nEnter .retrieve to Retrieve data.\nEnter .food for Diet.\nEnter .execercise for Exercise.")
            the_main_p()

        elif mai_n == ".info":
            print("\nThis program is built for a group of Friends who are currently on a Gym Training.\nThis program helps them to keep track of the data i.e. what they ate and which exercises the did.\nThis program takes input and adds the data to the respective file to the participant.\nAnd also Retrieves the Data to show. ")
            the_main_p()

        elif mai_n == ".start":
            print("Starting the Main Program.",end="")
            time.sleep(0.5)
            print(".",end="")
            time.sleep(0.5)
            print(".",end="")
            time.sleep(0.5)
            print(".",end="")
            time.sleep(0.5)
            print(".",end="")
            time.sleep(0.5)
            print(".",end="")
            time.sleep(0.5)
            print(".",end="")
            time.sleep(0.5)
            print(".",)
        
        elif mai_n == ".quit":
            exit()

        else:
            print("Invalid Input")
            the_main_p()

        def sub_main2():
            """Takes Input for Name."""
            global name1
            name1 = input("\nPlease Enter the Serial Number of the Name.\nUse .name command to know all the names.\nEnter here : ")

            if name1 == ".name":
                name()
                sub_main2()
            
            elif name1 not in dc:
                print("This Name is not in the list. Please Enter a valid name.")
                sub_main2()
            
            elif name1 in dc:
                global ab
                ab = dc[name1]
                print(f"You choosed {ab}.")

            else:
                print("Oops! Something went wrong.")
                sub_main2()

    

        def sub_main3():
            """Asks What user wants to do."""

            work = input("\nWhat you want to do\n.log to Log Data\n.retrieve to Retrieve Data.\nEnter Here : ")

            commands = [".log",".retrieve"]

            if work not in commands:
                print("Please use a Valid Command.")
                sub_main3()

                    
            def sub_main3bran():

                if work in commands:
                    if work == ".log":
                        
                        print("Enter .food to Log Food.\nEnter .exercise to Log Exercise.")
                        global ps 
                        ps = [".food",".exercise"]
                        global op 
                        op = input("Enter Here : ")
                        global a1
                        if op not in ps:
                            print("Please use a Valid Command.")
                            sub_main3bran()

                        elif op == ".food":
                            a1 = "Food"
                        elif op == ".exercise":
                            a1 = "Exercise"
                        sub_main3log()
                    
                    
                    if work == ".retrieve":
                        print("Enter .food to Retrieve Food.\nEnter .exercise to Retrieve Exercise.")
                        op = input("Enter Here : ")
                        ps = [".food",".exercise"]
                        if op not in ps:
                            print("Please use a Valid Command.")
                            sub_main3bran()
                        sub_main3ret()
            sub_main3bran()
        sub_main2()
        sub_main3()
    the_main_p()





 
    

    def rep():
        """Asks Whether to repeat the program or exit."""
        yeslist = ["yes" , "y"]
        repeat = input("\nEnter \"yes\" \'y\' to repeat the program.\n").lower()
        if repeat in yeslist:
            main() 
        else:
            print("Thanks for using the Program.")
            exit()
        
    rep()
 
main()