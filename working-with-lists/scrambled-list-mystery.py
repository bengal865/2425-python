# Scrambled List Mystery
# 05 JUN 20XX

scrambled_list = ["apple", "dog", "cat", "ball", "sleep"]

# Instructions (provide these to students):
# Use a for loop to iterate through the list.
# If the element starts with the letter "a", move it to the end of the list.
# Print the final unscrambled list.

# Solution code (hidden from students):
unscrambled_list = scrambled_list.copy()  # Avoid modifying original list by making a copy of it
for i in range(len(unscrambled_list)):
  if unscrambled_list[i][0].lower() == "a":
    temp = unscrambled_list.pop(i)  # Remove element from current position
    unscrambled_list.append(temp)  # Add element to the end

print("Unscrambled list:", unscrambled_list)
