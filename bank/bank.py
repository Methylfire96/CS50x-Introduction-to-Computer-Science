from sys import argv
from cs50 import get_string

greetings = get_string("Greetings: ")

if "hello" in greetings.isalpha:
    print("0$")
if "H" or "h" in greetings[0]:
    print("20$")
else:
    print("100$")
