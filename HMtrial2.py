import random
import re
import time


guessed_letters = []

hm_word = ""


def main():
    hm_word = difficulty_choice()
    n = 0
    while True:
        if n <= 7:
            guess = letter_guess()
            skip = skipturn(guess, hm_word)
            if skip is True:
                n += 0
            elif not skip:
                n += 1
            replace_uscore(hm_word)
            print(n)
            HM_print(n, hm_word)
        """else:
            print("The word was " + hm_word.strip() + ".")
            print("Try again!")
            time.sleep(3)
            quit()"""



def difficulty_choice():
    while True:
        difficulty_choice = input("What would you like the difficulty to be? Easy (E) or Hard (H). ")

        difficulty_easy = bool(
                    re.match("E", difficulty_choice, re.I) or difficulty_choice == re.match("EASY", difficulty_choice, re.I))
        difficulty_hard = bool(
                    re.match("H", difficulty_choice, re.I) or difficulty_choice == re.match("HARD", difficulty_choice, re.I))

        if difficulty_easy is True:
            easy_word_list = []
            wordlist = open('HMWordsEasy.txt', 'r')
            for word in wordlist:
                easy_word_list.append(word)
            hm_word = random.choice(easy_word_list)
            number_of_characters(hm_word)
            return hm_word
        elif difficulty_hard is True:
            hard_word_list = []
            wordlist = open('HMWordsHard.txt', 'r')
            for word in wordlist:
                hard_word_list.append(word)
            hm_word = random.choice(hard_word_list)
            number_of_characters(hm_word)
            return hm_word
        else:
            print("You must choose 'E' for Easy or 'H' for Hard.")


def number_of_characters(hm_word):
    num_of_characters = ""
    for character in hm_word.strip():
        if character == " ":
            num_of_characters += " "
        elif character != " ":
            num_of_characters += "_"
    print(num_of_characters)
    # print(hm_word)
    return num_of_characters


def letter_guess():
    while True:
        guess = input("Guess a letter. ")
        if not re.match(r'^[a-z]$', guess, re.I):
            time.sleep(0.5)
            print("Please guess a single letter.")
        else:
            return guess



def replace_uscore(hm_word):
    newnoc: str = ""
    for character in hm_word.strip():
        if character in guessed_letters:
            newnoc += character
        else:
            newnoc += "_"
    print("Letters you have guessed: ")
    time.sleep(0.5)
    print(guessed_letters)
    time.sleep(0.5)
    print(newnoc)
    wincons(newnoc)
    return newnoc


def wincons(newnoc):
    wincon1 = newnoc.isalpha()
    if wincon1 is True:
        print("Great job!  You saved the hangman!")
        print("""
______
|    |  
|    0
|   /|\\
|   / \\   \\
|__________\\
             """)
        time.sleep(3)
        quit()


def skipturn(guess, hm_word):
    if guess in guessed_letters:
        print("You have already guessed that letter, try another.")
        time.sleep(0.5)
        skip = True
        return skip
    elif guess in hm_word:
        skip = True
        guessed_letters.append(guess)
        return skip
    else:
        guessed_letters.append(guess)
        skip = False
        return skip


def HM_print(n, hm_word):

    if n == 0:
        print("""
______
|    
|    
|   
|          \\
|___________\\
        """)
        time.sleep(1)
    elif n == 1:
        print("""
______
|    |  
|    
|   
|          \\
|___________\\
        """)
        time.sleep(1)
    elif n == 2:
        print("""
______
|    |  
|    0
|   
|          \\
|___________\\
        """)
        time.sleep(1)

    elif n == 3:
        print("""
______
|    |  
|    0
|    |
|          \\
|___________\\
        """)
        time.sleep(1)
    elif n == 4:
        print("""
______
|    |  
|    0
|    |\\
|          \\   
|___________\\
        """)
        time.sleep(1)
    elif n == 5:
        print("""
______
|    |  
|    0
|   /|\\
|          \\  
|___________\\
        """)
        time.sleep(1)
    elif n == 6:
        print("""
______
|    |  
|    0
|   /|\\
|     \\    \\
|___________\\
        """)
        time.sleep(1)
    elif n == 7:
        print("""
______
|    |  
|    0
|   /|\\
|   / \\   \\
|__________\\
        """)
    elif n == 8:
        print("""
______
|    |  
|    |
|    |   
|    0      /
|_  /|\\  __/
  | / \\
  |           """)
        time.sleep(1)
        print("The word was", hm_word)
        print("You failed to save the hangman!  Try again next time!")
        time.sleep(10)
        quit()


if __name__ == "__main__":
    main()
