import random
def gam():
    n=random.randint(1,10)
    attempts = 5
    while attempts > 0:
        guess = int(input("Enter your guess: "))
        if guess == n:
            print("Congratulations! You guessed the number correctly.")
            break
        elif guess < n:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")
        attempts -= 1
        print("You have", attempts, "attempts left.")
        if attempts == 0:
            print("Sorry, you've used all your attempts. The number was", n)
    
print("Hey Folks! Welcome to the Number Guessing Game!")
print("I will think of a number between 1 and 10, and you have to guess it.")
print("You have 5 attempts to guess the number correctly.")
n=random.randint(1,10)
attempts = 5
gam()
while True:
    Aga=input("Do you want to play again? (yes/no): ")
    if Aga.lower() == "yes":
        print("Great! Let's play again.")
        gam()
    elif Aga.lower() == "no":
        print("Thank you for playing! Goodbye!")
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

        
