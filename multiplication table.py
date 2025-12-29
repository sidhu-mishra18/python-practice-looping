#Write a python program to print multiplication table of any number
n = int(input("Enter the number: "))
print(f"The table of {n} is: ")
for i in range(1,11):
    print(n*i)
