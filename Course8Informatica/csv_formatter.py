import re


def format_csv_data(PMID, genes, title):
    title = re.sub(r'<span.*<b>|</b></span>', '', title)
    genes = list(genes.keys())
    genedata = ""
    for i in range(len(genes)):
        print(genes)
        if i < (len(genes) - 1):
            genedata += genes[i] + ","
        else:
            genedata += genes[i]

    data = PMID + ';' + genedata + ';' + title

    return data
