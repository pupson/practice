import random
import hangman_art
import hangman_words


words = hangman_words.word_list
word = random.choice(words)
stages = hangman_art.stages
logo = hangman_art.logo

blank_word = []

for letter in range(0, len(word)):
    blank_word += '_'

bad_guess_count = 0
guess_correct = 0
game_over = False

print(logo)

while game_over == False:
    print("\n")
    print(blank_word)
    print("\n")
    guess = input("Welcome to Hangman, guess a letter: ").lower()
    
    print(stages[-bad_guess_count-1])
    if guess not in word:
        print("{} is not in word".format(guess))
        bad_guess_count += 1
        if bad_guess_count > 6:
            print("\nGame over!\n")
            game_over = True
    elif guess in blank_word:
        print("You already guessed that letter, try again.")
    else:
        for lettr in range(0, len(word)):
            letter = word[lettr]
            if letter == guess: 
                blank_word[lettr] = letter
                guess_correct += 1
                if guess_correct == len(word):
                    print("\nYou won! It was {}\n\n".format(''.join(blank_word)))
                    game_over = True
