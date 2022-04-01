"""
Goal: Replicate the `word_in_file` function within the basic io section
using system arguments; Instead of prompting the user to input the file path
and word to search making the two arguments mandatory requirements for your
cli function.

Run the following function from the `cli_intro` to test out your cli tool:
    python <name_of_this_file> <path_to_file> <word_to_search>

Optional: Write tests for your cli tool
    - How to mock `sys.argv`: https://stackoverflow.com/questions/18668947/how-do-i-set-sys-argv-so-i-can-unit-test-it
    - In order to read out printed lines from your function and assert your output try checking out the test_basic_io.py file

Optional: Instead of using sys.argv; Try using the argparse library https://docs.python.org/3/library/argparse.html
"""
import sys


def main():
    print(sys.argv)


if __name__ == "__main__":
    main()
