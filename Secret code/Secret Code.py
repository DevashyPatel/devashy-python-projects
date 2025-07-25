#Author: Devashy Patel
#Date: 17/6/2025
import random

def reverse_word(word):
    reversed_word = ""
    for char_index in range(len(word) - 1, -1, -1):
        reversed_word += word[char_index]
    reversed_word += " "
    return reversed_word

ch = int(input("Enter 1 to encode and 2 to decode: "))
if ch!= 1 and ch!= 2:
    raise ValueError("Invalid input")

statement = input("Enter the statement to which the task is to be performed: ")
words = statement.split()
new_statement = ""

if ch == 1:
    for word in words:
        if len(word) <= 3:
            new_statement += reverse_word(word)
        else:
            new_statement += f"{random.choice(word[1:])}{random.choice(word[1:])}{random.choice(word[1:])}{word[1:]}{word[0:1]}{random.choice(word[1:])}{random.choice(word[1:])}{random.choice(word[1:])} "
elif ch == 2:
    for word in words:
        if len(word) <= 3:
            new_statement += reverse_word(word)
        else:
            new_statement += f"{word[-4:-3]}{word[3:-4]} "

print(new_statement)