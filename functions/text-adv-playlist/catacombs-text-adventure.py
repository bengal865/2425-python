weapon = False

def strange_creature():
  actions = ["fight","flee"]
  global weapon
  print("A strange ghoul-like creature has appeared. You can either run or fight it. What would you like to do?")
  user_input = ""
  while user_input not in actions:
    print("Options: flee/fight")
    user_input = input()
    if user_input == "fight":
      if weapon:
        print("You kill the ghoul with the knife you found earlier. After moving forward, you find one of the exits. Congrats!")
      else:
        print("The ghoul-like creature has killed you.")
      quit()
    elif user_input == "flee":
      show_skeletons()
    else:
      print("Please enter a valid option.")
      
def show_skeletons():
  directions = ["backward","forward"]
  global weapon
  print("You see a wall of skeletons as you walk into the room. Someone is watching you. Where would you like to go?")
  user_input = ""
  while user_input not in directions:
    print("Options: left/backward/forward")
    user_input = input()
    if user_input == "left":
      print("You find that this door opens into a wall. You open some of the drywall and discover a knife.")
      weapon = True
    elif user_input == "backward":
      intro_scene()
    elif user_input == "forward":
      strange_creature()
    else:
      print("Please enter a valid option.")
      

def haunted_room():
  directions = ["right","left","backward"]
  print("You hear strange voices. You think you may have awakened some of the dead. Where would you like to go?")
  user_input = ""
  while user_input not in directions:
    print("Options: right/left/backward")
    user_input = input()
    if user_input == "right":
      print("Multiple ghoul-like creatures suddenly begin emerging as you enter the room. You are killed.")
      quit()
    elif user_input == "left":
      print("You made it! You've found an exit.")
      quit()
    elif user_input == "backward":
      intro_scene()
    else:
      print("Please enter a valid option.")

def camera_scene():
  directions = ["forward","backward"]
  print("You notice a camera that has been dropped on the ground. Someone else has been here recently. Where would you like to go?")
  user_input = ""
  while user_input not in directions:
    print("Options: forward/backward")
    user_input = input()
    if user_input == "forward":
      print("Success! You've found an exit.")
      quit()
    elif user_input == "backward":
      show_shadow_figure()
    else:
      print("Please enter a valid option.")
      
def show_shadow_figure():
  directions = ["right","backward"]
  print("You see a dark, shadowy figure appear in the distance. A chill runs down your spine. Where would you like to go?")
  user_input = ""
  while user_input not in directions:
    print("Options: right/left/backward")
    user_input = input()
    if user_input == "right":
      camera_scene()
    elif user_input == "left":
      print("You discover this door opens into a wall.")
    elif user_input == "backward":
      intro_scene()
    else:
      print("Please enter a valid option.")


def intro_scene():
  directions = ["left","right","forward"]
  print("You are at an intersection, and you can choose to proceed down any one of the four hallways. Where would you like to go?")
  user_input = ""
  while user_input not in directions:
    print("Options: left/right/backward/forward")
    user_input = input()
    if user_input == "left":
      show_shadow_figure()
    elif user_input == "right":
      show_skeletons()
    elif user_input == "forward":
      haunted_room()
    elif user_input == "backward":
      print("You find that this door opens into a wall.")
    else: 
      print("Please enter a valid option.")

if __name__ == "__main__":
  while True:
    print("Welcome to my text adventure game!")
    print("As an avid traveller, you have decided to visit the Catacombs of Paris.")
    print("However, during your exploration of the catacombs beneath the streets of Paris, you take a wrong turn and end up getting lost.")
    print("You can choose to walk in multiple directions to find a way out.")
    print("Before you start your adventure, however, please enter your first name:\n")
    first_name = input()
    print(f'Good luck, {first_name}!')
    intro_scene()