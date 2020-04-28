import interpreter


if __name__ == '__main__':
    f = open("instructions.txt")
    lines = f.readline()
    print("lines: ", lines)
    list_tokens = interpreter.tokenize(lines)
    print(list_tokens )
    # interpreter.execute(lines)

    f.close()
