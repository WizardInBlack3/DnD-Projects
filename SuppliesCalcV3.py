## Supplies Calculator V3 

import random
import math

def GetBasicInfo():
    HexValue = float(input("How many miles does a single Hex represent?: "))                #Should always be a whole number, despite the code allowing it to be a float.
    TravelDistance = float(input("How many miles long will this journey be?: "))

    #TravelPaceVerifyer: This loop acquires the Travel Pace at which The Party is using, and verifies they have entered a valid option
    while True:          
        TravelPace = input("Which Travel Pace will the Adventuring Party be using? [Normal, Fast, or Slow]: ")

        if TravelPace == 'Normal' or TravelPace == 'normal':
            print("")
            print("The standard travel pace, an equilbibrium of swiftness and caution. At Normal travel pace, an Adventuring Party can travel 36 miles per day, at a rate of 3MPH for 12 hours.")
        elif TravelPace == "Fast" or TravelPace == "fast":
            print("")
            print("A hastened travel pace, spurred on by desperation at the expense of caution. At Fast travel pace, an Adventuring Party can travel 48 miles per day, at a rate of 4MPH for 12 hours.")
        elif TravelPace == "Slow" or TravelPace == "slow":
            print("")
            print("A timid travel pace, mired by lethargy or paranoia. At Slow travel pace, an Adventuring Party can travel 24 miles per day at a rate of 2MPH for 12 hours.") 
        else:
            print("Your input is invalid, please x2 check your spelling and ensure you've entered Normal, Fast, or Slow!")
            continue    #restarts TravelPaceVerifyer loop

        TravelPaceConfirm = input("Is this okay? [Y/N]: ").strip().lower()
                   #.strip().lower() will remove leading and trailing whitespace from the user input, account for accdiental presses of the spacebar
        if TravelPaceConfirm == "y":
            break          #exits TravePaceVerifyer loop
        elif TravelPaceConfirm == "n":
            print("Let's pick a different one.")
            continue          #restarts TravelPaceVerifyer loop
        else:
            print("Invalid input, please try again")
            continue          #restarts TravelPaceVerifyer loop
            
    print("")
    print("Preem. Now let's calculate the cost!...")
    print("")

    return TravelPace, HexValue, TravelDistance


