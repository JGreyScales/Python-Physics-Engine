while True:
    try:

        base = int(input('What is the base number?:\t\t'))
        target = int(input('What is the target?:\t\t'))

        if base <= 0 or target < base:
            print('please have base greater than one and target greater than base')
            continue

        break

    except:
        print('please only enter floats')
        continue

for i in range((target * 100) + 1):

    if round(base**(i / 100)) == target:
        print((i + 1) / 100)
        break
else:
    print('that value cannot be logged up to 2 decimal places')