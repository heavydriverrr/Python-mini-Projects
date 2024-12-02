import random
from hangman_wlist import word_list
from hangman_art import stages,logo

lives = 6
chose_word = random.choice(word_list)
print(logo)
#--
placeholder = ""
word_lent = len(chose_word)
for position in range(word_lent):
    placeholder += "_"
print(placeholder)
#--

#---
game_over = False
correct_letters = []

while not game_over:

    print(f"*****<???>/{lives} lives left******")
    guess = input("guess letter: ").lower()

    if guess in correct_letters:
        print(f"you've already guessed {guess}")
    #----
    display = ""
    for letter in chose_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)
#-------
    if guess not in chose_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print(f"************|you lose|->It's '{chose_word}' *************")

    if "_" not in display:
        game_over = True
        print("*************|you win|**************")

    print(stages[lives])
