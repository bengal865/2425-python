# Highest & Lowest Scores in a List
# 05 JUN 20XX

scores = [78, 92, 56, 88, 45, 100]

# Finding the highest score
highest_score = scores[0]
for score in scores:
  if score > highest_score:
    highest_score = score

# Finding the lowest score (similar logic)
lowest_score = scores[0]
for score in scores:
  if score < lowest_score:
    lowest_score = score

print("Highest Score:", highest_score)
print("Lowest Score:", lowest_score)
