## Supplies Calculator V5
#Account for multiple different kinds of mounts on the same journey
#Account for their feeding requirements

import random
import math

# | --- Dictionary Zone --- |
CurrentJourneyState = {         
    "TotalHoursTraveled": 0,
    "TotalHoursElapsed": 0,
    "HoursSpentResting": 0,
    "HoursSpentCamping": 0,
    "HoursSinceRest": 0,
    "NumOfShortRests": 0,
    "ShortRestsSkipped": 0,
    "NextExhaustionCheck": 12,
    "CurrentExhaustionDC": 10,
    "TorchesUsed": 0,           
    "OilFlasksUsed": 0,
    "HerbsUsed":  0,             #For when the LIGHT cantrip is used as a LightSource
    "RationsConsumed": 0,        #To account for Rations consumed
    "FirewoodBurnt": 0,          #To account for number of Firewoods burnt during Short Rests
    "MilesTraveled": 0,
    "MilesRemaining": 0,       #Ensure that AI's code is updating this based off what the user inputs
    "CurrentLightSource": None,
    "LightSourceDurability": 0,        #How much burn time a given light source has left -- the "HP Bar" of a torch or oil flask
}

ValidConfirmationInputs = {
    "y",
    "yes",
}

ValidRejectionInputs = {
    "n",
    "no",
}

TravelPaceSpeeds = {                   #Each of these speeds are MPH
    "slow": 2,
    "normal": 3,
    "fast": 4,
    "camel (normal)": 5,
    "elephant (normal)": 4,
    "draft horse (normal)": 4,
    "riding horse (normal)": 6,
    "mastiff (normal)": 4,
    "mule (normal)": 3,
    "pony (normal)": 3,
    "war horse (normal)": 6,
    "phantom steed (normal)": 10,
    "draft horse (fast)": 7,
    "riding horse (fast)": 9,
    "war horse (fast)": 9,
    "phantom steed (fast)": 13,
    "camel (slow)": 3,
    "elephant (slow)": 2,
    "draft horse (slow)": 2,
    "riding horse (slow)": 4,
    "mastiff (slow)": 2,
    "mule (slow)": 1,
    "pony (slow)": 1,
    "war horse (slow)": 4,
    "phantom steed (slow)": 7,
    "help": 1
}

HelpMenu4TravelSpeeds = {
    "|-- Slow = 2mph --|",
    "|-- Normal = 3mph --|",
    "|-- Fast = 4mph --|"
}

HelpMenu4CamelTravelSpeeds = {
    "|-- Camel (Normal) = 5mph --|",
    "|-- Camel (Fast) = Unavailable --|",
    "|-- Camel (Slow) = 3mph --|"
}

HelpMenu4ElephantTravelSpeeds = {
    "|-- Elephant (Normal) = 4mph --|",
    "|-- Elephant (Fast) = Unavailable --|",
    "|-- Elephant (Slow) = 2mph --|"
}

HelpMenu4MastiffTravelSpeeds = {
    "|-- Mastiff (Normal) = 4mph --|",
    "|-- Mastiff (Fast) = Unavailable --|",
    "|-- Mastiff (Slow) = 2mph --|"
}

HelpMenu4MuleAndPonyTravelSpeeds = {
    "|-- Mule & Pony (Normal) = 4mph --|",
    "|-- Mastiff & Pony(Fast) = Unavailable --|",
    "|-- Mastiff & Pony(Slow) = 1mph --|"
}

HelpMenu4DraftHorseTravelSpeeds = {
    "|-- Draft Horse (Normal) = 4mph --|",
    "|-- Draft Horse(Fast) = 7mph --|",
    "|-- Draft Horse(Slow) = 2mph --|"
}

HelpMenu4RidingHorseTravelSpeeds = {
    "|-- Riding Horse (Normal) = 6mph --|",
    "|-- Riding Horse(Fast) = 9mph --|",
    "|-- Riding Horse(Slow) = 4mph --|"
}    

HelpMenu4WarHorseTravelSpeeds = {
    "|-- War Horse (Normal) = 6mph --|",
    "|-- War Horse(Fast) = 9mph --|",
    "|-- War Horse(Slow) = 4mph --|"
}    

HelpMenu4PhantomSteedTravelSpeeds = {
    "|-- Phantom Horse (Normal) = 6mph --|",
    "|-- Phantom Horse(Fast) = 9mph --|",
    "|-- Phantom Horse(Slow) = 4mph --|"
}    

