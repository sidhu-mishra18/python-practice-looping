#Write a python program to check whether a number is palindrome or not

n = int(input("Enter the number: "))
temp = n
rev = 0
while n>0:
    rev = rev*10+ n%10
    n //=10
if temp == rev:
    print(f"The given number {temp} is a palindrome.")
else:
    print(f"The given number {temp} is not a palindrome.")