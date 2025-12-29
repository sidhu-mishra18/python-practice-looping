#Compound intrest calculator in python
p = float(input("Enter the principle amount: "))
r = float(input("Enter the rate of intrest: "))
t = float(input("Enter the time period in years: "))

CI = p*pow((1+r/100),t) - p
print(f"Compound intrest is: {CI}")