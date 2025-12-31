#Write a python program to calculate product of digits of a number
a = int(input("Enter the number: "))
prod = 1
while a>0:
    prod *=a%10
    a = a//10
print(f"The product of the digits of number is {prod}")