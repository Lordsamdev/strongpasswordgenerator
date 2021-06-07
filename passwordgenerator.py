from random import choice # Imports the choice function from random

alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o"]  # List of lowercase characters
# from a to o
alph_upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"]  # List of uppercase characters
# from A to O

file_name = "/Users/SAMUEL OLUBIYO O/Documents/strongpasswords.txt"  # file directory for the text file to contain
# the generated passwords
number = list(range(1, 11)) # List of numbers from 1 to 10
symbols = ["/", "@", "#", "$", "%", "&", "?", "*"]  # List of symbols

password_sequence = f"{choice(alpha)}{choice(alph_upper)}{choice(number)}{choice(symbols)}" \
                    f"{choice(number)}{choice(alpha)}{choice(symbols)}{choice(number)}{choice(alph_upper)}" \
                    f"{choice(symbols)}\n"

with open(file_name, "a") as file_object:  # appending the generated passwords to a text file
    file_object.write(password_sequence)
    print(password_sequence)

# Author: OLUBIYO SAMUEL A
# Github @ Lordsamdev



