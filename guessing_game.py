import random

# Initialize secret number, guess limit/count, and game state
secret_number = random.randint(0, 100)
guess_limit = 5
guess_count = 0
game_over = False

# Main function
def main():
    print('Guess the secret number between 1 and 100, you have 5 chances!')
    guess = None

    while not game_over:
        # Get user guess
        guess = get_guess()

        # Check guess
        if guess != secret_number:
            if guess_count == (guess_limit - 1):
                print(f'Out of guesses, game over! The secret number was {secret_number}')
                play_again()
                continue
            if guess < secret_number:
                print('Higher! Try again')
                wrong_guess(
                    guess)  # guess_count getting incremented here, but still getting higher/lower if guess 5 wrong
                continue
            elif guess > secret_number:
                print('Lower! Try again')
                wrong_guess(guess)
                continue
        else:
            # Notify of correct guess, ask to play again
            print(f'Correct! The secret number was {secret_number}.')
            play_again()

# Functions
def hint(guess):
    global guess_count
    global guess_limit
    global secret_number

    upper_range = secret_number + 6
    lower_range = secret_number - 5
    if guess_count >= (guess_limit - 3) and guess_count != 5:
        if guess in range(lower_range, upper_range + 1):
            print('Hint: your guess was within 10 of the secret number.')
        else:
            print('Hint: your guess is more than 10 away from the secret number.')

    if guess_count >= (guess_limit - 1) and guess_count != 5:
        if secret_number % 2 == 0:
            print('Hint: the secret number is even.')
        else:
            print('Hint: the secret number is odd.')

def wrong_guess(guess):
    global guess_count
    guess_count += 1
    if guess_count != 5:
        hint(guess)
        print(f'You have used {guess_count}/{guess_limit} guesses\n')


def get_guess():
    while True:
        player_guess = input('Guess a number: ')
        if player_guess.isnumeric():
            return int(player_guess)
        else:
            print('That is not a valid guess, please guess a number.')
            continue


def play_again():
    while True:
        again = input('Would you like to play again? (y/n)?: ')
        if again == 'y':
            global secret_number
            secret_number = random.randint(0, 100)
            global guess_count
            guess_count = 0
            break
        elif again == 'n':
            print('Thanks for playing!')
            global game_over
            game_over = True
            break
        else:
            print('Please type either y or n.')

if __name__ == '__main__':
    main()