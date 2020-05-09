import interpreter


if __name__ == '__main__':
    f = open("instructions.txt")
    while True:
        lines = f.readline()
        if not lines:
            break
        print("lines: ", lines)
        list_tokens = interpreter.tokenize(lines)
        print(list_tokens)
        interpreter.execute_tokens(list_tokens)

    f.close()
