# 6.00 Problem Set 3
# 
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"
def get_guess():
    ''' gets the guessed letter from player '''
    guess = raw_input("\n\n  Please guess a letter: ").lower()
    return guess

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    #print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    
    
    #print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------
# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program

wordlist = load_words()
print "\n\n\t\tWelcome to the game, Hangman! ".upper()

# your code begins here!
word = choose_word(wordlist)
length = len(word)
max_attempts = length + 1
available_letters = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
    
def del_alphabeth(alphabeth,choice_range):
    if alphabeth in choice_range:
       letters_remaining = string.replace(choice_range,alphabeth,"_ ")
       return letters_remaining

def progress_so_far(word,guessed_letters):
    newstring = []
    for index in range(len(word)):
        letters = word[index]
        if letters in guessed_letters:
            newstring.append(letters)
        else:
            newstring.append("_")
    return newstring

# Print game headers 
##print word
print "  I am looking for a word that contains", length, " letters"
print "  ---------------"
print "  You have", max_attempts, "guesses to make."
print "  Available letters: ", available_letters

def eval_guess(guess,word):
    ''' Gets guess from player,checks if 
    word contains the guess and print progress made
    so far, else return failure report '''

    max_attempts = length + 1
    available_letters = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
    guessed_letters = []
    newstring = []
    correct_guesses = 0
    wrong_guesses = 0

    while True  and max_attempts > 1:
        # Ensures that only a single alphabeth is entered at a time 
        if (guess == '' or len(guess) > 1) : # 
            print "  Guess must be a single letter !"
            guess = get_guess()
        # Prevents guessing any letter more than once
        if guess in guessed_letters:
            print " This letter has been guessed!"
            guess = get_guess()
            
        else:
            guessed_letters.append(guess)
            # performs the actual check for the guessed letter in the word

            if guess not in word:
                print "   Opps!", guess, "is not in the word"
                print "   -----------------"
                max_attempts -= 1  
                print "  you have ", max_attempts, "attempts left"
                available_letters = del_alphabeth(guess,available_letters)
                print "  Available letters: ", available_letters
                wrong_guesses += 1
                guess = get_guess()

            else:  
                print "   Good guess: '", guess, "' appeared", word.count(guess), "times"
                print "   progress so far: ", progress_so_far(word,guessed_letters)
                available_letters = del_alphabeth(guess,available_letters)
                print "\n  Available Letters:  ", available_letters

                correct_guesses += word.count(guess) # gets 
                if  correct_guesses == length:
                    print " \n\n\t\t Great Job! the word is ", word.upper(), "!!!"
                    print "\t\t wrong guesses: ",wrong_guesses
                    break
                else:
                    guess = get_guess()
    else:
        print "\n\t ************************************"
        print "\t\t\t\tGame Over!".upper() # terminate the game
        print "\t ************************************"
        print "\n\t\t The word is ", word.upper()
        exit()

guess = get_guess()
eval_guess(guess,word)
