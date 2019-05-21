print("Input 3 strings and find what string is the longest")
word1 = input()
word2 = input()
word3 = input()
empty = len(word1) + len(word2) + len(word3)

if empty > 0:
    if len(word1) > len(word2) and len(word1) > len(word3):
        print("\"{}\" is the longest string".format(word1))
    elif len(word2) > len(word2) and len(word2) > len(word3):
        print("\"{}\" is the longest string".format(word2))
    elif len(word3) > len(word2) and len(word3) > len(word1):
        print("\"{}\" is the longest string".format(word3))
    else:
        print("All strings are the same length")
else:
    print("All strings are empty")
