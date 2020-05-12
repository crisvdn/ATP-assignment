import interpreter
import re
from program_state import *


def split_and_return(string):
    return re.split('([^a-zA-Z0-9])', string)


if __name__ == '__main__':
    f = open("instructions.w++")
    ps = ProgramState()

    for i, one_line in enumerate(f.readlines()):
        print(one_line)
        splitted_line = list(filter(str.strip, split_and_return(one_line)))
        list_tokens = interpreter.tokenize(splitted_line, i+1, 1)
        interpreter.execute(ps, list_tokens)
    print(ps)
    f.close()
