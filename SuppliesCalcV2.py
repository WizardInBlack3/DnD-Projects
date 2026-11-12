## Supplies Calculator V2

import random

def GetBasicInfo():
    HexValue = int(input("How many miles does a single Hex represent?: "))                #Should always be a whole number, despite the code allowing it to be a float.
    TravelDistance = int(input("How many miles long will this journey be?: "))

    #TravelPaceVerifyer: This loop acquires the Travel Pace at which The Party is using, and verifies they have entered a valid option
    while True:          
        TravelPace = input("Which Travel Pace will the Adventuring Party be using? [Normal, Fast, or Slow]: ")

        if TravelPace == 'Normal' or TravelPace == 'normal':
            print("The standard travel pace, an equilbibrium of swiftness and caution. At Normal travel pace, an Adventuring Party can travel 36 miles per day, at a rate of 3MPH for 12 hours.")
        elif TravelPace == "Fast" or TravelPace == "fast":
            print("A hastened travel pace, spurred on by desperation at the expense of caution. At Fast travel pace, an Adventuring Party can travel 48 miles per day, at a rate of 4MPH for 12 hours.")
        elif TravelPace == "Slow" or TravelPace == "slow":
            print("A timid travel pace, mired by lethargy or paranoia. At Slow travel pace, an Adventuring Party can travel 24 miles per day at a rate of 2MPH for 12 hours.") 
        else:
            print("Your input is invalid, please x2 check your spelling and ensure you've entered Normal, Fast, or Slow!")
            continue    #restarts TravelPaceVerifyer loop

        TravelPaceConfirm = input("Is this okay? [Y/N]: )").strip().lower()
                   #.strip().lower() will remove leading and trailing whitespace from the user input, account for accdiental presses of the spacebar
        if TravelPaceConfirm == "y":
            break          #exits TravePaceVerifyer loop
        elif TravelPaceConfirm == "n":
            print("Let's pick a different one.")
            continue          #restarts TravelPaceVerifyer loop
        else:
            print("Invalid input, please try again")
            continue          #restarts TravelPaceVerifyer loop
            
    print("Preem. Now let's calculate the cost!...")

def PerformCalculations(HexValue, TravelDistance, TravelPace):
    OilCost = float(input("How much 1 Flask of Oil Cost?: "))
    RationsCost = float(input("How much does 1 Portion of Rations cost?: "))
    FirewoodCost = float(input("How much does 1 Bundle of Firewood cost?: "))

    if TravelPace == "Normal" or TravelPace == "normal":
        HowLong2GetThere = TravelDistance // 3               #/ by 3 is hard-coded as per the rules of Normal Travel Pace
        print("peepee poopoo")
        print(HowLong2GetThere)
GetBasicInfo()
PerformCalculations(HexValue, TravelDistance, TravelPace)
