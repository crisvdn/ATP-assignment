import interpreter


if __name__ == '__main__':
    f = open("instructions.txt")

    while True:
        lines = f.readline()
        if not lines:
            break
        list_tokens = interpreter.tokenize(lines)
        print(list_tokens)
        print(interpreter.execute(list_tokens))

    f.close()
