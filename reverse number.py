#Write a python program to enter a number and print its reverse
n = int(input("Enter the numbe: "))
temp = n
digit = 0
rev_num = 0
while n>0:
    digit +=1
    n=n//10
i=0
while temp >0:
    i +=1
    rev_num += (temp%10)*(10**(digit-i))
    temp = temp//10
print(f"The reversed version of number is: {rev_num}")