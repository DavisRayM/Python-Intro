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
    for i in range(2):
        nums.append(
            int(input(f"Enter {i+1} number: ")))

    print('press 1 for Addition \n press 2 for Subtraction \n press 3 for Multiplication \n press 4 for Division')
    option = int(input("enter your option: "))
    if option == 1:
        for n in first:
            for i in second:
                result = n+i
    elif option == 2:
        for n in first:
            for i in second:
                result = n-i

    elif option == 3:
        for n in first:
            for i in second:
                result = n*i

    elif option == 4:
        for n in first:
            for i in second:
                result = n/i

    else:
        print('Invalid Value')


    # Calculate sum & print out
    # Challenge task: Modify the function to allow users to input
    # what arithmetic operation they'd like to perform.
    print(result)

# Reading Files and printing out contents
def print_out_authors():
    """
    Function opens the authors.txt file in the current directory
    and prints out it's contents
    """
    # Open file objec
    with open('/home/ona/Downloads/Python-Intro/questions/basic_io/authors.txt', 'r') as f:
        data = f.read()
    #authors_file = open(r'Downloads/Python-Intro/questions/basic_io/authors.txt', 'r')

    # Print out contents of the file
    print(data)


def collect_names():
    """
    Function collects 3 names from the user and writes it to
    a file
    """
    # Open output file; use `out.txt`
    # outfile = open(...)
    
    with open('/home/ona/Downloads/Python-Intro/questions/basic_io/out.txt', 'w') as f:
        

        name1 = input('enter first name ')
        
        name2 = input('enter second name ')
        
        name3 = input('enter third name ')
        
        data = [name1,name2,name3]
        for d in data:
        #finalString = "  ".join(data)
            f.write(d + '\n')
    # Collect 3 names from the user and write to file
    # for name in user_input:
    #     write_to_file(name)


if __name__ == '__main__':
    collect_names()