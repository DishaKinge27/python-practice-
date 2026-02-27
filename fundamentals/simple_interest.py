# Simple Interest Calculator 
p= float(input("Enter the principal amount: "))
r= float(input("Enter Rate of interest: "))
n= float(input("Enter the time period: "))
simp_int=(p*r*n)/100
print("Simple interest: ",simp_int)
print("Total amount: ",p+simp_int)
#in this code, we converted all the variables into float datatype to perform further arithmetic operations 
