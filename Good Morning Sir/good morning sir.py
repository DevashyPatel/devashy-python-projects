#Author: Devashy Patel
#Date: 6/8/2025
import time

timestamp = int(time.strftime("%H"))

if timestamp<12:
    print("Good morning sir")
elif timestamp<18:
    print("Good afternoon")
elif timestamp<21:
    print("Good evening")
else:
    print("Good night")
