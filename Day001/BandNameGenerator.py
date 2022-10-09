from pyfiglet import Figlet
from termcolor import colored

f = Figlet(font='big')
print(colored(f.renderText("Band Name Generator"), 'green'))

print(colored("Not sure what should be your band name? Well, let me generate one for you!\n",'red',attrs=["bold"]))

a = input("Which city did you grow up in?\n\u279D ")
b = input("What's the name of your pet?\n\u279D ")
print("An interesting band name for you would be ",end="")
print(colored(a+" "+b, "blue", attrs=["bold"]))
