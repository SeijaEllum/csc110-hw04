# ------------------------------------------------------
#        Name: Seija Ellum
#       Peers: (add any collaborators)
#  References: (anything you checked to solve this)
# ------------------------------------------------------
import sys

secret_word = "food"

# Task 1
def check_text():
    """ Ask for a sentence and then see if it contains the secret word or Dog  """
    while True:
    #input sentence
        text = input("Give me a sentence: ")
    #check for secret word
        if secret_word in text:
            print("You used the secret word!")
            break
    #check for dog
        elif "dog" in text.lower():
            print("You used the word \"dog\" or the word \"Dog\"!")
            break
    #if neither
        else:
            print("Try again")

# Task 2
def check_greater():
    """ Ask for two integers and then see which is greater """
    while True:
    #input one number
        num1 = int(input("Give me an integer: "))
    #input a second number
        num2 = int(input("Give me another integer: "))
    #if first integer is greater
        if num1 > num2:
            print("First is Greater")
            break
    #if second integer is greater
        elif num1 < num2:
            print("Second is Greater")
            break
    #if the integers are equal
        else:
            print("Try again")
    

# Task 3
def get_special_numbers():
    """Print numbers between 1 and 40 that meet the requirements """
    for num in range(1, 41):
        if num % 2 == 0:
            continue
        if num % 3 != 0:
            continue
        if num % 5 == 0:
            continue
        print(num)


# Task 4.a
def my_for_loop():
    """ Check each letter in a valid word """
    word = input("Enter a word: ")

    # check if word length is invalid or it has spaces
    if len(word) < 2 or len(word) > 5:
        print("bad word")
        return
    if " " in word:
        print("bad word")
        return

    # Check each letter for vowel or consonant
    for let in word:
        if let.lower() in "aeiou":
            print(f"{let} is a vowel")
        else:
            print(f"{let} is a consonant")

# Task 4.b
def my_while_loop():
    """ check inputted letter for a, b, or c """
    #input letter
    while True:
        letter = input("Choose a, b, or c: ")
        #if a
        if letter == "a":
            continue
        #if b
        elif letter == "b":
            print("Goodbye")
            return
        #if c
        elif letter == "c":
            exit()
        #if other letter
        else:
            print("try again")

# ---------------------------------------
# Do not modify anything below this line
# ---------------------------------------

def main():

    # Task 1 calls
    check_text()

    # Task 2 calls
    check_greater()

    # Task 3 calls
    get_special_numbers()

    # Task 4 calls
    my_for_loop()
    my_while_loop()

if __name__ == "__main__":
    main()
    print("The End")
