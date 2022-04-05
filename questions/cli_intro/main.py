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
from typing import List


def main():
    """encryption of program run as module"""
    args: Dict[str,str] = read_args()
    results: List[str] = search_file(args["file_path"], args["keyword"])
    show_results(results)

def read_args():
    """check for valid CLI arguments amd return them in a dictionary"""
    if len(sys.argv) != 3:
        print("usage: python -m cli_imtro.main [file] [keyword]")
        exit()

    return{
        "file_path": sys.argv[1],
        "keyword": sys.argv[2]
    }
def search_file(file_path: str, keyword: str):
    """opens file_path, reads each line,returns a List of line w/keyword"""
    matches: List[str]= []
    file_handle = open(file_path,"r",encoding="utf8")
    for line in file_handle:
        if keyword in line:
            matches.append(line)
    file_handle.close()
    return matches

def show_results(matches: List [str]):
    for line in matches:
        print(line.strip())

    print("Total matches:" + str(len(matches)))



if __name__ == "__main__":
    main()
