#Author: Noah Mayock
#Asssignment: Code Temperature Converter
#credit to SI Joseph Harris for helping correct some issues

#Welcome message:

print("Noah Mayock's Temp Converter:\n ")

#inputs:

fTemp = float(input ("Enter a Temperature: "))
strTempType = input ("Is the temp F for Fahrenheit or C for Celsius? ")

#Calculations to convert to Celsius:

if strTempType == "F" or strTempType == "f":
    if fTemp <= 212.0:
        fTempC = (5.0 / 9.0) * (fTemp - 32.0)
        print("The Celsius Equivalent is: ", format(fTempC, ".1f"))
    else:
        print("Temp cannot be > 212")

#Calulations to convert to fahrenheit:

elif strTempType == "C" or strTempType == "c":
    if fTemp <= 100.0:
        fTempF = ((9.0 / 5.0) * fTemp) + 32.0
        print("The Fahrenheit Equivalent is: ", format(fTempF, ".1f"))
    else:
        print("Temp cannot be > 100")
        
else:
    print("Enter an F or C")
