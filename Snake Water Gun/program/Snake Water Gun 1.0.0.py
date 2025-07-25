#Author: Devashy Patel
#Date: 24/6/25

"""Snake, Water and Gun is a variation of the children's game "rock-paper-scissors" where players use hand
 gestures to represent a snake, water, or a gun. The gun beats the snake, the water beats the gun, and the
  snake beats the water. Write a python program to create a Snake Water Gun game in Python using if-else
statements. Do not create any fancy GUI. Use proper functions to check for win."""

import random
import time
import sys
import winsound

def type_text(text, delay=0.02):
    winsound.Beep(440, 500)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


type_text("""===========================================
           WELCOME TO THE BATTLE!
===========================================

                🐍 SNAKE
                💧 WATER
                🔫 GUN

         Choose wisely. Play smart.
         Outsmart the computer!

-------------------------------------------
🔹 Press [1] to Start Game
🔹 Press [2] for How to Play
🔹 Press [3] to Exit
-------------------------------------------

     Developed by: Devashy Patel
         Version: 1.0.0
===========================================
            """)
action = int(input("   Enter input :"))


while action != 3:
 if action == 1:
  score = 0
  for i in range(3):

         type_text(f"""
                   BATTLE: {i+1}
         Enter the attack you want to use--
                🐍 SNAKE press [1]
                💧 WATER press [2]
                🔫 GUN   press [3]
         """)
         attack = int(input(" Enter input :"))
         counter = random.randint(1, 3)
         if attack == 1 and counter == 2:
             type_text("🐍 Snake drinks 💧 Water → ✅ YOU WIN!")
             score += 1
         elif attack == 2 and counter == 3:
             type_text("💧 Water douses 🔫 Gun → ✅ YOU WIN!")
             score += 1
         elif attack == 3 and counter == 1:
             type_text("🔫 Gun shoots 🐍 Snake → ✅ YOU WIN!")
             score += 1
         elif attack == counter:
             type_text("🤝 Both chose the same → It's a TIE!")
         elif attack == 2 and counter == 1:
             type_text("💧 Water gets drunk by 🐍 Snake → ❌ YOU LOSE!")
             score -= 1
         elif attack == 3 and counter == 2:
             type_text("🔫 Gun gets doused by 💧 Water → ❌ YOU LOSE!")
             score -= 1
         elif attack == 1 and counter == 3:
             type_text("🐍 Snake gets shot by 🔫 Gun → ❌ YOU LOSE!")
             score -= 1

         time.sleep(1)
  if score > 0:
      type_text(f"\n🏆 Final Score: {score} → 🎉 YOU WON THE BATTLE! 🐍💧🔫")
  elif score == 0:
      type_text(f"\n⚖️ Final Score: {score} → 🤝 IT WAS A DRAW!")
  elif score < 0:
      type_text(f"\n💀 Final Score: {score} → ❌ YOU LOST THE BATTLE!")
  time.sleep(1)
  break
 elif action == 2:
     type_text("""
     📜 HOW TO PLAY:

     This is a 3-round game based on the classic "Rock-Paper-Scissors" concept,
     but with a twist!

     Choices:
         🐍 Snake
         💧 Water
         🔫 Gun

     RULES:
         🔫 Gun shoots 🐍 Snake → Gun wins
         💧 Water douses 🔫 Gun → Water wins
         🐍 Snake drinks 💧 Water → Snake wins

     INSTRUCTIONS:
     1. You will play 3 rounds against the computer.
     2. Each round, choose one option: Snake [1], Water [2], or Gun [3].
     3. The winner is determined by the rules above.
     4. Your score increases by 1 for a win, decreases by 1 for a loss.
     5. Final score will be shown after 3 rounds.

     🎯 Outsmart the computer and win the battle!
     """)
     time.sleep(1)
     break

type_text("\n\nHope you enjoyed playing the Game😊")
exit()