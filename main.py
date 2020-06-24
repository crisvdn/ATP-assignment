import interpreter
import re
from program_state import *
from decorators import calculate_time


def split_and_return(string):
    return re.split('([^a-zA-Z0-9])', string)


@calculate_time
def run():
    f = open("instructions.w++")
    ps = ProgramState()

    for i, one_line in enumerate(f.readlines()):
        splitted_line = list(filter(str.strip, split_and_return(one_line)))
        list_tokens = interpreter.tokenize(splitted_line, i + 1, 1)
        interpreter.execute(ps, list_tokens)
        print(f"ps after line {i}: {ps}")
    f.close()


if __name__ == '__main__':
    run()