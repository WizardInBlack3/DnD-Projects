import random

def GetBasicInfo():
    HexValue = int(input("How many miles does a single Hex represent?: "))     ##put error checking here - ensure than a whole number GREATER THAN 0 is entered
    TravelDistance = int(input("How many miles long will this journey be?: "))     ##put error checking here - ensure a whole number GREATER THAN 0 is entered
    TravelPace = input("Which Travel Pace will the Adventuring Party be using? [Normal, Fast, or Slow]: ")     ##put error checking here - ensure the user enters the choices provided

    while TravelPace == "Normal" or TravelPace == "normal":
        print("At " + TravelPace + " Travel Pace, an Adventuring Party can travel 36 miles per day, at a rate of 3MPH for a total of 12 hours.")
        TravelPaceConfirm = input("Is this ok?: [Y/N] ")
        while TravelPaceConfirm == "Y" or TravelPaceConfirm == "y":
            print("Preem. Now to calculate the cost...")
            OilCost = int(input("How much does 1 Flask of Oil cost?: "))
            RationsCost = int(input("How much does 1 Portion of Rations cost?: "))
            FirewoodCost = int(input("How much does 1 Bundle of Firewood cost?: "))
            ## complicated math goes here
            HowLong2GetThere = TravelDistance // 3          ##Dividing by 3 is hard-coded as per the rules of Normal Travel Pace: "at a rate of 3MPH"
            print(HowLong2GetThere)                         ##Included to help verify math.
            OilFlaskLifetime = 240                          ##240 minutes = 4 hours
            HowManyFlasks = 0
            ## 1 flask lasts max of 4 hrs, but in order to
            ## be safe, the Light Level needs to be kept above
            ## Dark. Dark is the 2nd lowest tier of Light Level (Black as Pitch being the lowest).
            ## In order to accurate determine how many flasks are oil are needed, I'll need to
            ## find out the relatinship between Light Level, Time, and portions of an oil flask.
            ## In a lantern, 1 flask of oil lasts for a total of 4 hours, the Light Level is reduced by 1 every 30 minutes.
            ## 0 - 30 mins = Radiant, 31 - 60 mins = Dim Light, 61 - 90 mins = Shadowy, 91 mins to 120 mins = Dark, 121 mins - 150 mins = Black as Pitch.
            ## ;therefore, after 2.5 hours, a flask of oil is totally burnt up, the Light Level is at Black as Pitch.
            ## 
            break
        while TravelPaceConfirm == "N" or TravelPaceConfirm == "n":
            print("Welp. Idk how to re-prompt you so byeee")
            return ##I need this to go back to where it prompts the users for a new TravelPace. How?..
        ##if TravelPaceConfirm != "Y" or TravelPaceConfirm != "y" or TravelPaceConfirm != "N" or TravelPaceConfirm != "n":
            ##print("The prey approaches")     ##For whatever reason, this line of code still executes even if TravelPaceConfirm == Y, y, N, or N.
    while TravelPace == "Slow" or TravelPace == "slow":
         print("At " + TravelPace + " Travel Pace, an Adventuring Party can travel 24 miles per day, at a rate of 2MPH for a total of 12 hours.")
         TravelPaceConfirm = input("Is this ok?: [Y/N] ")
         while TravelPaceConfirm == "Y" or TravelPaceConfirm == "y":
             print("Preem. Now to calculate the cost...")
             OilCost = int(input("How much does 1 Flask of Oil cost?: "))
             RationsCost = int(input("How much does 1 Portion of Rations cost?: "))
             FirewoodCost = int(input("How much does 1 Bundle of Firewood cost?: "))
             return
         if TravelPaceConfirm == "N" or TravelPaceConfirm == "n":
             print("Welp. Idk how to re-prompt you so byeee")
             break
    while TravelPace == "Fast" or TravelPace == "fast":
            print("At " + TravelPace + " Travel Pace, an Adventuring Party can travel 48 miles per day, at a rate of 4MPH for a total of 12 hours.")
            TravelPaceConfirm = input("Is this ok?: [Y/N] ")
            while TravelPaceConfirm == "Y" or TravelPaceConfirm == "y":
                print("Preem. Now to calculate the cost...")
                OilCost = int(input("How much does 1 Flask of Oil cost?: "))
                RationsCost = int(input("How much does 1 Portion of Rations cost?: "))
                FirewoodCost = int(input("How much does 1 Bundle of Firewood cost?: "))
                return
            if TravelPaceConfirm == "N" or TravelPaceConfirm == "n":
                print("Welp. Idk how to re-prompt you so byeee")
                break
    while TravelPace != "Fast" or TravelPace != "fast" or TravelPace != "Slow" or TravelPace != "slow" or TravelPace != "Normal" or TravelPace != "normal":
        print("That Travel Pace does not exist")
        break          ## This leaves the program, not 100% what I intend, but doesn't create an infinite loop.  

##Copy-and-Paste these when needed
"""
    OilCost = int(input("How much does 1 Flask of Oil cost?: "))
    ##put error checking here - ensure a whole number GREATER THAN 0 is entered
    RationsCost = int(input("How much does 1 Portion of Rations cost?: "))
    #put error checking here - ensure a whole numbrer GREATER THAN 0 is entered
    FirewoodCost = int(input("How much does 1 Bundle of Firewood cost?: "))
    #put error checking here - ensure a whole number GREATER THAN 0 is entered

"""



GetBasicInfo()