LightSources = {
    "torch": 1,     #1 hour
    "light": 1,     #1 hour
    "lantern": 4    #4 hours
}

Characters = {}

ValidMountChoices = {
    "camel",
    "elephant",
    "draft horse",
    "riding horse",
    "mastiff",
    "mule",
    "pony",
    "warhorse",
    "phantom steed"
}

def GetJourneyInfo():
    print("")
    print("|----- JOURNEY Setup -----|")

    HexValue = float(input("How many miles does a single Hex represent?: "))                #Should always be a whole number, despite the code allowing it to be a float.
    TravelDistance = float(input("How many miles long will this journey be?: "))
    NumOfHexes = int(TravelDistance / HexValue)
    CurrentJourneyState["MilesRemaining"] = TravelDistance
    print("")
    print(f"Journey Length (Miles): {TravelDistance} miles.") 
    print(f"Journey Length (Hexes): {NumOfHexes} hexes.")

    #Accounting for each PC in The Party so that their Exhaustion LvL & CON Saving Throws vs
    #EXHAUSTION can be calc'd later.
    #Appends user input into a Dictionary containing each PC's name."
    print("")
    NumOfCharacters = int(input("How many Player Characters are in The Party?: "))
    for CharacterNum in range(1, NumOfCharacters + 1):
        CharacterName = input(f"Character #{CharacterNum} Name: ")
        Characters[CharacterName] = {"ExhaustionLevel": 0}          #I believe this is adding a Exhasution LvL tag to a character who was just added to the dictionary.    

    return NumOfHexes, TravelDistance, HexValue

