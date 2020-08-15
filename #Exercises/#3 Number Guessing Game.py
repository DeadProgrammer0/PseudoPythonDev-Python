n = 18
num_of_guesses = 9
guesses_left = 9

while(1):
    
    guesses_left = guesses_left - 1

    ip = int(input("\nEnter Your Number : "))

    if ip == n:
        print("Congrats! You Guessed The Number.")
        print("Number Of Guesses You Took =",num_of_guesses - guesses_left)
        break

    if guesses_left == 0:
        print("Game Over! All your guesses was Wrong.")
        break
    
    elif ip > n:
        print("Your Number is Greater. Enter a Smaller Number.")
        print("Number of Guesses left =", guesses_left)
        continue

    elif ip < n:
        print("Your Number is Smaller. Enter a Greater Number.")
        print("Number of Guesses left =", guesses_left)
        continue

    else: 
        print("Error! Invalid Input")
        continue