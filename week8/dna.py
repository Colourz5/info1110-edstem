def complement(dna):
    intabupper = "ATCG"
    outtabupper = "TAGC"
    trans = str.maketrans(intabupper, outtabupper)
    complement = dna.translate(trans)
    intablower = "atcg"
    outtablower = "tagc"
    trans = str.maketrans(intablower, outtablower)
    complement = list(complement.translate(trans))
    for index, character in enumerate(complement):
        if character not in intabupper and character not in intablower:
            complement[index] = "x"
    complement = "".join(complement)
    return complement


dna = input("Enter strand: ")
if dna.strip() == "":
    print("\nNo strand provided.")
else:
    complement = complement(dna)
    print("\nComplementary strand is {}".format(complement))
