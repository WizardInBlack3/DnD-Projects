import random


def PromptDemographics():
    name = input("Enter your name: ")
    age = input("Enter your age: ")

    print("Hello " + name + "! Pleased to meet you! :)")
    print(" "+ name + ", you are " + age + " years old!")
    
    race = input("What is your race?: ")

    print("I've always had pleasant relations with " + race + "s." )    
def Prompt4Battle():
    Population = ["1", "2", "3,", "4", "5", "6", "7", "8"]
    CreaturePossibilites = ["Goblins", "Wolves", "Giant Rats", "Minotaurs", "Ogres"]
    Answer = input("Are you looking to fight a monster?: ")
    if Answer == "yes":
        print("Very well, then.")
        print ("You shall be fighting...")
        RandomPopulationResult = random.choice(Population)
        print(RandomPopulationResult)
        RandomCreatureResult = random.choice(CreaturePossibilites)
        print(RandomCreatureResult)
    if Answer == "no":
        print("Coward :P")

PromptDemographics()
Prompt4Battle()

#CreaturePopulationPossibilites = ["1", "2", "3,", "4", "5", "6", "7", "8"]
#CreaturePossibilites = ["Goblins", "Wolves", "Giant Rats", "Minotaurs", "Ogres"]
#CreaturePopulation = random.choice(CreaturePopulationPossibilites)
#CreaturesAppeared = random.choice(CreaturePossibilities)
#print(CreaturePopulation)
#print(CreaturesAppeared)
               
