occurrence = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
digits = input()
i = 0
while i < len(digits):
    if int(digits[i]) == 0:
        occurrence[0] += 1
    elif int(digits[i]) == 1:
        occurrence[1] += 1
    elif int(digits[i]) == 2:
        occurrence[2] += 1
    elif int(digits[i]) == 3:
        occurrence[3] += 1
    elif int(digits[i]) == 4:
        occurrence[4] += 1
    elif int(digits[i]) == 5:
        occurrence[5] += 1
    elif int(digits[i]) == 6:
        occurrence[6] += 1
    elif int(digits[i]) == 7:
        occurrence[7] += 1
    elif int(digits[i]) == 8:
        occurrence[8] += 1
    elif int(digits[i]) == 9:
        occurrence[9] += 1
    i += 1
j = 0
while j < 10:
    print("{}: {}".format(j, occurrence[j]))
    j += 1
