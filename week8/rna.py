import time


def spliceosome(rna):
    intron_open = "GUGU"
    intron_close = "AGAG"
    count = 0
    starttime = time.perf_counter()
    # while intron_open in rna and intron_close in rna:
    while count < 10:
        temp = rna
        start = rna.index(intron_open)
        end = rna.index(intron_close) + 4
        rna = rna[:start] + rna[end:]
        count += 1
        print("Iteration: {}".format(count))
        print(rna)
        if rna == temp:
            break
    timetaken = time.perf_counter() - starttime
    print("This took {} seconds".format(timetaken))
    return rna


rna = input("Input strand: ")
rna = spliceosome(rna)
print("\nOutput is {}".format(rna))

# Program runs too slow
# GUGUAGAGGUCACAGUGUAAAAGCUCUAGAGCAGACAGAUGUAGAGGUGUUGUGUAACCCGUAGAGCAAAGGCAACAGUGUGUAAAGAGGUGUAAAGAG
# GUCACACAGACAGAUGUAGAGGUGUUGUGUAACCCGUAGAGCAAAGGCAACAGUGUGUAAAGAGGUGUAAAGAG
