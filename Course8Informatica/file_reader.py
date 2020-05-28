import re

def read_disease_abbreviation_file():
    abbreviationList = []
    filename = "Course8Informatica/disease_abbreviations.txt"


    with open(filename, 'r', encoding="utf-8") as file:
        for line in file:
            if line[:8] != 'Acronyms' and len(line) > 1:
                line = line.strip()
                symbols = line.split('\t')
                symbol = symbols[0]
                if len(symbol) > 1:
                    if "/" in symbol:
                        more_symbols = symbol.split("/")
                        for s in more_symbols:
                            abbreviationList.append(s)
                    else:
                        abbreviationList.append(symbol)

    #  todo: run this only once, and just load a pre-formatted list of abbreviations
    # with open("abbrevations_only.txt", 'w') as out:
    #     for abbrev in abbreviationList:
    #         out.write(abbrev+"\n")
    #     print('done')


    return abbreviationList


def read_genepanel_file(method, filename="Course8Informatica/GenPanels_merged_DG-2.17.0.txt"):
    symbols = []
    genpanelsDict = {}
    heritanceDict = {}

    file = open(filename, "r")
    for line in file:
        if line[:6] != 'Symbol':
            line.strip()
            line = line.split('\t')
            symbol = line[0]
            symbols.append(symbol)
            genpanelsDict[symbol] = re.split(';', line[1])
            for sym in genpanelsDict[symbol]:
                try:
                    heritances = sym.split('(')[1].split(')')[0]
                    heritances = re.split(r',|\/', heritances)
                    for heritance in heritances:
                        try:
                            heritanceDict[heritance] += 1
                        except KeyError:
                            heritanceDict[heritance] = 1
                except IndexError:
                    print(sym)

    if method == "heritance_list":
        return list(heritanceDict.keys())

    if method == "symbols":
        return symbols

read_disease_abbreviation_file()