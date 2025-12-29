#Write a python program to count number of digits in a number
n = int(input("Enter the number: "))
digit = 0
while n>0:
    digit = digit+1
    n//=10
print(f"The number of digits in the number is {digit}")