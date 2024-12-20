#Author: Noah Mayock
#Assignment: Compound Interest with loops

#Input

fDeposit = 0
while fDeposit <= 0:
    try:
        fDeposit = float(input("What is the orginal deposit (positive value): "))
        if fDeposit <= 0:
            print("Input must be a positive numeric value")
    except ValueError:
            print("Input must be a positive numeric value")
fIntR = 0
while fIntR <= 0:
    try:
        fIntR = float(input("What is the Interest Rate (positive value): ")) / 100
        if fIntR <= 0:
            print("Input must be a positive numeric value")
    except ValueError:
        print("Input must be a positive numeric value")
iMonths = 0
while iMonths <= 0:
    try:
        iMonths = int(input("What is the Number of Months (positive value): "))
        if iMonths <= 0:
            print("Input must be a positive numeric value")
    except ValueError:
        print("Input must be a positive numeric value")
fGoal = -1
while fGoal <= -1:
    try:
        fGoal = float(input("What it the Goal Amount (can enter 0 but not negative): "))
        if fGoal < 0:
            print("Input must be 0 or greater")
    except ValueError:
        print("Input must be 0 or greater")


#calculations:

fMonthlyRate = fIntR / 12
for iMonths in range(iMonths):
    iMonths += 1
    fAccBal = fDeposit * (1 + fMonthlyRate) ** iMonths
    print("Month: ",iMonths,"Account Balance is: $",format(fAccBal, ",.2f"))
if fGoal > 0:
    iTotalMonths = 0
    fAccBal = fDeposit
    while fAccBal < fGoal:
        fAccBal += fAccBal * fMonthlyRate
        iTotalMonths += 1
    print("It will take", iTotalMonths, "months to reach the goal of $", format(fGoal, ",.2F"))
   
    
