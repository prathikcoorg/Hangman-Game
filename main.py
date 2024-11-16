import random
from hangman_words import word_list
from hangman_art import stages,logo

print(logo)
chose_word = random.choice(word_list)

lives = 6


chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    print(f"****************************{lives}<???>/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"you already guessd {guess}")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)



    if guess not in chosen_word:
        lives -= 1
        print(f"you guessed  z{guess}  that not in words you lose a life")

        if lives == 0:
            game_over = True
            print("you lose ")

            print(f"***********************it was {chose_word} thats why YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages[lives])
