# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    for char in secret_word:
        if (char in letters_guessed) == False:
            guessed = False
            break
        else:
            guessed = True
    return guessed

#secret_word = 'apple'
#letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
#print(is_word_guessed(secret_word, letters_guessed))


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    correct_guess = []
    guess = ""
    
#    letters_guessed = input("Enter a letter: ")    
    for char in letters_guessed:
        if char in secret_word:
            correct_guess.append(char)
           
    for char in secret_word:
        if char in correct_guess:
            guess += char
        else:
            guess += " _ "
                
    print(guess)
    #guess = ""
    

#letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
#get_guessed_word(secret_word, letters_guessed)

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    import string
    alphabets = string.ascii_lowercase
    remaining = ""
    
    for letter in alphabets:
        if letter not in letters_guessed:
            remaining += letter
    return remaining
    #for letter in letters_guessed:
    #    if letter in alphabets:
    #        alphabets = alphabets.replace(letter, "")
   
    #return alphabets
            
#letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
#print(get_available_letters(letters_guessed))
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    num_guess = 6
    num_warnings = 3
    letters_guessed = []
    duplicate_guesses = []
    #display = "_ " * len(secret_word)
     
    print("   Welcome to the game Hangman!")
    print("   I am thinking if a word that is", len(secret_word), "letters long.")
   
    
    #while the word is not guessed correctly
    while True:
        print("---------------")
        
        #print the number of guesses and warnings left
        print("You have", num_guess, "guesses and",  num_warnings, "warnings")
        
        #display the list of letters available for guessing
        letters_remaining = get_available_letters(letters_guessed)
        print("Letters available: ", letters_remaining)
        
        #Ask the user for input
        user_input = (input("Enter a letter: ")).lower()
        print("Your guess is: ", user_input)
          
       
        #check user input
        #if input is not an alphabet --> minus warnings then guesses
        if not user_input.isalpha():
            if num_warnings > 0:
                num_warnings -= 1
                print("Oops! That is not a valid letter! You have", num_warnings, "warnings and", num_guess, "guesses left.")
            elif num_guess > 0:
                num_guess -= 1
                print("Oops! That is not a valid letter. You have", num_warnings, "warnings and", num_guess, "guesses left.")
            else:
                print("Sorry! You ran out of guess! The word was", secret_word, ".")
                break
        #if input is an alphabet --> check if is already guessed    
        else:
            if user_input not in letters_guessed:
                letters_guessed.append(user_input)
                
            #check is the word is correctly guessed
            word_is_guessed = is_word_guessed(secret_word, letters_guessed)
            
            if word_is_guessed:
                display = get_guessed_word(secret_word, letters_guessed)
                print("Good guess!", secret_word, "is the word.")
                print("Congratulations, you won!")
                print("-------------------")
                break
            
            #check is user input duplicated
            elif user_input in duplicate_guesses:
                if num_warnings > 0:
                    num_warnings -= 1
                    print("Oops! You've already guessed that letter. You have", num_warnings, "warnings and", num_guess, "guesses left.")
                elif num_guess > 0:
                    num_guess -= 1
                    print("Oops! You've already guessed that letter. You have", num_warnings, "warnings and", num_guess, "guesses left.")
                else:
                    print("Sorry! You ran out of guess! The word was", secret_word, ".")
                    break
           
            #check if user_input is in the secret word
            elif user_input in secret_word:
                display = get_guessed_word(secret_word, letters_guessed)
                print("Good guess!")
                print("------------------------")
                
            elif user_input not in secret_word:
                num_guess -= 1
                display = get_guessed_word(secret_word, letters_guessed)
                
                print("Oops! That letter is not in my word!")
                if num_guess == 0:
                    print("Sorry! You ran out of guess! The word was", secret_word, ".")
                    break
        duplicate_guesses.append(user_input)
        print("letters guess: ", letters_guessed )
        print("Duplicate guess: ", duplicate_guesses)            


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
