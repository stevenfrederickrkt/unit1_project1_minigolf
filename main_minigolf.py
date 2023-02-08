#mini golf python

name = input("Welcome to GC mini golf! What is your name? ")
num_holes = int(input(f'Hi, {name}! Would you like to play 3 or 6 holes today? '))
par = num_holes * 3
score = 0
for x in range(num_holes):
    strokes = int(input(f"How many putts for hole {x+1} (par is 3) "))
    score += strokes
"""Score Checking Debug
print(f'Score: {score}')
print(f'Par: {par}')"""
if (score > par):
    print(f"Nice try, {name}... Your total score was: +{score - par}.")
elif (score < par):
    print(f"Great job, {name}! Your total score was: {score-par}.")
else:
    print(f"Good game, {name}. Your total score was: {score-par}.")



