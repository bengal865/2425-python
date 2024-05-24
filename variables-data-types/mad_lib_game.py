# MAD LIB GAME
# 31 MAY 2018
# More Python Programming book, pp. 40-42

print("MR. PROVENCHER'S MAD LIB GAME")
print("Enter your answer to the following prompts\n")

guy = input("Name of a famous man:\n")
girl = input("Name of a famous woman:\n")
food = input("Plural form of your favorite food:\n")
ship = input("Name of a famous spaceship:\n")

job = input("Plural form of a profession:\n")
planet = input("Name of a planet:\n")
drink = input("Your favorite drink:\n")
number = input("A number between 1 and 10:\n")

story = """
	A famous Hollywood couple, GUY and GIRL, went on\n
	vacation to the planet PLANET.  Travelling aboard the SHIP,\n
	it took NUMBER weeks to reach the planet.  They enjoyed a quiet\n
	candlelight dinner overlooking an ocean made of DRINK,\n
	all the while savoring their FOOD.  But because they were both JOB,\n
	they had to cut their vacation short by four days.
"""
	
story = story.replace("GUY", guy)
story = story.replace("GIRL", girl)
story = story.replace("FOOD", food)
story = story.replace("SHIP", ship)

story = story.replace("JOB", job)
story = story.replace("PLANET", planet)
story = story.replace("DRINK", drink)
story = story.replace("NUMBER", number)

print(story)
