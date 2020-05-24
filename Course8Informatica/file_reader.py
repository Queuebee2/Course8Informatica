import re

def read_disease_abbreviation_file():
    abbreviationList = []
    filename = "Course8Informatica/disease_abbreviations.txt"

    file = open(filename, "r")
    for line in file:
        if line[:8] != 'Acronyms' and len(line) > 1:
            line.strip()
            line = line.split('\t')
            abbreviationList.append(line[0])

    return abbreviationList


def read_genepanel_file(method):
    symbols = []
    genpanelsDict = {}
    heritanceDict = {}
    filename = "Course8Informatica/GenPanels_merged_DG-2.17.0.txt"

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