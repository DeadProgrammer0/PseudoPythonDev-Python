
inp = input('\nEnter your Birth Year or Age : ')
Current_year = 2020
Minimum_year = Current_year - 100

while True:
    if inp.isnumeric() == False or inp == '0':
        print('Invalid Input!')
        inp = input('\nEnter your age : ')

    if inp.isnumeric() == True:
        Age = int(inp)
        if len(inp) > 4:
            print('Please enter a valid Age or Birth Year. Input should be 4 digits or less.')
            inp = input('\nEnter your age : ')
            continue
        if len(inp) <= 2 and len(inp) != 0:
            Age = (Current_year - Age)

        if Age > Current_year:
            print('You are not born yet!')
            break
        if Age < Minimum_year:
            print('Seems like you are the oldest person alive...')
            break
        if Age > Minimum_year and Age < Current_year:
            Age_100 = Age + 100
            print(f'Your Age is {Current_year-Age} in {Current_year} and You\'ll be 100 years old in {Age_100}')
            break
