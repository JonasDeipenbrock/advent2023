import os
from typing import Dict

def get_input():
    with open(__file__.rstrip("main.py") + "input.txt", "r") as f:
        return f.readlines()


def solve_a(input: list[str]):
    sum = 0
    for line in input:
        first_number = None
        last_number = None
        for char in line:
            if(char.isdigit()):
                if(first_number is None):
                    first_number = char
                last_number = char
        combined_number = int(first_number + last_number)
        # print(combined_number)
        sum += combined_number
    print(sum)


def get_word_indizes(line: str, indizes: Dict[int, str]) -> Dict[int, str]:
    number_pairs = [["one", "1"], ["two", "2"], ["three", "3"], ["four", "4"], ["five", "5"], ["six", "6"], ["seven", "7"], ["eight", "8"], ["nine", "9"]]
    for pair in number_pairs:
        leftest_index = line.find(pair[0])
        rightest_index = line.rfind(pair[0])
        if(leftest_index == -1):
            # skip this cause both will have no match
            continue
        if(leftest_index == rightest_index):
            indizes[leftest_index] = pair[1]
        else:
            indizes[leftest_index] = pair[1]
            indizes[rightest_index] = pair[1]
    return indizes

def get_number_indizes(line: str, indizes: Dict[int, str]) -> Dict[int, str]:
    for index, char in enumerate(line):
        if(char.isdigit()):
            indizes[index] = char
    return indizes

def solve_b(input: list[str]):
    sum = 0
    for line in input:
        indizes: Dict[int, str] = dict()
        indizes = get_word_indizes(line, indizes)
        indizes = get_number_indizes(line, indizes)
        
        first_number = min(indizes.items(), key=lambda x: x[0])[1]
        last_number = max(indizes.items(), key=lambda x: x[0])[1]
        combined_number = int(first_number + last_number)
        sum += combined_number
    print(sum)


if __name__ == "__main__":
    input = get_input()
    solve_a(input)
    solve_b(input)