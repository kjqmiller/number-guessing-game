# Guess That Number!
## Introduction
Game that generates random number from a predetermined range that the player must guess. Provides additional hints as the player runs out of attempts.

## Why?
I made this project as a way to:
* Build a project from scratch without following along with a tuturial
* Practice my Python coding with a fun project that could be expanded and improved
* Learn how to make a game that could be played on the command line

## Technologies 
* Python 3.9

## Overview
`guessing_game.py` is a command line game in which the player attempts to guess a secret number out of a user defined range. This range is hardcoded into the script and must be set before playing, along with the number of guesses that he player is allowed. The file is broken up into a `main()` function which runs the game, as well as several helper functions. These helper functions are `hint()`, `wrong_guess()`, `get_guess()`, and `play_again()`.

### main()
`main()` gets a guess from the player, then checks if the guess is equal to the secret number. If correct it tells the player their guess was right, and then asks if they want to play again. If the guess is wrong the guess count is incrementet and the player is told if their guess is too high or too low. 

### hint()
`hint()` accepts `guess` as an argument and provides the user with hints as the begin to run out of guesses. There are two different hints. One that tells the player if they are within a set range of the secret number, and another at the end of the game which tells the player if the secret number is even or odd.

### wrong_guess()
`wrong_guess()` accepts `guess` as an arguement and increments the guess count upon a wrong guess. It also tells the player how many out of their total guesses they have made, and provides a hint if they are running out of guesses.

### get_guess()
`get_guess()` accepts the bounds `min_num` and `max_num` as arguments. It verifies that the player's input is both an integer and not outside the bounds of the secret number range. If the guess is not valid, player is prompted to guess again.

### play_again()
`play_again()` asks the player if they'd like to play again after finishing a game. If they choose to play gain, `guess_count` and `secret_number` are reset, and the game begins again. If they choose not to play again, they are thanked and the program ends.

## Key Lessons Learned
* I learned how to add additional functionality, such as the hint mechanic, to an otherwise working project.
* Initially the secret number range and guess limit were both hardcoded. I quickly found out that this makes changing things much harder and that using variables to change them from a single spot is much easier and more flexible.
* The first iteration of this project quickly became hard to understand because I did not break it up into multiple functions. By separating things out I was able to write code that was much easier to read and make changes to.
