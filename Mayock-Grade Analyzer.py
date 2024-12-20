#Author: Noah Mayock
#Assignment: Grade Analyser

#inputs

strName = input("Name of the person we are calculatinig grades for: ")

intScoreOne = int(input ("Test 1: "))
intScoreTwo = int(input ("Test 2: "))
intScoreThree = int(input ("Test 3: "))
intScoreFour = int(input ("Test 4: "))

if intScoreOne < 0 or intScoreTwo < 0 or intScoreThree < 0 or intScoreFour < 0:
    print("Test scores must be greater than 0.")
    exit()

strDrop = input("Do you wish to Drop the Lowest Grade Y or N? ")

#Calculations:

if strDrop == "N":
    fAvg = float((intScoreOne + intScoreTwo + intScoreThree + intScoreFour) / 4)
    print(strName, "test average is: ", format(fAvg, ".1f"))
elif strDrop == "Y":
    if intScoreOne < intScoreTwo:
        intLow = intScoreOne
    else:
        intLow = intScoreTwo
    if intScoreThree < intLow:
        intLow = intScoreThree
    if intScoreFour < intLow:
        intLow = intScoreFour
    fAvg = float(((intScoreOne + intScoreTwo + intScoreThree + intScoreFour) - intLow) / 3)
    print(strName, "test average is: ", format(fAvg, ".1f"))
else:
    print("Enter an Y or N to Drop the Lowest Grade.")
    exit()

#Letter grade if/elif/else

if fAvg >= 97.0:
    strLGrade = "A+"
elif fAvg < 97.0 and fAvg >= 94.0:
    strLGrade = "A"
elif fAvg <= 93.9 and fAvg >= 90.0:
    strLGrade = "A-"
elif fAvg <= 89.9 and fAvg >= 87.0:
    strLGrade = "B+"
elif fAvg <= 86.9 and fAvg >= 84.0:
    strLGrade = "B"
elif fAvg <= 83.9 and fAvg >= 80.0:
    strLGrade = "B-"
elif fAvg <= 79.9 and fAvg >= 77.0:
    strLGrade = "C+"
elif fAvg <= 76.9 and fAvg >= 74.0:
    strLGrade = "C"
elif fAvg <= 73.9 and fAvg >= 70.0:
    strLGrade = "C-"
elif fAvg <= 69.9 and fAvg >= 67.0:
    strLGrade = "D+"
elif fAvg <= 66.9 and fAvg >= 64.0:
    strLGrade = "D"
elif fAvg <= 63.9 and fAvg >= 60.0:
    strLGrade = "D-"
else:
    strLGrade = "F"
print("Letter Grade for the test is:", strLGrade)
