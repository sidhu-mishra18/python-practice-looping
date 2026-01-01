#Write a python program to find power of a number using for loop.

n = int(input("Enter the number: "))
p = int(input("Enter the power: "))
prod = 1
for i in range(1,p+1):
    prod *= n
print(f"The value of {n} to the power of {p} is {prod}")