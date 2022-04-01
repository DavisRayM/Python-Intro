"""
Basic IO section: Covers input and output functionality of python
"""

# Reading basic input from the user
def say_hello():
    """
    Function captures the users name from the terminal
    and says hello
    """
    # Capture users name from the terminal
    name = ""

    # Prints out hello <user>
    # Challenge: Instead of using "format" function
    #            use a string formatting feature introduced
    #            in Python3
    print("Hello {}!".format(name))


def calculate_sum():
    """
    Function captures two number from the user and
    returns the sum
    """
    # Capture user input
    # Challenge: Instead of using two variable `num1` and `num2`
    #            use a list instead
    num1 = num2 = 0

    # Calculate sum & print out
    # Challenge task: Modify the function to allow users to input
    # what arithmetic operation they'd like to perform.
    print(num1 + num2)


# Reading Files and printing out contents
def print_out_authors():
    """
    Function opens the authors.txt file in the current directory
    and prints out it's contents
    """
    # Open file object
    # authors_file = open(...)

    # Print out contents of the file
    pass


def collect_names():
    """
    Function collects 3 names from the user and writes it to
    a file
    """
    # Open output file; use `out.txt`
    # outfile = open(...)

    # Collect 3 names from the user and write to file
    # for name in user_input:
    #     write_to_file(name)
