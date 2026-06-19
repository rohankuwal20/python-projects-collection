import random
print("Welcome to the Number Guessing Game!")
print("let's play a game where you have to guess a number between 1 and 100.")
print("You have 10 attempts to guess the correct number.")
print("Good luck!")
print("---------------------------------------------------")
computer_number = random.randint(1, 100)
attempts = 10
player_guess = 0
is_running= True
while is_running:
    player_guess = input("Enter your guess () : ")
    if attempts == 0:
        print("Sorry, you've run out of attempts. The correct number was:", computer_number)
        break

        
    if not player_guess.isdigit():
        print("enter number between 1 and 100.")
    elif player_guess.isdigit():
        player_guess = int(player_guess)
        if  0<player_guess<101 :
            if player_guess < computer_number:
                print("Your guess is too low. Try again.")
                attempts -= 1
                print(f"{attempts} is left to guess number")
            elif player_guess > computer_number:
                print("Your guess is too high. Try again.")
                attempts -= 1
                print(f"{attempts} is left to guess number")
            elif computer_number == player_guess:
                print(f"Congratulations! You guessed the correct number in {10-attempts+1}attempts!")
                if not input("play again ?(y/n): ").lower()=="y":
                    is_running = False
                    print("thanks for playing!") 
        else :
            print(f"you entered {player_guess},its invalid ")
            print("enter a number betweem 1 to 100.")

            