#Author: Noah Mayock
#Assignment: Lists and Real Estate Analyzer

#input converter and data validation

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

#Median function

def getMedian(fValListSort):
    if (len(fValListSort) % 2) == 1:
        index = len(fValListSort) // 2
        return fValListSort[index]
    else:
        index = len(fValListSort) // 2
        fMiddleOne = fValListSort[index]
        fMiddleTwo = fValListSort[index -1]
        return ((fMiddleOne + fMiddleTwo) / 2)

#Main Logic   

def main():
    fValueList = []
    while True:
        fPropValue = getFloatInput("Enter property sales value: ")
        fValueList.append(fPropValue)
        sContinue = input("Enter another value Y or N: ")
        while sContinue.lower() not in ['y', 'n']:
            sContinue = input("Enter another value Y or N: ")
        if sContinue.lower() == 'n':
            break
        
    fValListSort = sorted(fValueList)
    fMedian = getMedian(fValListSort)
    fMin = min(fValListSort)
    fMax = max(fValListSort)
    fTotal = sum(fValListSort)
    fAvg = fTotal / (len(fValListSort))
    fCommission = fTotal * .03
    
    #Output
    for count, item in enumerate(fValListSort, start=1):
        print(f"Property {count} ${item:,.2F}")                
    print(f"Minimum: \t ${fMin:,.2F}")

    print(f"Maximum: \t ${fMax:,.2F}")

    print(f"Total: \t\t ${fTotal:,.2F}")

    print(f"Average: \t ${fAvg:,.2F}")
            
    print(f"Median: \t ${fMedian:,.2F}")

    print(f"Commission: \t ${fCommission:,.2F}")    
main()
