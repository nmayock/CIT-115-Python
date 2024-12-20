#Author: Noah Mayock
#Assignmnet: Paint Job with functions and file output

import math

#input function:

def getFloatInput(sPrompt):
    while True: 
        try:
            fValue = float(input(sPrompt))
            if fValue <= 0:
                print("Input mmust be a positive numeric value")
            else:
                return fValue
        except ValueError:
            print("Input must be a positive numeric value")
    
        
#calc functions:

def getGallonsOfPaint(fSquareFt, fFeetPerGal):
    return int(math.ceil(fSquareFt / fFeetPerGal))

def getLaborHours(fLabPerGal, iTotalGal):
    return (fLabPerGal * iTotalGal)

def getLaborCost(fLaborHours, fHourlyRate):
    return (fLaborHours * fHourlyRate)

def getPaintCost(iTotalGal, fPaintPrice):
    return (iTotalGal * fPaintPrice)

def getSalesTax(sState):
    if sState == "CT":
        return .06
    elif sState== "MA":
        return .0625
    elif sState== "ME":
        return .085
    elif sState == "RI":
        return .07
    elif sState== "VT":
        return .06
    else:
        return .0
def showCostEstimate(iTotalGal, fLaborHours, fPaintCost, fLaborCost, fSalesTax, sLastName):
    fTotalLaborCost = (fLaborCost * iTotalGal)
    fTax = ((fTotalLaborCost + fPaintCost) * fSalesTax)
    fTotalCost = fTax + fPaintCost + fTotalLaborCost
    print(f"Gallons of Paint: {iTotalGal}")
    print(f"Hours of Labor: {fLaborHours:,.1F}")
    print(f"Paint Charges: ${fPaintCost:,.2F}")
    print(f"Labor Charges: ${fTotalLaborCost:,.2F}")
    print(f"Tax: ${fTax:,.2F}")
    print(f"Total cost: ${fTotalCost:,.2F}")

    #File Creation:
    with open(f"{sLastName}_PaintJobOutput.txt","w") as PaintCalc1:
        PaintCalc1.write(f"Gallons of Paint: {iTotalGal}\n")       
        PaintCalc1.write(f"Hours of Labor: {fLaborHours:,.1F}\n")
        PaintCalc1.write(f"Paint Charges: ${fPaintCost:,.2F}\n")
        PaintCalc1.write(f"Labor Charges: ${fTotalLaborCost:,.2F}\n")
        PaintCalc1.write(f"Tax: ${fTax:,.2F}\n")
        PaintCalc1.write(f"Total cost: ${fTotalCost:,.2F}\n")
                         
                         
    print(f"{sLastName}_PaintJobOutput.txt was created")

    
#main function:

def main():
    fSquareFt = getFloatInput("Enter wall space in square feet: ")
    fPaintPrice = getFloatInput("Enter paint price per gallon: ")
    fFeetPerGal = getFloatInput("Enter feet per gallon: ")
    fLabPerGal = getFloatInput("How many labor hours per gallon: ")
    fHourlyRate = getFloatInput("Labor charge per hour: ")
    sState = input("State job is in: ")
    sLastName = input("Customer Last Name: ")
    iTotalGal = getGallonsOfPaint(fSquareFt, fFeetPerGal)
    fLaborHours = getLaborHours(fLabPerGal, iTotalGal)
    fLaborCost = getLaborCost(fLaborHours, fHourlyRate)
    fPaintCost = getPaintCost(iTotalGal, fPaintPrice)
    fSalesTax = getSalesTax(sState)
    showCostEstimate(iTotalGal,
                     getLaborHours(fLabPerGal, iTotalGal),
                     getPaintCost(iTotalGal, fPaintPrice),
                     getLaborCost(fLabPerGal, fHourlyRate),
                     getSalesTax(sState),
                     sLastName)

main()
