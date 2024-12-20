# Author: Noah Mayock
# Assignment: Code Inter Planetary Weights

#inputs

sName = input("What is your name? ")
fWeight = float(input("What is your body weight? "))

#Named constants

MERCURY_SGFACTOR = 0.39
VENUS_SGFACTOR = 0.91
MOON_SGFACTOR = 0.165
MARS_SGFACTOR = 0.38
JUPITER_SGFACTOR = 2.34
SATURN_SGFACTOR = 0.93
URANUS_SGFACTOR = 0.92
NEPTUNE_SGFACTOR = 1.12
PLUTO_SGFACTOR = 0.066

#Calculations

wMerc = fWeight * MERCURY_SGFACTOR
wVenu = fWeight * VENUS_SGFACTOR
wMoon = fWeight * MOON_SGFACTOR
wMars = fWeight * MARS_SGFACTOR
wJupi = fWeight * JUPITER_SGFACTOR
wSatu = fWeight * SATURN_SGFACTOR
wUran = fWeight * URANUS_SGFACTOR
wNept = fWeight * NEPTUNE_SGFACTOR
wPlut = fWeight * PLUTO_SGFACTOR

#Output

print(sName,"Your weights on different planets in the solar system are: ")

print( '{:20}'.format ("Weight on Mercury:"), format(wMerc, "15,.3f"))
print( '{:20}'.format ("Weight on Venus:"), format(wVenu, "15,.3f"))
print( '{:20}'.format ("Weight on Moon:"), format(wMoon, "15,.3f"))
print( '{:20}'.format ("Weight on Mars:"), format(wMars, "15,.3f"))
print( '{:20}'.format ("Weight on Jupiter:"), format(wJupi, "15,.3f"))
print( '{:20}'.format ("Weight on Saturn:"), format(wSatu, "15,.3f"))
print( '{:20}'.format ("Weight on Uranus:"), format(wUran, "15,.3f"))
print( '{:20}'.format ("Weight on Neptune:"), format(wNept, "15,.3f"))
print( '{:20}'.format ("Weight on Pluto:"), format(wPlut, "15,.3f"))
