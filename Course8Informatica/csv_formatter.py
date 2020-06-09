import re
from flask import Markup

def format_csv_data(PMID, genes, title, mesh, delim=';'):
    """formats data into csv format

    Args:
        - PMID (str) : pubmed id
        - genes (dict) : mapping of genes to a number 
        - title(markupsafe.Markup)
        - delim(str) : delimiter
    Returns:
        - data (str) : csv-ready formatted data string.

    Todo:
        1. verify genes param description
    """
    title = re.sub(r'<span.*<b>|</b></span>', '', title)
    mesh = str(mesh).split("</b></span>")
    csv_mesh = []
    for m in mesh:
        m = str(m)
        if m and m.strip():
            m = m.split('title=')[1]
            m = m.split('><b>')[1]
            csv_mesh.append(m)

    print(csv_mesh)
    csv_mesh = ", ".join(csv_mesh)
    genes = list(genes.keys())
    genedata = ""
    for i in range(len(genes)):
        if i < (len(genes) - 1):
            genedata += genes[i] + ","
        else:
            genedata += genes[i]

    data = f'{PMID}{delim}{genedata}{delim}{csv_mesh}{delim}{title}'

    return data
