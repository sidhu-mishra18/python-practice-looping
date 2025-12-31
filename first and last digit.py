#Write a python program to find first and last digit of a number
n = int(input("Enter the number: "))
ld =0
fd =0
ld = n%10
while n>9:
    n//=10
fd = n
print(f"The last digit is {ld}")
print(f"The first digit is {fd}")