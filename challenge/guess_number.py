import random

secret_number = random.randint(1, 20)

def guess_number():
    print('You have 6 chances to guess the number.')
    for guess_taken in range(1, 7):
        try:
            guess = int(input('Take a guess: '))

            if guess < secret_number:
                print('Your guess is too low.')
            elif guess > secret_number:
                print('Your guess is too high.')
            else:
                break
        except ValueError:
            print('You did not type a number.')
        finally:
            print(f'You have {6 - guess_taken} chances left.\n')

    return guess, guess_taken


if __name__ == "__main__":
    name = input('Hello. What is your name? ')
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    guess, guess_taken = guess_number()
    
    if guess == secret_number:
        print(f"Good job, {name}! You guessed my number in {guess_taken} guesses.")
    else:
        print(f"Nope. The number I was thinking of was {secret_number}")