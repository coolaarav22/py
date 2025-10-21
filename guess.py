import random

lower_bound = 1
upper_bound = 5
max_attempts = 5

secret_number = random.randint(lower_bound , upper_bound)


def get_guess():

    while True:

      guess = int(input(" guess a number between 1 to 5: "))

      if lower_bound <= guess <= upper_bound
              return guess
      else:
               print(" invalid input. please ender within the specifiend range.")


def check_guess(guess , secret_number)
          
   if guess == secret_number
         return "correct"
   elif guess < secret_number:
         return "to low"
   else:
         return
   


def play_game():
         
      attempts = 0
      win = False

      while attempts < max_attempts:
             
       attempts = attempts

       guess = get_guess()

result = check_guess( guess , secret_number)

if result == "correct"
print(f"congratulations! you guessed the secret number [secrets_number] in ")
