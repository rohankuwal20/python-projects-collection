import random

options = ("rock","paper","scissors")
player_choice = 0
running = True
#print(help(random))
print("welcome to rock,paper and scissor game")
print("-------------good luck----------------")
while running :
    player_choice=input("enter your choice(rock,paper,scissor)! : ")
    computer_choice = random.choice(options)
    if player_choice not in options:
          print("invalid choice ! choose from rock,paper,scissors")
          continue
    print("-----------------------------")
    print(f"computer's choice : {computer_choice}")
    print(f"your's choice : {player_choice}")
    print("-----------------------------")
    if computer_choice == player_choice:
        print("its tie !")
    elif player_choice == "rock" and computer_choice == "scissors" :
        print("you win")
    elif player_choice == "paper" and computer_choice == "rock" :
        print("you win")
    elif player_choice=="scissors"  and computer_choice == "paper":
        print("you win")
    else :
        print("you lose")
    if not input("play again ?(y/n): ").lower()=="y":
                    running = False
                    print("thanks for playing!")     
