import random

def RandomPopulationAndInitiative():
    Population = ["1", "2", "3", "4", "5", "6", "7", "8"]
    InitiativeVal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    CreaturePossibilities = ["Goblins", "Wolves", "Giant Rats", "Minotaurs", "Ogres"]
    RandomPopulationResult = random.choice(Population)
    RandomCreatureResult = random.choice(CreaturePossibilities)
    print("There are " + RandomPopulationResult + " " + RandomCreatureResult + " before you!")
    RandomPopulationResultAsInt = int(RandomPopulationResult)
    print("I need to calculate the Initiative of " + RandomPopulationResult + " " +RandomCreatureResult+ "...")

##for loop? while loop? some type of loop??
    
    
    
RandomPopulationAndInitiative()
    
