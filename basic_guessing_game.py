#Basic Guessing Game

the_word = "football"
guess = ""
guess_count = 0
guess_limit = 5
out_of_guesses = False

while guess != the_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter the word: ")
        guess_count += 1
    else:
        out_of_guesses = True

if(out_of_guesses):
    print("Sorry! You Lost")
else:
    print("Congratulations! You Won")
