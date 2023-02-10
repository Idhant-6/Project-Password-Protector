import imp
import os
import pyautogui
from termcolor import colored
import time

os.system('color')

password = "Password"
project_start = False

confirm = pyautogui.prompt("Your Password?")
if confirm == password:
    pyautogui.alert(
        "You Entered the Right Passoword, get the Administrator Rights :P")
    print(colored("Administrator Rights Granted!", "green"))
    project_start = True

elif confirm != password:
    pyautogui.alert(
        "You entered the Wrong Password... Try Again if you know the password??")
    print(colored("Administrator Rights didn't Granted...Try Again...", "red"))
    project_start = False
else:
    print("Invalid Input, Please input the password again...")


while project_start:
    print("Python OOPS Training Camp")

    class Instagram:
        def __init__(self, user_id, username):
            self.id = user_id
            self.username = username
            self.followers = 0
            self.following = 0

        def follow(self, user):
            user.followers += 1
            self.following += 1

    Idhant = Instagram("0", "Idhant Singh")
    Taylor = Instagram("1", "Taylor Swift")
    Shawn = Instagram("2", "Shawn Mendes")
    Justin = Instagram("3", "Justin Bieber")
    Ariana = Instagram("4", "Ariana Grande")

    print(Idhant.following, Taylor.following,
          Shawn.following, Justin.following, Ariana.following)
    print(Idhant.followers, Taylor.followers,
          Shawn.followers, Justin.followers, Ariana.followers)
    print(Idhant.username, Taylor.username,
          Shawn.username, Justin.username, Ariana.username)
    print(Idhant.id, Taylor.id, Shawn.id, Justin.id, Ariana.id)

    Idhant.follow(Taylor)
    Idhant.follow(Justin)
    Justin.follow(Idhant)
    Taylor.follow(Ariana)
    Shawn.follow(Taylor)
    Taylor.follow(Idhant)

    print(Idhant.following, Taylor.following,
          Shawn.following, Justin.following, Ariana.following)
    print(Idhant.followers, Taylor.followers,
          Shawn.followers, Justin.followers, Ariana.followers)
    break

time.sleep(6)


os.system('color')

password = "idhant@007"
project_start = False

confirm = pyautogui.prompt("Your Password?")
if confirm == password:
    pyautogui.alert(
        "You Entered the Right Passoword, get the Administrator Rights :P")
    print(colored("Administrator Rights Granted!", "green"))
    project_start = True

elif confirm != password:
    pyautogui.alert(
        "You entered the Wrong Password... Try Again if you know the password??")
    print(colored("Administrator Rights didn't Granted...Try Again...", "red"))
    project_start = False


while project_start:
    print("Python OOPS Training Camp")

    class Instagram:
        def __init__(self, user_id, username):
            self.id = user_id
            self.username = username
            self.followers = 0
            self.following = 0

        def follow(self, user):
            user.followers += 1
            self.following += 1

    Idhant = Instagram("0", "Idhant Singh")
    Taylor = Instagram("1", "Taylor Swift")
    Shawn = Instagram("2", "Shawn Mendes")
    Justin = Instagram("3", "Justin Bieber")
    Ariana = Instagram("4", "Ariana Grande")

    print(Idhant.following, Taylor.following,
          Shawn.following, Justin.following, Ariana.following)
    print(Idhant.followers, Taylor.followers,
          Shawn.followers, Justin.followers, Ariana.followers)
    print(Idhant.username, Taylor.username,
          Shawn.username, Justin.username, Ariana.username)
    print(Idhant.id, Taylor.id, Shawn.id, Justin.id, Ariana.id)

    Idhant.follow(Taylor)
    Idhant.follow(Shawn)
    Justin.follow(Idhant)
    Taylor.follow(Ariana)
    Shawn.follow(Taylor)
    Taylor.follow(Idhant)

    print(Idhant.following, Taylor.following,
          Shawn.following, Justin.following, Ariana.following)
    print(Idhant.followers, Taylor.followers,
          Shawn.followers, Justin.followers, Ariana.followers)
    break

time.sleep(6)
