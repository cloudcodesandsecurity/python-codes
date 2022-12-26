# Dictionary list to pick user's choice
list_choices = {'Letters in a word': "letter",
                'Numbers in a figure': "number",
                'Total number of words in a sentence': "sentence"
                }
# User's input as choice
users_choice = input("What do you want to count? 'Letters in a word', 'Numbers in a figure' "
                     "or 'Total number of words in a sentence'? ")


# Python functions
def letter():
    your_word = input("Type the word: ")
    letters_in_word = str(len(your_word))
    print("The number of letters in your word: " + your_word + " \n" + "is: " + letters_in_word)

def number():
   # User's number choice
    your_number = print("Type the numbers or give a range of number '0: as first, 100: as second': ")
    print("Type the first number and hit enter")
    first_number = int(input())
    print("Type the first number and hit enter")
    second_number = int(input())
   # Placing User's choice in a python range
    range_number = range(first_number,second_number)
   # Converting to string
    frange_number = str(range_number)
   # Calculating the length in the numbers
    total_numbers = len(range_number)
   # Converting to string
    ftotal_numbers = str(total_numbers)
    print("The total numbers in your given range of numbers: " + frange_number + " \n" + "is: " + ftotal_numbers)

def sentence():
    instruction = print("Copy and paste the sentence")
    copied_sentence = input("Paste the copied sentence: ")
    pasted_sentence = len(copied_sentence.split())
    fpasted_sentence = str(pasted_sentence)
    print("The total words in your sentence: " + copied_sentence + " \n" + "is: " + fpasted_sentence)


# If .... Elif and  Else statements
if list_choices[users_choice] == 'letter':
    letter()

elif list_choices[users_choice] == 'number':
    number()

elif list_choices[users_choice] == 'sentence':
    sentence()

else:
    print("You have selected a wrong option!")
