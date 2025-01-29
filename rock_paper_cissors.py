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
game_image =[rock, paper, scissors]

user_choice = int(input("0 for rock, 1 for paper or 2 for scissors)\n"))
print(game_image[user_choice])

ia_weapon = random.randint(0, 2)
print ("Ia chose :")
print(game_image[ia_weapon])

if user_choice >= 3 or user_choice < 0:
    print("Invalid number")
elif user_choice == 0 and ia_weapon == 2:
    print("You win")
elif ia_weapon == 0 and user_choice == 2:
    print ('You loose')
elif ia_weapon > user_choice:
    print("You loose!")
elif user_choice > ia_weapon:
    print("You win!")
elif ia_weapon == user_choice:
    print ("Draw !")
0
