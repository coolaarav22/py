import random


def get_user_choice():

    user_choice = str(input("ender your choice (rook,paper,or scissors):")).lower() 


    while user_choice not in ["rock,paper,scissrs"]:

        print("invalid choice. please ender rock,paper,sciessors")
        user_choice = input("ender your choice (rock,paper,sciessors): ").lower

        return user_choice
def play_game():
  
  print("Welcome to Rock, Paper, Scissors!")

  user_choice = get_user_choice()
  computer_choice = get_computer_choice()


  print(f"You chose {user_choice}.")
  print(f"Computer chose {computer_choice}.")



  result = determine_winner(user_choice, computer_choice)
  print(result)



if __name__ == "__main__":
    play_game()
