import re
import pprint


dataText = open('21.txt').read()
data = dataText.splitlines()
translations = {}
for line in data:
    contains =  re.search('(.*) \(contains (.*)\)', line)
    english = contains.group(2).split(", ")
    spanish = contains.group(1).split(" ")
    for engWord in english:
        # If word is not recorded yet, record all possibilities
        if engWord not in translations.keys():
            translations[engWord] = spanish
        else:
            translations[engWord].extend(spanish)


pprint.pprint(translations)


for word, possibilities in list(translations.items()):
    for poss in possibilities:
        if possibilities.count(poss) == 1:



# mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
# trh fvjkl sbzzf mxmxvkd (contains dairy)
# sqjhc fvjkl (contains soy)
# sqjhc mxmxvkd sbzzf (contains fish)

# kfcds, nhms, sbzzf, or trh

