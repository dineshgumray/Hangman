# Write your code here
import random

print("H A N G M A N")
word_list = ['python', 'java', 'kotlin', 'javascript']
random_word = word_list[random.randint(0, 3)]
check_with_this = random_word

while True:
    user_input = input('Print Type "play" to play the game, "exit" to quit:')
    if user_input == "exit":
        break
    elif user_input != "play":
        continue
    mask_word = '-' * len(random_word)
    make_set = set(random_word)
    lives = 8
    prev_track = set()
    while lives > 0:
        print()
        print(mask_word)
        letter = input("Input a letter: ")
        if len(letter) != 1:
            print("You should input a single letter")

        elif not letter.isalpha() or letter.isupper():
            print("It is not an ASCII lowercase letter")

        elif letter in random_word:
            fposition = random_word.index(letter)
            bposition = random_word.rindex(letter)
            if fposition == bposition:
                mask_word = mask_word[0:fposition]+letter+mask_word[bposition+1:]
            else:
                mask_word = mask_word[0:fposition] + letter + mask_word[fposition + 1:]
                mask_word = mask_word[0:bposition] + letter + mask_word[bposition + 1:]
            random_word = random_word.replace(letter, "_")

        elif letter in make_set or letter in prev_track:
            print("You already typed this letter")

        else:
            lives -= 1
            print("No such letter in the word")

        if mask_word == check_with_this:
            print("You guessed the word!")
            print("You survived!")
            break
        prev_track.add(letter)

    else:
        print("You are hanged!")
