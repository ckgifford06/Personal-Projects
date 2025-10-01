# This is my wordle program. I did this in my free time.
# GIFFORD, CHARLES
# 10/07/24

import random
import datetime 


words = ["apple", "grape", "brave", "piano", "scale", "flute", "stone", "grain", "plane", "brain", "shine", "spade", "train", "frost", "glide", "crane", "flame", "charm", "cloud", "clamp", "grace", "blend",
         "stack", "track", "strap", "grant", "lemon", "camel", "chart", "chime", "grasp", "climb", "frame", "march", "flask", "blaze", "gleam", "crisp", "spear", "grind", "roast", "stand", "stare", "flair",
         "fable", "chase", "bland", "grasp", "fling", "sweep", "slope", "score", "flock", "smoke", "flute", "shark", "shrug", "stork", "flash", "guard", "frail", "grape", "crisp", "flint", "slick", "stake",
         "grind", "skate", "flint", "sheep", "shiny", "glare", "flour", "shrub", "flirt", "smart", "sleep", "greet", "flume", "glory", "crane", "sleek", "trail", "fling", "glove", "shark", "shrug", "flash",
         "trick", "gravy", "fraud", "slump", "stomp", "trace", "tramp", "glaze", "trove", "crave", "sheer", "flock", "glide", "grunt", "slate", "shark", "smirk", "flask", "grasp", "trace", "blush", "glide",
         "tramp", "flock", "glint", "steep", "trace", "fluff", "globe", "tryst", "frown", "glare", "trove", "shiny", "glove", "trace", "smoke", "shone", "flock", "grape", "tried", "shine", "flask", "glaze",
         "stork", "sheer", "flash", "glove", "trove", "crave", "sheer", "shine", "glare", "trace", "flock", "grasp", "shine", "glaze", "shark", "smirk", "flask", "grape", "trail", "flock", "glide", "trove",
         "crane", "shine", "flock", "greet", "flour", "shrub", "flint", "sleek", "shine"]

def generateDailyWord():
    random.seed(datetime.date.today().toordinal())
    return random.randint(1, len(words))

correctAnswer = words[generateDailyWord()]

guess = input("Enter your first guess (five-letter word): ")
count = 1

if len(guess) > 5:
    print("That is not five letters. Try again. To try again, simply press the blue run button another time.")
    exit()

for i in range(0, 5):
    if guess[i] in correctAnswer and guess[i] == correctAnswer[i]:
            print(guess[i].upper() + " is in the correct position.")
    elif guess[i] in correctAnswer:
            print(guess[i].upper() + " is in the word, but is not in the correct position.")
    else:
        print(guess[i].upper() + " is not in the word.")

if guess == correctAnswer:
        print("Congratulations. That was your first try.")

while guess != correctAnswer:
    if count > 4:
        print("Sorry, nice try! The correct answer was: " + correctAnswer + ".")
        break
    guess = input("Enter another guess: ")
    count += 1
    for i in range(0, 5):
        if guess[i] in correctAnswer and guess[i] == correctAnswer[i]:
            print(guess[i].upper() + " is in the correct position.")
        elif guess[i] in correctAnswer:
            print(guess[i].upper() + " is in the word, but is not in the correct position.")
        else:
            print(guess[i].upper() + " is not in the word.")
    if guess == correctAnswer:
        print("Congratulations. " + correctAnswer + " is the correct answer. You got it right on try " + str(count) + ".")


