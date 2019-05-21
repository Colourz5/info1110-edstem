line = input("Enter line: ")
anagram = input("Enter anagram: ")
punctuation = str.maketrans("!?.,'\\\"/[](){}+-*=-_<>|%#@^&~`", 30*" ")
line = line.translate(punctuation)
anagram = anagram.translate(punctuation)
line = (line.lower()).replace(" ", "")
anagram = (anagram.lower()).replace(" ", "")
if sorted(line) == sorted(anagram):
    print("\nAnagram!")
else:
    print("\nNot an anagram.")
