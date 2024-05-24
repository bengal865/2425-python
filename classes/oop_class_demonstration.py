# Author: Bruce Provencher
# Date: 15 AUG 2014
# Project: OOP Demo 1



class Lifeform:


    def __init__(self, numberOfEyes, lifeSpan, clan):
        
        self.numberOfEyes = numberOfEyes
        self.lifeSpan = lifeSpan
        self.clan = clan


        

firstAlien = Lifeform(3, 2500, "Zylosian")
print ("I just created an alien based on the Lifeform class!")
print ("My first alien has", firstAlien.numberOfEyes,"eyes.")
print ("It has a lifespan of",firstAlien.lifeSpan,"years, and")
print ("belongs to the",firstAlien.clan,"clan.\n\n")





secondAlien = Lifeform(8, 10000, "Circadian")
print ("I just created a second alien based on the Lifeform class!")
print ("My second alien has", secondAlien.numberOfEyes,"eyes.")
print ("It has a lifespan of",secondAlien.lifeSpan,"years, and")
print ("belongs to the",secondAlien.clan,"clan.")

