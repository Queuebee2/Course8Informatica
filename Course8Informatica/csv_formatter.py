import re

def format_csv_data(PMID, genes, title,delim=';'):
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
    genes = list(genes.keys())
    genedata = ""
    for i in range(len(genes)):
        if i < (len(genes) - 1):
            genedata += genes[i] + ","
        else:
            genedata += genes[i]

    data = f'{PMID}{delim}{genedata}{delim}{title}'

    return data
