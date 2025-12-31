#Write a python program to find frequency of each digit in a given integer

n = int(input("Enter the number: "))
temp = n

while temp > 0:
    digit = temp % 10
    count = 0
    temp2 = n

    while temp2 > 0:
        if temp2 % 10 == digit:
            count += 1
        temp2 //= 10

    print(f"The frequency of {digit} is {count}")
    temp //= 10

