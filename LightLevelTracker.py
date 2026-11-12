# Light Level Tracker

import random
import math

LightLevel = {
    "Radiant": 75,
    "Dim Light": 51,
    "Shadowy": 26,
    "Dark": 1,
    "Black As Pitch": 0
}

LightSources = {
    "torch",
    "lantern",
    "light cantrip",
    "daylight spell"
}


def TrackLightLevel():
    CurrentLightLevel = 100
    TimeElapsed = 0
    LightSourceUsed = input(f"Light Source: ").lower()
    while LightSourceUsed not in LightSources:
        LightSourceUsed = input(f"Invalid Light Source, pls choose a valid option: (HELP to see options) ").lower()
    else:
        print(f"Using {LightSourceUsed}... ")

        if LightSourceUsed == "torch":
            print(f"Torch Durability = 1 Hour")
            print(f"Light Level = Radiant")
            LightLevelMalice = input(int("Time Passed: "))
            CurrentLightLevel = 60 - LightLevelMalice
            print(CurrentLightLevel)
        
    

TrackLightLevel()   
