x=input('Enter grade within the range 1.0 to 10.0: ')

try:
    grade=float(x)

    if grade>10.0:
        print('Enter valid grade within the range 1.0 to 10.0')
    elif grade>9.0:
        print('Excellent')
    elif grade>8.0:
        print('Very Good')
    elif grade>7.0:
        print('Good')
    elif grade>6.0:
        print('Fair')
    elif grade>5.0:
        print('Pass')
    else:
        print('Fail')

except:
    print('Invalid Input')
