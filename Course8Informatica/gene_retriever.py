import re
from flask import Markup
from Course8Informatica import file_reader as fr

excludeList = ['DNA', 'RNA', 'SNP', 'PCR', 'RARE', 'LOD', 'USA', 'HCC', 'CIN']
US_states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

# TODO
#  dit runt maar één keer, tijdens de import van dit bestand.
#  maak er een class van of zorg dat het ge rerunt kan worden pls
abbreviationList = fr.read_disease_abbreviation_file()
heritanceList = fr.read_genepanel_file('heritance_list')
symbols_in_current_genepanel = fr.read_genepanel_file('symbols')

joinedExcludeList = excludeList + US_states + abbreviationList + heritanceList


def find_genes(text):
    geneslist = []
    genesDict = {}
    if isinstance(text[0], list):
        for data in text:
            data[0] = Markup(mark_genes(data[0]))
            data[2] = Markup(mark_genes(data[2]))
        return text

    else:
        geneslist += return_genes(text[0])
        geneslist += return_genes(text[2])
        for gene in geneslist:
            try:
                genesDict[gene] += 1
            except KeyError:
                genesDict[gene] = 1
        return genesDict


def mark_genes(text):
    extra_index = 0
    for match in re.finditer(r'( |\()([A-Z]([A-Z]|[0-9]|-){2,})( |\)|,|\.)', text):
        s = match.start()
        e = match.end()
        match_text = text[s+extra_index:e+extra_index]

        if_state_text = re.sub(r'\(|\)|,', '', match_text).strip()


        if if_state_text not in joinedExcludeList and not allCharSame(if_state_text):
            if if_state_text in symbols_in_current_genepanel:
                text = text[:s+extra_index] + '<span title="Mentioned in current GenePanel"><b>' + text[s+extra_index:e+extra_index] + '</b></span>' + text[e+extra_index:]
                extra_index += 59
            else:
                text = text[:s+extra_index] + '<span title="Not mentioned in current GenePanel"><b>' + text[s+extra_index:e+extra_index] + '</b></span>' + text[e+extra_index:]
                extra_index += 63

    return text


def return_genes(text):
    genes = []
    extra_index = 0
    for match in re.finditer(r'( |\()([A-Z]([A-Z]|[0-9]|-)+)( |\)|,)',
                             text):
        s = match.start()
        e = match.end()
        match_text = text[s:e]

        gene = re.sub(r'\(|\)|,', '', match_text).strip()
        if gene not in joinedExcludeList:
            print(gene)
            genes.append(gene)

    return genes


def allCharSame(text):
    for i in range(len(text)):
        if text[0] != text[i]:
            return False

    return True

