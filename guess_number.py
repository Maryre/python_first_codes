from random import randint

class Die():
    """A class for representing a single die and getting user number"""

    def __init__(self, num_sides=6):
        """a six side die"""
        self.num_sides = num_sides

    def roll(self):
        """return a random number between 1 to 6"""
        rand_num = randint(1, self.num_sides)
        return rand_num

    def get_input(self):

        try:
            user_number = int(input("\nGuess what's the number: "))
        except ValueError:
            print("Please enter a valid number!!")
            user_number = int(input("\nGuess what's the number: "))
        return user_number


class CheckNum():

    """A class for checking the user input"""

    def __init__(self, random_number, user_number):
        self.user_input = user_number
        self.random_number = random_number

    def check_number(self):
        die = Die()

        if self.user_input not in range(1, die.num_sides+1):
            print ("Please enter a valid number between 1 and " + str(die.num_sides))
        elif self.user_input == self.random_number:
            print("Congradulation! your guess is correct!!")
        elif (self.user_input - self.random_number) >= 3:
            print("Your guess is too high")
        elif (self.random_number - self.user_input) >= 3:
            print("Your guess is too low")
        else:
            print("Your guess is so near the random number")


#Dice rolling and getting user guess
die = Die()
random_number = die.roll()

while True:
    user_number = die.get_input()
    check_num = CheckNum (random_number, user_number)
    Check_number = check_num.check_number()
    if user_number == random_number:
        break