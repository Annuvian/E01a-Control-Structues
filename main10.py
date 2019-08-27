#!/usr/bin/env python3

import sys, utils, random           # import the modules we will need

utils.check_version((3,7))          # make sure we are running at least Python 3.7
utils.clear()                       # clear the screen


print('Greetings!')                                                 # Prints out the string "Greetings!" to the console.
colors = ['red','orange','yellow','green','blue','violet','purple'] # Stores the colors listed to an array variable called "colors".
play_again = ''                                                     # Defines the variable "play_again" as being equal to an empty string
best_count = sys.maxsize                                            # the biggest number
while (play_again != 'n' and play_again != 'no'):                   # If user input does not equal "n" or "no" when asked to play again, the game starts over.
    match_color = random.choice(colors)                             # Randomly picks an item from the "colors" array as the "match_color"
    count = 0                                                       # Sets the variable "count" equal to 0.
    color = ''                                                      # Sets the variable "color" equal to an empty string
    while (color != match_color):                                   # Keeps the loop repeating until the user guesses the right color.
        color = input("\nWhat is my favorite color? ")              # \n is a special code that adds a new line
        color = color.lower().strip()                               # Changes the user input to all lowercase and strips leading and trailing spaces.
        count += 1                                                  # Increments count by 1
        if (color == match_color):                                  # Checks to see if the user guessed the right color.
            print('Correct!')                                       # If they did guess the right color, prints "Correct!" to the console.
        else:                                                       # Below this line is what happens if the correct color is NOT guessed correctly.
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count)) # Tells the user they guessed wrong and tells them how many times they've guessed total using count.
    print('\nYou guessed it in {0} tries!'.format(count))           # Only if the color is guessed correctly, it'll exit the loop and tell them how many tries it took before they guessed right
    if (count < best_count):                                        # Checks to see if the times it took was less than the best_count.
        print('This was your best guess so far!')                   # If the count was less than best_count, it tells you that this was your best guess so far.
        best_count = count                                          # Sets best_guess equal to count
    play_again = input("\nWould you like to play again? ").lower().strip() # Asks the user if they'd like to play again and awaits their input.
print('Thanks for playing!')                                        # This executes if they say "n" or "no" when being prompted to play again. Tells them thanks for playing.