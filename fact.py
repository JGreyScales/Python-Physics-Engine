# while user input less than 1 and user input less then 99999 because 99999 is right on the verge of taking more then 3 seconds to compute on my PC 
# (you could go higher however it would be too slow)
user_input = 0
while user_input < 1:
    try:
        user_input = int(input('Please type and int:\t\t'))
        if user_input > 99999:
            user_input = 0
    except:
        print('please use an interger')
        continue

# for x in range (input - 1) since we wont be doing input x input at any point
for x in range(user_input - 1):
    # counter times equal to int(x) + 1 to make up for the start at 0 method of computer counting
    user_input *= x + 1
    print(user_input)