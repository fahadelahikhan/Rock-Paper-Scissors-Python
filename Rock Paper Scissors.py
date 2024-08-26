from Expressions import Expression
import random

user_choice = int(input("Rock (0), Paper (1) or Scissors (2) ?\n"))

if user_choice > 2 or user_choice < 0:
    print(f"You typed an invalid number. You lose.")
else:
    computer_choice = random.randint(0, 2)

    if (computer_choice == 0 and user_choice == 1 or computer_choice == 2 and user_choice == 0 or
            computer_choice == 1 and user_choice == 2):
        print("You Win !")
    elif (computer_choice == 0 and user_choice == 0 or computer_choice == 2 and user_choice == 2 or
          computer_choice == 1 and user_choice == 1):
        print("Draw !")
    else:
        print("You lose !")

    print(f"Your choice is: {Expression[user_choice]}")
    print(f"Computer choice is: {Expression[computer_choice]}")
