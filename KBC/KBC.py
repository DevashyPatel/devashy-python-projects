#Authur: Devashy Patel
#Date: 12/6/2025

questions = ["Who is the current president of the USA?","How many bones are there in adult human body?","Which year was the last olympic"]
cans = ["Donald Trump","206","2024"]
total_points = 0
for i in questions:
    print(i)
    ans = input()
    if ans == cans[questions.index(i)]:
        total_points = total_points + 1
if total_points == 0:
    print("You won nothing unfotunately")
elif total_points == 1:
    print("You won 10000$")
elif total_points == 2:
    print("You won 20000$")
elif total_points == 3:
    print("Congratulations you won 100,000$")