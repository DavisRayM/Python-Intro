# importing randint function
# from random module
from random import randint
#creating a class to store the games function
class NumberGuesser:
    def __init__(self):
        pass

# Function which generates a new
# random number everytime it executes
    def generator(self):
        return randint(10,10)

    # Function takes user input and returns
    # true or false depending whether the
    # user wins the lucky draw!
    def rand_guess(self):

        # calls generator() which returns a
        # random integer between 10
        random_number = self.generator()

        # defining the number of
        # guesses the user gets
        guess_left = 3

        # Setting a flag variable to check
        # the win-condition for user
        flag = 0

        # looping the number of times
        # the user gets chances
        while guess_left > 0:

            # Taking an input from the user
            guess = int(input("Pick your number to "
                        "enter the lucky draw\n"))

            # checking whether user's guess
            # matches the generated win-condition
            if guess == random_number:

                # setting flag as 1 if user guessses
                # correctly and then loop is broken
                flag = 1
                print("Congrats!! You Win.")
                break


            else:

                # If user's choice doesn't match
                # win-condition then it is printed
                print("Guessed number is higher than the actual number")

            # Decrementing number of
            # guesses left by 1
            guess_left -= 1

        # If win-condition is satisfied then,
        # the function rand_guess returns True
        if flag is 1:
            return True

        # Else the function returns False
        else:
            return False


if __name__ == '__main__':
	NumberGuesser().rand_guess()