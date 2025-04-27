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

player_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
pc_choose = random.randint(0, 2)
game_images = [rock, paper, scissors]

print(game_images[player_choose])
print(f"PC choose:\n" + game_images[pc_choose])

if player_choose == pc_choose:
    print("Draw")


if player_choose == 0 and pc_choose == 2:
    print("You win!")
if player_choose == 1 and pc_choose == 0:
    print("You win!")
if player_choose == 2 and pc_choose == 1:
    print("You win!")


if player_choose == 2 and pc_choose == 0:
    print("You lost!")
if player_choose == 0 and pc_choose == 1:
    print("You lost!")
if player_choose == 1 and pc_choose == 2:
    print("You lost!")