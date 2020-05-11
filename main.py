import interpreter
from program_state import *

if __name__ == '__main__':
    f = open("instructions.txt")
    ps = ProgramState()

    for one_line in f.readlines():
        list_tokens = interpreter.tokenize(one_line, 1, 1)
        interpreter.execute(ps, list_tokens)
    print(ps)
    f.close()
