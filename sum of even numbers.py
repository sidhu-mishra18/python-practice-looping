#Write a python program to find sum of all even numbers between 1 to n.
n = int(input("Enter the value of n: "))
sum = 0
for i in range(0,n+1,2):
    sum += i
print(sum)