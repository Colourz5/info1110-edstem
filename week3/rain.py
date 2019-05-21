rain = input("Is it currently raining? ")

if rain == "Yes":
    print("You should take the bus.")

elif rain == "No":
    distance = float(input("How far in km do you need to travel? "))
    if distance > 10:
        print("You should take the bus.")
    elif distance >= 2 and distance <= 10:
        print("You should ride your bike.")
    else:
        print("You should walk.")
