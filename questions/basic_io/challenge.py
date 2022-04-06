
"""
With the knowledge learnt in the main.py file create a function
that asks the user for a file path & word then proceeds to check
whether the inputted word is present within the file. Function
should return true if word is present and false if it isn't
"""
"""
Challenge:
- Modify function to print out the line and line number
- Modify function to print out all the lines that contains the line
- Modify the function to perform a case insensitive search on the file and print out all lines that contain the word in any form
"""
def word_exists_in_file():
    count = 0
   
    file_path = input("Enter file name:")
    with open(file_path, 'r') as f:
        data =f.readlines()
        print(data)

    word = input("Enter word to search for ")
    for i, d in enumerate(data,start= 1):
        if word.lower() in d.lower():
            return True
   
        return False
    
    # Strips the newline character
    # for d in data:
    #     count += 1
    #     print("Line{}: {}".format(count, d.strip()))

    
    #     word = input("Enter word to search for ")
        
    #     if word.lower() in d.lower():
    #         print(word,"was found in the book.")
    #     else:
    #         print(word,"was not found in the book.")



    # Read file contents and check whether word is present within
    # one of the lines
    #return False


if __name__ == '__main__':
   word_exists_in_file()