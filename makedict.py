import string
dictionary = []
alphabet = list(string.ascii_uppercase)
for letter in alphabet:
    file = open("gcide-0.52/CIDE." + letter).read().split("\n")
    for line in file:
        if line[:8] == "<p><ent>":
            if line[8:-10].lower() not in dictionary:
                dictionary.append(line[8:-10].lower())
out = open("dictionary", "w")
for word in dictionary:
    out.write(word)
    out.write("\n")
out.close()
print("Exported to dictionary")
quit()
