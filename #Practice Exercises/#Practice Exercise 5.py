def Next_value(num):
    int_num = num
    num = str(num)
    reverse = int(num[::-1])

    while int_num != reverse:
        int_num += 1
        num = str(int_num)
        reverse = int(num[::-1])
        if int_num == reverse:
            break

    if int_num == reverse:
        return int_num

if __name__ == "__main__":
    mylist = []
    nextlist = []
    while True:
        try:
            inp_range = int(input('Enter the number of values you want to enter : '))
            for i in range(inp_range):
                mylist.append(int(input(f"Enter the value here : ")))

        except Exception as e:
            print('Please enter Integers only!')
            continue
        else:
            print('Input is taken successfully!\n')

            for i in mylist:
                nextlist.append(Next_value(i))
            
            print(f'Entered list was {mylist} and Next value list is {nextlist}.')
            break