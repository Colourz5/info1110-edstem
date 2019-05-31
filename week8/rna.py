def spliceosome(rna):
    intron_open = "GUGU"
    intron_close = "AGAG"
    while True:
        start = rna.find(intron_open)
        if start == -1:
            break
        end = rna.find(intron_close, start + 4) + 4
        if end == -1:
            break
        rna = rna[:start] + rna[end:]
    return rna


rna = input("Input strand: ")
rna = spliceosome(rna)
print("\nOutput is {}".format(rna))
