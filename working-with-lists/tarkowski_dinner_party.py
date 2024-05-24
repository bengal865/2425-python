#Richie Tarkowski
#10/14/16
#Dinner Party

import time

party = ['LeBron James' , 'Michael Jordan' , 'Wilt Chamberlain']
print("Dinner Party:")
print()
print()

#Create list of who is invited.

print("People invited:")
print()
print(party[0] ,",", party[1] ,",", party[2])
print()

input("Press ENTER to write invitations.")
print()

time.sleep(1)
print("Writing invitations...")
time.sleep(2)
print()

#Create invitations for each of them.

print(party[0] , ", you are invited to a dinner party at my house on Saturday, October 15, 2016. RSVP me!")
print(party[1] , ", you are invited to a dinner party at my house on Saturday, October 15, 2016. RSVP me!")
print(party[2] , ", you are invited to a dinner party at my house on Saturday, October 15, 2016. RSVP me!")
print()
print()

input("Press ENTER to send invitations.")
print()

time.sleep(1)
print("Waiting for responses...")
time.sleep(1)
print()
print()

#Show who can attend or not.

print("RSVP's:")
print()
print(party[0], ": YES")
print(party[1], ": YES")
print(party[2], ": NO")
print()

#Take Wilt C. off the list and add Magic J.

del party[2]
party.append('Magic Johnson')

print("Magic Johnson will be invited instead.")
print()

input("Press ENTER to write new invitations.")
print()

#Write new invitations for them.

print(party[0], ", you are either still invited or being invited to my dinner party on Saturday, October 15, 2016, at my house. The time is 8:00 pm.")
print(party[1], ", you are either still invited or being invited to my dinner party on Saturday, October 15, 2016, at my house. The time is 8:00 pm.")
print(party[2], ", you are either still invited or being invited to my dinner party on Saturday, October 15, 2016, at my house. The time is 8:00 pm.")
print()

input("Press ENTER to send invitations.")
print()

time.sleep(1)
print("Sent.")
time.sleep(1)
print()

#Add people to my list and send them invitations.

party.insert(0, "Kyrie Irving")
party.insert(2, "Kobe Bryant")
party.append("Tim Duncan")

print("Party moved to outdoors..." , party[0] ,",", party[2] ,",", party[5] , "will now be invited.")
print()

input("Press ENTER to write new invitations.")
print()

time.sleep(1)
print("Writing new invitations...")
time.sleep(1)
print()

print(party[0], ", you are either still invited or being invited in this letter to the dinner party at my house on Saturday, October 15, 2016. The party is now being held outdoors.")
print(party[1], ", you are either still invited or being invited in this letter to the dinner party at my house on Saturday, October 15, 2016. The party is now being held outdoors.")
print(party[2], ", you are either still invited or being invited in this letter to the dinner party at my house on Saturday, October 15, 2016. The party is now being held outdoors.")
print(party[3], ", you are either still invited or being invited in this letter to the dinner party at my house on Saturday, October 15, 2016. The party is now being held outdoors.")
print(party[4], ", you are either still invited or being invited in this letter to the dinner party at my house on Saturday, October 15, 2016. The party is now being held outdoors.")
print(party[5], ", you are either still invited or being invited in this letter to the dinner party at my house on Saturday, October 15, 2016. The party is now being held outdoors.")
print()

input("Press ENTER to send the new invitations.")
print()

time.sleep(1)
print("Sent.")
time.sleep(1)
print()

#Remove four people from my list and let them know I am sorry to hear that they can not go.

print("Due to the forecast, only two guests have agreed to still go to your party.")
print()

input("Press ENTER to start removing guests from the list and let them know you are sorry they decided not to attend.")
print()

remove1 = party.pop(0)
print(remove1, ", I am sorry to hear you decided not to attend, maybe next time!")
print()
time.sleep(3)

remove2 = party.pop(1)
print(remove2, ", I am sorry to hear you decided not to attend, maybe next time!")
print()
time.sleep(3)

remove3 = party.pop(2)
print(remove3, ", I am sorry to hear you decided not to attend, maybe next time!")
print()
time.sleep(3)

remove4 = party.pop(2)
print(remove4, ", I am sorry to hear you decided not to attend, maybe next time!")
print()
time.sleep(3)
print()

#Let the two remaining guests know the food will be great.

input("Press ENTER to let the two remaining guests that you are glad they are coming and the food will be great!")
print()

time.sleep(1)
print("Writing invitations...")
print()
time.sleep(1)
print("Sending letters...")
time.sleep(1)
print()
print()

print(party[0] , ", thank you for deciding to still attend my outdoor party! The food will be great!!!")
print(party[1] , ", thank you for deciding to still attend my outdoor party! The food will be great!!!")
print()

#Remove the last two people from the list and print the empty list.

print("We will now remove the last two guests from the list because the party is starting soon.")
del party[0]
del party[0]
print()

print("Here is what remains on our list:")
print(party)



