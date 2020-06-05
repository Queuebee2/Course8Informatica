import re
from flask import Markup
from Course8Informatica import file_reader as fr

gene_dict = fr.read_gene_file()
mesh_dict = fr.read_mesh_terms_file()
heritance_list, symbols = fr.read_genepanel_file()

joinedExcludeList = heritance_list


def find_mesh_terms(text):
    data_first_search = ""
    for data in text:
        data_first_search += data[0] + " " + data[2] + " "
    search_dict = create_mesh_dict(data_first_search)
    for data in text:
        mesh1 = mark_mesh(data[0], search_dict)
        mesh2 = mark_mesh(data[2], search_dict)
        for mesh in mesh1:
            if mesh not in mesh2:
                mesh2.append(mesh)

        mesh2_string = ""
        for item in mesh2:
            mesh2_string += item
        data.append(mesh2_string)

    return text


def create_mesh_dict(text):
    print(text)
    search_dict = {}
    mesh_dict = {"reportedly": "test", "shows": "test", "both": "tessst"}
    for key in mesh_dict:
        regexp = re.compile(r'\b' + re.escape(str(key)) + r'\b', re.IGNORECASE)
        if regexp.search(text):
            print("1" + key)
            search_dict[key] = mesh_dict[key]

    return search_dict


def mark_mesh(text, search_dict):
    meshterms = []
    for key in search_dict:
        regexp = re.compile(r'\b' + re.escape(str(key)) + r'\b', re.IGNORECASE)
        if regexp.search(text):
            print(key)
            meshterms.append(Markup('<span class="btn-solid-lg page-scroll" title="{}"><b>{}</b></span>'.format(search_dict[key], key)))

    return meshterms


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

        if_state_text = re.sub(r'\(|\)|,|\.', '', match_text).strip()

        if if_state_text in symbols:
            text = text[:s+extra_index] + '<span title="Mentioned in current GenePanel"><b>'+ text[s+extra_index:e+extra_index] + '</b></span>' + text[e+extra_index:]
            extra_index += 59
        elif if_state_text in gene_dict:
            text = text[:s+extra_index] + '<span title="Not mentioned in current GenePanel ({})"><b>'.format(gene_dict[if_state_text]) + text[s+extra_index:e+extra_index] + '</b></span>' + text[e+extra_index:]
            extra_index += 65 + len(gene_dict[if_state_text])

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
