# Programmer: Bruce Provencher
# Times table using built-in Python range() function

what_num = int(input("What number do you wish to multiply?\n"))
start_value = 1
max_value = int(input("How high should the times table go?\n"))
max_value += 1

for looper in range(start_value, max_value):
    print (looper, "times", what_num, "=", looper * what_num)
