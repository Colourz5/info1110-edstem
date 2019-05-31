def license_key_formatter(license, k):
    # k is segment length
    license = "".join(license.split("-"))
    output = ""
    count = 0
    index = len(license) - 1
    while index >= 0:
        output += license[index]
        count += 1
        if count == k:
            output += "-"
            count = 0
        index -= 1
    return output.strip("-").upper()[::-1]


if __name__ == "__main__":
    license = input("Enter license to be formatted: ")
    k = int(input("Enter segment length: "))
    print("\nOutput is {}".format(license_key_formatter(license, k)))
