import random

if __name__ == "__main__":
    while True:
        try:
            a = int(input('\nEnter the Minimum Nuber : '))
            b = int(input('Enter the Maximum Nuber : '))
        except Exception as e:
            print("Please enter Integers only!")
            continue
        else:
            if a > b:
                print('\nMinimum number can\'t be greater than Maximum number!')
                print('Try again...')
                continue
            else:
                Player_1 = 0
                Player_2 = 0
                chance = 0
                Player_num = None

                def Main(Player_num_f):
                    random_num = random.randrange(a,b+1)
                    global Player_1
                    global Player_2
                    global chance
                    global Player_num
                    chance = 0

                    print(f'\n{Player_num_f}\'s turn!')
                    while True:
                        try:
                            guess = int(input('\nEnter your Guess : '))
                            chance += 1
                        except Exception as e:
                            print('Enter a Integer!')
                        else:
                            if guess > random_num:
                                print('Your guess is greater.')
                            elif guess < random_num:
                                print('Your guess is lesser.')
                            elif guess == random_num:
                                print(f'Congrats You guessed the number in {chance} Chance.')                      
                                break
                            else:
                                print('Something went wrong. Exiting...')
                                break
                    if Player_num_f == 'Player1':
                        Player_num = 'Player1'     
                    elif Player_num_f == 'Player2':
                        Player_num == 'Player2' 


                Main('Player1')
                Player_1 = chance
                Main('Player2')
                Player_2 = chance                
                
                if Player_1 < Player_2:
                    print(f'Player1 Won!!. Took {Player_1} chance/s.')
                elif Player_1 > Player_2:
                    print(f'Player2 Won!!. Took {Player_2} chance/s.')
                elif Player_1 == Player_2:
                    print('Match Draw!!')

                break