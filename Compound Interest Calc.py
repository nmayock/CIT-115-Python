#Author: Noah Mayock
#Assignmmnet: Compound Interest

#input

fPV = float(input("Enter the starting principal: "))
fR = float(input("Enter the annual interest rate: ")) /100
fM = float(input("How many times per year is the interest compounded: "))
fTy = float(input("For how many years will the account earn interest: "))

#Compute

fMTy = fM * fTy
fFutVal = fPV * (1 + (fR / fM)) ** fMTy

#Output

print("At the end of", fTy, " years you will have $", format(fFutVal, ",.2f"))
