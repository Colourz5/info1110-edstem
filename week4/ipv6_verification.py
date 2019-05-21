IP_ADDRESS = input("Please enter an IP address: ")
ip = IP_ADDRESS.split(":")
stringlength = True

for i in range(len(ip)):
    if len(ip[i]) > 4:
        stringlength = False

valid = (len(ip) == 8) and stringlength

if valid:
    try:
        for i in range(8):
            hex(int(ip[0], 16))
        print("It is a valid IPv6 address.")
    except SyntaxError:
        print("It is not a valid IPv6 address.")
else:
    print("It is not a valid IPv6 address.")
