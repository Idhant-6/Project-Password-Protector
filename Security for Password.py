import imp
import pyautogui
from termcolor import colored

password = "YOUR_PASSWORD_HERE"
project_start = False

confirm = pyautogui.prompt("Your Password?")
if confirm == password:
    pyautogui.alert("You Entered the Right Passoword, get the Administrator Rights :P")
    print(colored("Administrator Rights Granted!", "green"))
    project_start = True

elif confirm != password:
    pyautogui.alert("You entered the Wrong Password... Try Again if you know the password??")
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


    Idhant = Instagram("6", "Idhant Singh")
    Taylor = Instagram("7", "Taylor Swift")
    Shawn = Instagram("8", "Shawn Mendes")
    Justin = Instagram("9", "Justin Bieber")

    print(Idhant.following, Taylor.following, Shawn.following, Justin.following)
    print(Idhant.followers, Taylor.followers, Shawn.followers, Justin.followers)
    print(Idhant.username, Taylor.username, Shawn.username, Justin.username)
    print(Idhant.id, Taylor.id, Shawn.id, Justin.id)

    Idhant.follow(Taylor)
    Idhant.follow(Shawn)
    Justin.follow(Idhant)
    # Shawn.follow(Taylor)
    # Taylor.follow(Idhant)

    print(Idhant.following, Taylor.following, Shawn.following, Justin.following)
    print(Idhant.followers, Taylor.followers, Shawn.followers, Justin.followers)
    break


