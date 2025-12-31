#Write a python program to enter a number and print it in words

n = int(input("Enter the number: "))
digit = 0
rev = 0
while n>0:
    rev = rev*10+n%10
    n//=10
while rev>0:
    digit = rev%10
    if digit == 0:
        print("Zero ", end='')
    elif digit == 1:
        print("One ", end='')
    elif digit == 2:
        print("Two ", end='')
    elif digit == 3:
        print("Three ", end='')
    elif digit == 4:
        print("Four ", end='')
    elif digit == 5:
        print("Five ", end='')
    elif digit == 6:
        print("Six ", end='')
    elif digit == 7:
        print("Seven ", end='')
    elif digit == 8:
        print("Eight ", end='')
    elif digit == 9:
        print("Nine ", end='')
    rev//=10