def PerformCalculations(HexValue, TravelDistance, TravelPace):
    #Determines which source of Light that The Party uses for this journey
    while True:
        LightSource = input("Which Light Source will The Party use for this journey? [Torches/Lantern]: ")
        if LightSource == "torches" or LightSource == "torch" or LightSource == "Torches" or LightSource == "Torch":
            LightSourceCost = float(input("How much does 1 Torch cost?: "))
            break
        elif LightSource == "lanterns" or LightSource == "lantern" or LightSource == "Lanterns" or LightSource == "Lantern":
            LightSourceCost = float(input("How much does 1 Flask of Oil Cost?: "))
            break
        else:
            print("Error: Invalid light source. Please try again.")
            continue
        return LightSource, LightSourceCost
    RationsCost = float(input("How much does 1 Portion of Rations cost?: "))
    FirewoodCost = float(input("How much does 1 Bundle of Firewood cost?: "))
    NumOfPartyMembs = int(input("How many Adventurers are in The Party?: "))
    print(" ")


    if TravelPace == "Normal" or TravelPace == "normal":
        TravelTime = TravelDistance / 3               #/ by 3 (mph) is hard-coded as per the rules of Normal Overworld Travel Pace
        ShortRests = TravelTime // 12                 # if a journey takes longer than 12 hours to complete, The Party must take a Short Rest, which consists of 8 hours and sleep and 4 hours of relaxation, eating, crafting, etc.
        TotalRestTime = ShortRests * 8                # The Short Rest duration needs to be acounted for when determining
        TotalJourneyTime = TravelTime + TotalRestTime
        TravelTimeHours = int(TotalJourneyTime)                              #Converting TravelTime into an Hour:Minute format for mathematical and readability purposes.
        TravelTimeMinutes = int((TotalJourneyTime - TravelTimeHours) * 60)       

        # -- Light Source Calculations --
        if LightSource == "torches" or LightSource == "torch" or LightSource == "Torches" or LightSource == "Torch":
            LightUnitsNeeded = math.ceil(TotalJourneyTime)
            HoursPerHex = HexValue / 3                      #/ by 3 as per rules of Normal Travel Pace
            TorchLifetime = 1.0                               # hard-coded to = 1 hour, as per the rules of Light Sources
            UnburntTorchAmt = 0.0

            TorchesPerHexList = []
            LeftoverTorchTimePerHex = []
            MilesPerHexList = []

            num_hexes = math.ceil(TravelDistance / HexValue)

            for hex_index in range(num_hexes):                     #Full Dsiclaimer: This code block is AI-genn'd because idk how tf to use lists fr.
                
                if hex_index < num_hexes - 1:
                    MilesRemaining4ThisHex = HexValue
                else:
                    MilesRemaining4ThisHex = TravelDistance - (HexValue * (num_hexes - 1))

                MilesPerHexList.append(MilesRemaining4ThisHex)
                #Converting miles to hours
                HoursThisHex = MilesRemaining4ThisHex / 3

                EffectiveHours = HoursPerHex - UnburntTorchAmt

                if EffectiveHours <= 0:
                    TorchesUsed = 0
                    UnburntTorchAmt = abs(EffectiveHours)
                else:
                    TorchesUsed = math.ceil(EffectiveHours)
                    UnburntTorchAmt = (TorchesUsed - EffectiveHours)

                TorchesPerHexList.append(TorchesUsed)
                LeftoverTorchTimePerHex.append(UnburntTorchAmt)
                
            AverageTorchesPerHex = sum(TorchesPerHexList) / len(TorchesPerHexList)
            TotalTorchesUsed = sum(TorchesPerHexList)
            AverageTorchesPerHex = sum(TorchesPerHexList) / len(TorchesPerHexList)
            TorchCostPerHex = [t * LightSourceCost for t in TorchesPerHexList]
            TotalTorchCost = TotalTorchesUsed * LightSourceCost

            print("\n--- Torch Usage Per Hex ---")
            for i, (t, leftover, miles) in enumerate(zip(TorchesPerHexList, LeftoverTorchTimePerHex, MilesPerHexList), start=1):
                
                LeftoverHours = int(leftover)
                LeftoverMins = int((leftover - LeftoverHours) * 60)          

                print(f"Hex {i}: Torches Used = {t}, Unspent Torch Time = {LeftoverHours}h {LeftoverMins}m")

            print(f"\n Average Torches Per Hex: {AverageTorchesPerHex: .2f}")
            print(f"Total Torches Used: {TotalTorchesUsed}")
            print(f"Total Torch Cost: {TotalTorchCost} Gold")

            FinalLeftoverHours = int(UnburntTorchAmt)
            FinalLeftoverMins = int((UnburntTorchAmt - FinalLeftoverHours) * 60)
            
            print(f"Unspent Torch Time Upon Arrival: {FinalLeftoverHours}h {FinalLeftoverMins}m") 
    
         
        if ShortRests > 0:
            FirewoodNeeded = ShortRests                         # Because there is a 1-to-1 relationship between Firewood & Short Rests.
            TotalFirewoodCost = FirewoodCost * FirewoodNeeded
            RationsNeeded = ShortRests                          # Because, like firewood, there is a 1-to-1 relationship between Rations and Short Rests; however, each member of The Party must purchase 1 Ration per Short Rest in order to benefit from the Short Rest.
            TotalRationsCost = (RationsCost * NumOfPartyMembs) * ShortRests

            
            print(f"The Party must take {ShortRests} Short Rest(s).")
            print(f"Each Short Rest requires 1 Firewood. Because this journey requires {ShortRests} short rests, The Party must buy {FirewoodNeeded} bundles of firewood ({TotalFirewoodCost} Gold).")
            print (f"Additionally, since there are {NumOfPartyMembs} adventurers in The Party, they must buy {TotalRationsCost} Gold worth of rations.") 
        else:
            print ("The Party does not need to take a Short Rest during this journey.")
        TravelTime = str(TravelTime)
        TravelTimeHours = str(TravelTimeHours)
        TravelTimeMinutes = str(TravelTimeMinutes)
        print(f"Accounting for rests, at {TravelPace} travel pace, it will take {TravelTimeHours} hours and {TravelTimeMinutes} minutes to arrive at your destination.")
        # TotalJourneyCost = TotalRationsCost + TotalFirewoodCost + 


        
    elif TravelPace == "Fast" or TravelPace == "fast":
        TravelTime = TravelDistance / 4               #/ by 4 (mph) is hard-coded as per the rules of Fast Overworld Travel Pace
        ShortRests = TravelTime // 12
        TotalRestTime = ShortRests * 8
        TotalJourneyTime = TravelTime + TotalRestTime
        TravelTimeHours = int(TotalJourneyTime)
        TravelTimeMinutes = int((TotalJourneyTime - TravelTimeHours) * 60)
        
        # -- Light Source Calculations --
        if LightSource == "torches" or LightSource == "torch" or LightSource == "Torches" or LightSource == "Torch":
            LightUnitsNeeded = math.ceil(TotalJourneyTime)
            HoursPerHex = HexValue / 4                      #/ by 4 as per rules of Normal Travel Pace
            TorchLifetime = 1.0                               # hard-coded to = 1 hour, as per the rules of Light Sources
            UnburntTorchAmt = 0.0

            TorchesPerHexList = []
            LeftoverTorchTimePerHex = []
            MilesPerHexList = []

            num_hexes = math.ceil(TravelDistance / HexValue)

            for hex_index in range(num_hexes):                     #Full Dsiclaimer: This code block is AI-genn'd because idk how tf to use lists fr.
                
                if hex_index < num_hexes - 1:
                    MilesRemaining4ThisHex = HexValue
                else:
                    MilesRemaining4ThisHex = TravelDistance - (HexValue * (num_hexes - 1))

                MilesPerHexList.append(MilesRemaining4ThisHex)
                #Converting miles to hours
                HoursThisHex = MilesRemaining4ThisHex / 3

                EffectiveHours = HoursPerHex - UnburntTorchAmt

                if EffectiveHours <= 0:
                    TorchesUsed = 0
                    UnburntTorchAmt = abs(EffectiveHours)
                else:
                    TorchesUsed = math.ceil(EffectiveHours)
                    UnburntTorchAmt = (TorchesUsed - EffectiveHours)

                TorchesPerHexList.append(TorchesUsed)
                LeftoverTorchTimePerHex.append(UnburntTorchAmt)
                
            AverageTorchesPerHex = sum(TorchesPerHexList) / len(TorchesPerHexList)
            TotalTorchesUsed = sum(TorchesPerHexList)
            AverageTorchesPerHex = sum(TorchesPerHexList) / len(TorchesPerHexList)
            TorchCostPerHex = [t * LightSourceCost for t in TorchesPerHexList]
            TotalTorchCost = TotalTorchesUsed * LightSourceCost

            print("\n--- Torch Usage Per Hex ---")
            for i, (t, leftover, miles) in enumerate(zip(TorchesPerHexList, LeftoverTorchTimePerHex, MilesPerHexList), start=1):
                
                LeftoverHours = int(leftover)
                LeftoverMins = int((leftover - LeftoverHours) * 60)          

                print(f"Hex {i}: Torches Used = {t}, Unspent Torch Time = {LeftoverHours}h {LeftoverMins}m")

            print(f"\n Average Torches Per Hex: {AverageTorchesPerHex: .2f}")
            print(f"Total Torches Used: {TotalTorchesUsed}")
            print(f"Total Torch Cost: {TotalTorchCost} Gold")

            FinalLeftoverHours = int(UnburntTorchAmt)
            FinalLeftoverMins = int((UnburntTorchAmt - FinalLeftoverHours) * 60)
            
            print(f"Unspent Torch Time Upon Arrival: {FinalLeftoverHours}h {FinalLeftoverMins}m") 
    
         
        if ShortRests > 0:
            FirewoodNeeded = ShortRests                         # Because there is a 1-to-1 relationship between Firewood & Short Rests.
            TotalFirewoodCost = FirewoodCost * FirewoodNeeded
            RationsNeeded = ShortRests                          # Because, like firewood, there is a 1-to-1 relationship between Rations and Short Rests; however, each member of The Party must purchase 1 Ration per Short Rest in order to benefit from the Short Rest.
            TotalRationsCost = (RationsCost * NumOfPartyMembs) * ShortRests

            
            print(f"The Party must take {ShortRests} Short Rest(s).")
            print(f"Each Short Rest requires 1 Firewood. Because this journey requires {ShortRests} short rests, The Party must buy {FirewoodNeeded} bundles of firewood ({TotalFirewoodCost} Gold).")
            print (f"Additionally, since there are {NumOfPartyMembs} adventurers in The Party, they must buy {TotalRationsCost} Gold worth of rations.") 
        else:
            print ("The Party does not need to take a Short Rest during this journey.")
        TravelTime = str(TravelTime)
        TravelTimeHours = str(TravelTimeHours)
        TravelTimeMinutes = str(TravelTimeMinutes)
        print(f"Accounting for rests, at {TravelPace} travel pace, it will take {TravelTimeHours} hours and {TravelTimeMinutes} minutes to arrive at your destination.") 


 
        

    elif TravelPace == "Slow" or TravelPace == "slow":
        TravelTime = TravelDistance / 2               #/ by 2 (mph) is hard-coded as per the rules of Slow Overworld Travel Pace
        ShortRests = TravelTime // 12
        TotalRestTime = ShortRests * 8
        TotalJourneyTime = TravelTime + TotalRestTime
        TravelTimeHours = int(TotalJourneyTime)
        TravelTimeMinutes = int((TotalJourneyTime - TravelTimeHours) * 60)

        # -- Light Source Calculations --
        if LightSource == "torches" or LightSource == "torch" or LightSource == "Torches" or LightSource == "Torch":
            LightUnitsNeeded = math.ceil(TotalJourneyTime)
            HoursPerHex = HexValue / 2                      #/ by 2 as per rules of Normal Travel Pace
            TorchLifetime = 1.0                               # hard-coded to = 1 hour, as per the rules of Light Sources
            UnburntTorchAmt = 0.0

            TorchesPerHexList = []
            LeftoverTorchTimePerHex = []
            MilesPerHexList = []

            num_hexes = math.ceil(TravelDistance / HexValue)

            for hex_index in range(num_hexes):                     #Full Dsiclaimer: This code block is AI-genn'd because idk how tf to use lists fr.
                
                if hex_index < num_hexes - 1:
                    MilesRemaining4ThisHex = HexValue
                else:
                    MilesRemaining4ThisHex = TravelDistance - (HexValue * (num_hexes - 1))

                MilesPerHexList.append(MilesRemaining4ThisHex)
                #Converting miles to hours
                HoursThisHex = MilesRemaining4ThisHex / 3

                EffectiveHours = HoursPerHex - UnburntTorchAmt

                if EffectiveHours <= 0:
                    TorchesUsed = 0
                    UnburntTorchAmt = abs(EffectiveHours)
                else:
                    TorchesUsed = math.ceil(EffectiveHours)
                    UnburntTorchAmt = (TorchesUsed - EffectiveHours)

                TorchesPerHexList.append(TorchesUsed)
                LeftoverTorchTimePerHex.append(UnburntTorchAmt)
                
            AverageTorchesPerHex = sum(TorchesPerHexList) / len(TorchesPerHexList)
            TotalTorchesUsed = sum(TorchesPerHexList)
            AverageTorchesPerHex = sum(TorchesPerHexList) / len(TorchesPerHexList)
            TorchCostPerHex = [t * LightSourceCost for t in TorchesPerHexList]
            TotalTorchCost = TotalTorchesUsed * LightSourceCost

            print("\n--- Torch Usage Per Hex ---")
            for i, (t, leftover, miles) in enumerate(zip(TorchesPerHexList, LeftoverTorchTimePerHex, MilesPerHexList), start=1):
                
                LeftoverHours = int(leftover)
                LeftoverMins = int((leftover - LeftoverHours) * 60)          

                print(f"Hex {i}: Torches Used = {t}, Unspent Torch Time = {LeftoverHours}h {LeftoverMins}m")

            print(f"\n Average Torches Per Hex: {AverageTorchesPerHex: .2f}")
            print(f"Total Torches Used: {TotalTorchesUsed}")
            print(f"Total Torch Cost: {TotalTorchCost} Gold")

            FinalLeftoverHours = int(UnburntTorchAmt)
            FinalLeftoverMins = int((UnburntTorchAmt - FinalLeftoverHours) * 60)
            
            print(f"Unspent Torch Time Upon Arrival: {FinalLeftoverHours}h {FinalLeftoverMins}m") 
    
         
        if ShortRests > 0:
            FirewoodNeeded = ShortRests                         # Because there is a 1-to-1 relationship between Firewood & Short Rests.
            TotalFirewoodCost = FirewoodCost * FirewoodNeeded
            RationsNeeded = ShortRests                          # Because, like firewood, there is a 1-to-1 relationship between Rations and Short Rests; however, each member of The Party must purchase 1 Ration per Short Rest in order to benefit from the Short Rest.
            TotalRationsCost = (RationsCost * NumOfPartyMembs) * ShortRests

            
            print(f"The Party must take {ShortRests} Short Rest(s).")
            print(f"Each Short Rest requires 1 Firewood. Because this journey requires {ShortRests} short rests, The Party must buy {FirewoodNeeded} bundles of firewood ({TotalFirewoodCost} Gold).")
            print (f"Additionally, since there are {NumOfPartyMembs} adventurers in The Party, they must buy {TotalRationsCost} Gold worth of rations.") 
        else:
            print ("The Party does not need to take a Short Rest during this journey.")
        TravelTime = str(TravelTime)
        TravelTimeHours = str(TravelTimeHours)
        TravelTimeMinutes = str(TravelTimeMinutes)
        print(f"Accounting for rests, at {TravelPace} travel pace, it will take {TravelTimeHours} hours and {TravelTimeMinutes} minutes to arrive at your destination.") 


 
        

        
        






        
TravelPace, HexValue, TravelDistance = GetBasicInfo()
PerformCalculations(HexValue, TravelDistance, TravelPace)
