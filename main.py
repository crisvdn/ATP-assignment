import interpreter
from program_state import *

if __name__ == '__main__':
    f = open("instructions.txt")
    ps = ProgramState()

    while True:
        lines = f.readline()
        if not lines:
            break
        list_tokens = interpreter.tokenize(lines)
        print(list_tokens)
        print(interpreter.execute(ps, list_tokens))

    f.close()
