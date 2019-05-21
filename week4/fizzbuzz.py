startnum = 1
endnum = 100
i = startnum
while i <= endnum:
    string = ""
    if i % 3 == 0:
        string += "Fizz"
    if i % 5 == 0:
        string += "Buzz"
    if string == "":
        string = i
    print(string)
    i += 1
