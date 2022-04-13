import random
class NumberGuesser:
    def __init__(self):
        self.guess = 10
        self.count = 0

    def random_number(self,user_input):
        while True:
            self.count +=1
            if user_input > self.guess :
                raise ValueError("Guessed number is higher than the actual number")

            elif user_input < self.guess:
                raise ValueError("Guessed number is lower than the actual number")
            break
        print("Congrats! You guessed right")

if __name__ == "__main__":
    NumberGuesser().random_number(50)