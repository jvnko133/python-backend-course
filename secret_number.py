import time
import sys
import random

i = 0
secret_number = 0

while(i < 5):
    text = "GUESS THE NUMBER!"
    print(f"\r{text}", end="", flush=True)
    time.sleep(0.2)
    print("\r" + " " * len(text), end="", flush=True)
    time.sleep(0.2)
    i = i+1

print("\033[31mHello!\033[0m")
print("It's GUESS THE NUMBER game!\n")

while True:
    gamemode = int(input("Enter '1' if you want me to choose number for you.\n" \
    "Enter '2' if you want to choose number by yourself.\n" \
    "Enter '0' if you want to exit.\n"))

    if gamemode == 1:
        guess_number = 0
        secret_number = random.randint(1,10)

        print("I am chosing the number...")
        time.sleep(5)

        while True:
            guess_number = int(input("Enter your guess:\n"))

            if guess_number < secret_number:
                print("Too low!\n")
            elif guess_number > secret_number:
                print("Too high!\n")
            elif guess_number == secret_number:
                print(f"You got it! The secret number was {secret_number}\n\n") 
                time.sleep(2) 

                break

    elif gamemode == 2:
        guess_number = 0
        secret_number = int(input("Enter your secret number: "))

        while True:
            guess_number = int(input("Enter your guess: \n"))

            if guess_number < secret_number:
                print("Too low!\n")
            elif guess_number > secret_number:
                print("Too high!\n")
            elif guess_number == secret_number:
                print(f"You got it! The secret number was {secret_number}\n\n")
                time.sleep(2)  

                break
            
    elif gamemode == 0:
        print("Goodbye\n")
        sys.exit()            
    else:
        print("Pick \033[1;32mONLY GIVEN\033[0m integers to select the game mode.")