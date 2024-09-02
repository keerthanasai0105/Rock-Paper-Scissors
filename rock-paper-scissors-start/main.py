import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

print("hey! hai, welcome to a fam game ROCK  PAPER  SCISSORS")
index =int(input("ENTER YOUR CHOICE. Type 0 for ROCK , 1 for Paper, 2 for Scissors\n"))

sign=[rock,paper,scissors]
if index not in [0,1,2]:
  print("You choose a wrong option")
else:

 you=sign[index]
 print("Your choice\n"+you)
 com=sign[random.randint(0,2)]
 print("Computer choiice\n"+com)
 
 if you == com :
   print("GAME IS DRAW")
 elif you==rock and com==scissors :
   print("YOU WIN THE GAME")
 elif you==paper and com==rock :
   print("YOU WIN THE GAME")
 elif you==scissors and com==paper :
   print("YOU WIN THE GAME")
 else:
   print("YOU LOST, BETTER LUCK NEXT TIME") 
