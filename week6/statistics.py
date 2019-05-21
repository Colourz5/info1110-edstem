import sys
import math


# Returns the mean of the given data set.
def mean(numbers):
    total = 0
    for i in numbers:
        total += i
    result = total / len(numbers)
    return result


# Returns the variance of the given data set.
def variance(numbers, mean):
    total = 0
    for i in numbers:
        total += (i - mean)**2
    result = total / len(numbers)
    return result


# Returns the standard deviation of the given data set.
def sd(variance):
    result = math.sqrt(variance)
    return result


numbers = []
print("Enter data set:")
while True:
    try:
        num = input()
        num = num.split(" ")
        for i in num:
            numbers.append(float(i))
    except ValueError:
        print("Invalid input, must be an integer!")
    except EOFError:
        break

if len(numbers) == 0:
    print("\nNo data!")
    sys.exit()

average = mean(numbers)
var = variance(numbers, average)
stnd = sd(var)

print("\nMean = {:.04f}".format(average))
print("Variance = {:.04f}".format(var))
print("Standard deviation = {:.04f}".format(stnd))
