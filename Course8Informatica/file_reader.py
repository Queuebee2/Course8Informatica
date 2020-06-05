import re
import xml.etree.ElementTree as ET


def read_gene_file():
    symbols = {}

    gene_file = "C:\\Users\\bartj\\Downloads\\human_genes.txt"

    with open(gene_file, 'r', encoding="utf-8") as file:
        for line in file:
            line = line.split('\t')
            regexp = re.compile(r'[0-9]')
            if regexp.search(line[0][0]):
                symbol = line[5]
                symbols[symbol] = symbol
                for alias in line[6].split(', '):
                    symbols[alias] = symbol

    return symbols


def read_mesh_terms_file():
    # retrieved from ftp://nlmpubs.nlm.nih.gov/online/mesh/MESH_FILES/xmlmesh/
    mesh_dict = {}

    xml_file = "C:\\Users\\bartj\\Downloads\\desc2020.xml"
    root = ET.parse(xml_file).getroot()

    for concept in root.findall('DescriptorRecord/ConceptList/Concept'):
        conceptname = concept.find('ConceptName/String')
        concept_desc = concept.find('ScopeNote')
        concept_string = conceptname.text
        if concept_desc is not None:
            concept_string += ": " + concept_desc.text
        for mesh in concept.findall('TermList/Term/String'):
            mesh_dict[mesh.text.lower()] = concept_string.lower().strip()

    return mesh_dict


def read_genepanel_file(filename="Course8Informatica/GenPanels_merged_DG-2.17.0.txt"):
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

    return list(heritanceDict.keys()), symbols
