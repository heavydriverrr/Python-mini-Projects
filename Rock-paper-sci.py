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
game_img = [rock, paper, scissors]
user_input = int(input("to play,"
                   "choose 0 for rock, 1 for paper, 2 for scissor\n"))
if user_input < 0 or user_input > 2:
    print("Invalid input, __You lose!")
else:
    print(f'''you chose : {user_input}\n
            {game_img[user_input]}''')
    comp_choice = int(random.randint(0,2))
    print(f'''computer chose : {comp_choice}\n
            {game_img[comp_choice]}''' )
    if user_input == 0 and comp_choice == 2:
        print("You Win!")
    elif user_input == 0 and comp_choice == 1:
        print("_You lose!_")
    elif user_input == 1 and comp_choice == 0:
        print("You Win!")
    elif user_input == 1 and comp_choice == 2:
        print("_You lose!_")
    elif user_input == 2 and comp_choice == 1:
        print("You Win!")
    elif user_input == 2 and comp_choice == 0:
        print("_you lose!_")
    else:
        print("it's a draw")