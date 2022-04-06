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
    name = input("enter name ")

    # Prints out hello <user>
    # Challenge: Instead of using "format" function
    #            use a string formatting feature introduced
    #            in Python3
    print(f"Hello {name}!")


def calculate_sum():
    """
    Function captures two number from the user and
    returns the sum
    """
    # Capture user input
    # Challenge: Instead of using two variable `num1` and `num2`
    #            use a list instead

    operation = input('''
    Please type in the math operation you would like to complete:
    + for addition
    - for subtraction
    * for multiplication
    / for division
    ''')

    nums = []
    
    for i in range(2):
        print(i)
        nums.append(
            int(input(f"Enter {i+1} number: ")))
        #import pdb; pdb.set_trace()
        # print(nums)
        #print(nums[0],[1])
        print( nums)
        x = nums[0]
        if len(nums) > 1:
            y = nums[1]

    
    if operation == '+':
        print('{} + {} = '.format(x, y))
        print(x + y)

    elif operation == '-':
        print('{} - {} = '.format(x, y))
        print(x - y)

    elif operation == '*':
        print('{} * {} = '.format(x, y))
        print(x * y)

    elif operation == '/':
        print('{} / {} = '.format(x, y))
        print(x / y)

    else:
        print('You have not typed a valid operator, please run the program again.')


    # Calculate sum & print out
    # Challenge task: Modify the function to allow users to input
    # what arithmetic operation they'd like to perform.
    

# Reading Files and printing out contents
def print_out_authors():
    """
    Function opens the authors.txt file in the current directory
    and prints out it's contents
    """
    # Open file objec
    
    with open('/home/ona/Downloads/Python-Intro/questions/basic_io/authors.txt', 'r') as f:
        print(f.read())
    #authors_file = open(r'Downloads/Python-Intro/questions/basic_io/authors.txt', 'r')

    # Print out contents of the file
    #print(data)


def collect_names():
    """
    Function collects 3 names from the user and writes it to
    a file
    """
    # Open output file; use `out.txt`
    # outfile = open(...)
    
    data = []

    outfile = open('/home/ona/Downloads/Python-Intro/questions/basic_io/out.txt','w')
    for i in range(3):
        data.append(input(f"{i+1} enter name "))
    outfile.write('\n'.join(data))
    print(outfile)

if __name__ == '__main__':
    collect_names()