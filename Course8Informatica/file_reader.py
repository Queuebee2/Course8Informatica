import re
import xml.etree.ElementTree as ET
import io


# Filename had to be changable, so put it into a global for now
# Todo rework into a class or change methods to take filenames
#  because we dont need more cyclical dependencies -_-
#  https://stackoverflow.com/questions/3400525/global-variable-from-a-different-file-python
GENEPANEL_FILENAME = "Course8Informatica/GenPanels_merged_DG-2.17.0.txt"

def update_filename(filename):
    global GENEPANEL_FILENAME
    print(f'updating global filename {GENEPANEL_FILENAME} to {filename}')
    GENEPANEL_FILENAME = filename

def test_is_filename_updated():
    return GENEPANEL_FILENAME

def read_disease_abbreviation_file():
    from Course8Informatica.constants import abbrevations
    # log : output saved as a list in a py file

def read_gene_file():
    symbols = {}

    gene_file = "human_genes.txt"

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

    # xml_file = "desc2020.xml"
    # root = ET.parse(xml_file).getroot()

    # for concept in root.findall('DescriptorRecord/ConceptList/Concept'):
    #     conceptname = concept.find('ConceptName/String')
    #     concept_desc = concept.find('ScopeNote')
    #     concept_string = conceptname.text
    #     if concept_desc is not None:
    #         concept_string += ": " + concept_desc.text
    #     for mesh in concept.findall('TermList/Term/String'):
    #         mesh_dict[mesh.text.lower()] = concept_string.lower().strip()
    #
    #
    # with io.open("mesh_terms.csv", "w", encoding="utf-8") as f:
    #     for key, val in mesh_dict.items():
    #         f.write(key + "\t" + val + "\n")

    with io.open("mesh_terms.csv", "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip("\n")
            line = line.split('\t')
            mesh_dict[line[0]] = line[1]

    return mesh_dict


def read_genepanel_file(filename="Course8Informatica/GenPanels_merged_DG-2.17.0.txt"):
    symbols = []
    genpanelsDict = {}
    heritanceDict = {}

    with open(GENEPANEL_FILENAME, "r") as file:
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
