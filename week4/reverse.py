while True:
    try:
        word = input()
        line = ""
        for i in range(len(word)):
            line += word[-(i+1)]
        print(line)
    except EOFError:
        break