#def ProcessCurrentHex(NumOfHexes, TravelDistance, HexValue, CurrentHex):   <-- save this just in case
def ProcessCurrentHex(CurrentHex, HexValue):

    MilesThisHex = min(HexValue, CurrentJourneyState["MilesRemaining"])
    
    print("")
    print(f"|----- Hex {CurrentHex} -----|")
    print(f"Distance Remaining for Overall Journey: {CurrentJourneyState['MilesRemaining']:.2f} miles")
    print(f"Distance Remaining for {CurrentHex}: {MilesThisHex:.2f} miles")

    #print("")
    #UsingAMount = input("Will The Party be using mounts?: (Y/N) ").lower()
    #if USingAMount in ValidConfirmationInputs:
    #    WhichMount2Use = input("Which mount will be used?: ").lower()
    #    while WhichMount2Use not in ValidMountChoices:
    #       print("")
    #       WhichMount2Use = input("Invalid Mount, please enter a valid mount: ").lower()
    #else:
        #print("No mounts used")
    print("")
    print(f"|-- Travel Pace Selection For {CurrentHex} --|")
    TravelPace = input("Select a Travel Pace: (or HELP to see options): ").lower()
    while TravelPace not in TravelPaceSpeeds:
        TravelPace = input("Invalid Travel Pace. Please enter one of the provided options: ").lower()
    while TravelPace == "help":
        print("")
        print("-- Humanoid Travel Speed Options --")
        print(HelpMenu4TravelSpeeds)
        print("")
        print("-- Camel Travel Speed Options --")
        print(HelpMenu4CamelTravelSpeeds)
        print("")
        print("-- Elephant Travel Speed Options --")
        print(HelpMenu4ElephantTravelSpeeds)
        print("")
        print("-- Mastiff Travel Speed Options --")
        print(HelpMenu4MastiffTravelSpeeds)
        print("")
        print("-- Mule & Pony Travel Speed Options --")
        print(HelpMenu4MuleAndPonyTravelSpeeds)
        print("")
        print("-- Draft Horse Travel Speed Options --")
        print(HelpMenu4DraftHorseTravelSpeeds)
        print("")
        print("-- Riding Horse Travel Speed Options --")
        print(HelpMenu4RidingHorseTravelSpeeds)
        print("")
        print("-- War Horse Travel Speed Options --")
        print(HelpMenu4WarHorseTravelSpeeds)
        print("")
        print("-- Phantom Steed Travel Speed Options --")
        print(HelpMenu4PhantomSteedTravelSpeeds)
        print("")
        TravelPace = input("Select a Travel Pace: ").lower()
        
    #Calculating how long it will take to travel thru current hex.
    TravelTime4Hex = (MilesThisHex / TravelPaceSpeeds[TravelPace])
    print("")
    print(f"At a {TravelPace} Travel Pace, it will take {TravelTime4Hex:.2f} hours to travel through this hex")

    #Establishing a "working copy" of the amt of time it takes to travel thru this hex
    RemainingTravelTime = TravelTime4Hex

    #Acquiring which Light Source is utilized for this hex
    while RemainingTravelTime > 0:
        if CurrentJourneyState["LightSourceDurability"] <= 0:
            LightSource2Use = input("For this hex, which Light Source will be utilized? (Torch, Lantern, or Light Cantrip): ").lower()
            while LightSource2Use not in LightSources:
                LightSource2Use = input("Invalid Light Source, please choose from one of the provided options.").lower()
                
            #Establishing a light source used for this trip, then pulling from
            #its correlated value in the above dictionary.
            CurrentJourneyState["CurrentLightSource"] = LightSource2Use
            CurrentJourneyState["LightSourceDurability"] = LightSources[LightSource2Use]

            #Logging consumed torch, oil flask, or herb for Light cantrip
            if LightSource2Use == "torch" or LightSource2Use == "Torch" or LightSource2Use == "TORCH":
                CurrentJourneyState["TorchesUsed"] += 1

            elif LightSource2Use == "lantern" or LightSource2Use == "Lantern" or LightSource2Use == "LANTERN":
                CurrentJourneyState["OilFlasksUsed"] += 1

            elif LightSource2Use == "light" or LightSource2Use == "Light" or LightSource2Use == "LIGHT":
                CurrentJourneyState["HerbsUsed"] += 1

        #From here, we check to see how close we are to the next req'd stopping point.
        HoursUntilRest = (CurrentJourneyState["NextExhaustionCheck"] - CurrentJourneyState["HoursSinceRest"])
        LightSourceDurability = CurrentJourneyState["LightSourceDurability"]

        TravelChunk = min(RemainingTravelTime, HoursUntilRest, LightSourceDurability)

        #Processing the actual travelling within the current hex
        MilesPerHour = TravelPaceSpeeds[TravelPace]
        MilesTraveledThisChunk = TravelChunk * MilesPerHour
        
        CurrentJourneyState["MilesTraveled"] += MilesTraveledThisChunk
        CurrentJourneyState["MilesRemaining"] -= MilesTraveledThisChunk       #I have no fucking clue what any of this is LOL
        CurrentJourneyState["TotalHoursTraveled"] += TravelChunk
        CurrentJourneyState["TotalHoursElapsed"] += TravelChunk
        CurrentJourneyState["HoursSinceRest"] += TravelChunk
        CurrentJourneyState["LightSourceDurability"] -= TravelChunk

        RemainingTravelTime -= TravelChunk

        #Handling a depleted light source
        if CurrentJourneyState["LightSourceDurability"] <= 0 and RemainingTravelTime > 0:
            print("")
            print(f"The {CurrentJourneyState['CurrentLightSource']} has burned out.")
            CurrentJourneyState["CurrentLightSource"] = None

        #Handling the End-of-Journey Summary
        elif CurrentJourneyState["MilesRemaining"] <= 0:
            print("")
            print("|----- Journey Complete! -----|")
            print(" --- Summary of Journey --- ")

            print(f"Total Time Elapsed: {CurrentJourneyState['TotalHoursTraveled']}")

            #Logs total amt of torches expended
            if CurrentJourneyState["TorchesUsed"] >= 1:                    
                print(f"Torches Used: {CurrentJourneyState['TorchesUsed']}")

            #Logs total amt of oil flasks expended
            if CurrentJourneyState["OilFlasksUsed"] >= 1:
                print(f"Oil Flasks Used: {CurrentJourneyState['OilFlasksUsed']}")

            #Logs total amt of herbs expended
            if CurrentJourneyState["HerbsUsed"] >= 1:
                print(f"Herbs Used: {CurrentJourneyState['HerbsUsed']}")
            
        

        #Handling a Short Rest
        while (CurrentJourneyState["HoursSinceRest"] >= CurrentJourneyState["NextExhaustionCheck"]):
            print("\n--- SHORT REST REQUIRED ---")
            print(f"The Party has traveled for {CurrentJourneyState['HoursSinceRest']} hours; therefore, camp must be established, lest The Party accrue Exhaustion penalties.")
            ShortRestChoice = input("Take a Short Rest?: (Y/N) ").lower()

            #Verifying user input for ShortRestChoice
            #while ShortRestChoice not in ["yes", "Yes", "YES", "y", "Y", "no", "No", "NO", "n", "N"]:
            while ShortRestChoice not in ValidConfirmationInputs or ShortRestChoice not in ValidRejectionInputs:
                
                ShortRestChoice = input("Invalid input, please choose from one of the provided options. ").lower()

            if ShortRestChoice in ["yes", "y", "Y", "Yes", "YES"]:
                print("The Party begins setting camp...")
                #Eventually, add a Random Encounter calcltn for Nighttime Ambush here -- AFTER setup phase!

                CurrentJourneyState["TotalHoursElapsed"] += 2   #Accounting for time to setup camp & perform Camping Skills
                CurrentJourneyState["HoursSpentCamping"] += 2   

                print("Camp setup completed.")
                print("The Party begins resting...")
                
                CurrentJourneyState["NumOfShortRests"] += 1     #Recording completed Short Rest
                CurrentJourneyState["HoursSpentResting"] += 8   
                CurrentJourneyState["TotalHoursElapsed"] += 8   #Recording time that passes during Short Rest

                print("The Party completes an 8hr Short Rest.")

                CurrentJourneyState["HoursSpentCamping"] += 2
                CurrentJourneyState["TotalHoursElapsed"] += 2   #Accounting for time to tear down camp & prepare to travel again
                CurrentJourneyState["HoursSinceRest"] = 0       #Resetting the Short Rest timer 
                CurrentJourneyState["NextExhaustionCheck"] = 12

                for Character in Characters:
                    Characters[Character]["ExhaustionLevel"] = 0     #Reducing EXHSTN LvL by 1 upon completed SHRT RST
                print("\nThe Party is fully rested!")

                break
            if ShortRestChoice in ["no", "n", "N", "No", "NO"]:

                CurrentJourneyState["ShortRestsSkipped"] += 1

                print("The Party trudges onwards...")

                #Collecting the INITAL Constitution Saving Throw vs Exhaustion from each character in The Party
                print("|--- Constitution Saving Throw vs Exhaustion Required ---|")
                print(f"Current Exhaustion DC: {CurrentJourneyState['CurrentExhaustionDC']}")

                for Character in Characters:
                    SavingThrowResult = int(input(f"Enter {Character}'s Saving Throw: "))

                    if SavingThrowResult < CurrentJourneyState["CurrentExhaustionDC"]:
                        Characters[Character]["ExhaustionLevel"] += 1

                        print(f"{Character} Failed, gains 1 Level of Exhaustion")
                        print(f"{Character} currently has {Characters[Character]['ExhaustionLevel']} Levels of Exhaustion")

                    else:
                        print(f"{Character} suceeds.")
                
                CurrentJourneyState["CurrentExhaustionDC"] += 1
                CurrentJourneyState["NextExhaustionCheck"] = (CurrentJourneyState["HoursSinceRest"] + 2)
                
                #Subsequent Exhaustion Checks
                while (CurrentJourneyState["HoursSinceRest"] >= CurrentJourneyState["NextExhaustionCheck"]):
                    print("|--- Constitution Saving Throw vs Exhaustion Required ---|")
                    print(f"Current Exhaustion DC: {CurrentJourneyState['CurrentExhaustionDC']}")

                    for Character in Characters:
                        SavingThrowResult = int(input(f"Enter {Character}'s Saving Throw: "))

                        if SavingThrowResult < CurrentJourneyState["CurrentExhaustionDC"]:
                            Characters[character]["ExhaustionLevel"] += 1

                            print(f"{Character} Failed, gains 1 Level of Exhaustion")
                            print(f"{Character} currently has {Characters['ExhaustionLevel']} Levels of Exhaustion")

                        else:
                            print(f"{Character} suceeds.")
                        

                CurrentJourneyState["CurrentExhaustionDC"] += 1
                CurrentJourneyState["NextExhaustionCheck"] += 2
                    


            else:
                print("Invalid choice, please choose from one of the provided options.")

        
# --- Main Program ---#
NumOfHexes, TravelDistance, HexValue = GetJourneyInfo()

CurrentHex = 1
while CurrentJourneyState["MilesRemaining"] > 0.01:
    ProcessCurrentHex(CurrentHex, HexValue)
    CurrentHex += 1
