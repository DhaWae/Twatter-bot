from time import sleep
from app.twatter import run
import os


def main():
    if not os.path.exists(os.getcwd() + "/credential.txt"):
        with open("credential.txt", "w"):
            pass
        print("Enter username and password in credential.txt.")
        print("Program will exit in 2 seconds")
        sleep(2)
        quit(1)
    print("Heey What do you wanna spam today?")
    spam = input()
    print("Thank you. We will start it in a few seconds")
    sleep(2)
    run(spam)


if __name__ == '__main__':
    main()
