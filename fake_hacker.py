import time
import random
import os

text = "\033[1;92mFAKE HACKER TERMINAL!\033[0m"
for i in range(1,6):
    print(text, end="\r", flush=True)
    time.sleep(0.2)

    print(" " * len(text), end = '\r', flush=True)
    time.sleep(0.2)

    i = i+1


print("connected to address.\n")
time.sleep(1)

print("username: ", end="", flush=True)
time.sleep(0.3)
for i in range(9):
    print("\033[32m*\033[0m", end="", flush=True)
    time.sleep(0.2)
time.sleep(0.3)
print("\n")

text = "\033[91mUNKNOWN!\033[0m"
print("password: ", end="")
time.sleep(1)
for letter in text:
    print(letter, end="", flush=True)
    time.sleep(0.05)
time.sleep(3)

print("\033[2J\033[H", end="")

text = "\033[1;92mPASSWORD CONTAINS 4 SYMBOLS AND THEY ALL ARE NUMBERS!\033[0m"
for i in range(1,6):
    print(text, end="\r", flush=True)   
    time.sleep(1)

    print(" " * len(text), end = '\r', flush=True)
    time.sleep(1)

    i = i+1

password = str(random.randint(1000,9999))
gPassword = 0
attempts = 0

while True:
    if attempts > 10:

        print("\033[2J\033[H", end="")
        print("ACCESS DENIED!")
        time.sleep(2)
        print("\033[2J\033[H", end="") 

        text = "\033[91mGAME OVER\033[0m"
        for i in range(1,6):
            print(text, end="\r", flush=True)   
            time.sleep(1)
            print(" " * len(text), end = '\r', flush=True)
            time.sleep(1)
            i = i+1
        break
        
    gPassword = input("> Enter password:\n> ")
    if gPassword == password :
        print("ACCESS GRANTED!")
        break

    elif gPassword != password :
        attempts = attempts + 1
        print(f"WRONG PASSWORD. TRY AGAIN\nAttempt №{attempts}")

        for i in range(4):
            if gPassword[i] == password[i]:
                print(gPassword[i], "- correct digit and position")
            elif gPassword[i] in password:
                print(gPassword[i], "- correct digit, wrong position")
            else:
                print(gPassword[i], "- wrong digit")
        

