import sys

num = len(sys.argv) - 1
sum = 0
for i in range(1, num + 1):
    num1 = float(sys.argv[i])
    sum = sum + num1

if num == 0:
    print("You didn't input any arguments")
else:
    avg = sum / num
    list1 = str(sys.argv[1:num + 1])
    list1 = list1.replace("[", "{ ")
    list1 = list1.replace("]", " }")
    list1 = list1.replace("'", "")
    print(("Average of {} is {:.2f}").format(list1, avg))
