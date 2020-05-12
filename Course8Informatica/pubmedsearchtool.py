from Bio import Entrez, Medline
Entrez.email = 'A.N.Other@example.com'

def run_querry(querry, method):
    handle = Entrez.esearch(db='pubmed',
                            sort='relevance',
                            retmax='10000',
                            retmode='xml',
                            term=querry)
    record = Entrez.read(handle)
    idlist = record["IdList"]

    if method == "ids":
        return idlist

    if method == "amount":
        return len(idlist)

    if method == "abstract":
        dataList = []
        fetch_handle = Entrez.efetch(db="pubmed", id=idlist, rettype="medline", retmode="text")
        records = Medline.parse(fetch_handle)
        counter = 0
        for record in records:
            dataList.append({})
            try:
                dataList[counter]["TI"] = record["TI"]
                dataList[counter]["AU"] = record["AU"]
                dataList[counter]["AB"] = record["AB"]
            except KeyError:
                print("No Title, Authors or Abstract found!\n")
            counter += 1
        return dataList


def create_collapsible(results):
    collapsible = '<button type="button" class="collapsible">' \
                  '{}</button>' \
                  '<div class="content">' \
                  '<p>{}</p>' \
                  '<p>{}</p>' \
                  '<input type ="checkbox" id ="checkbox{}" class ="check">' \
                  '<b> Flag this data </b> </div>' \
                  '</div>'

    collapsibles = '<p><b>Results:</b></p>'
    for i in range(len(results)):
        collapsibles += collapsible.format(results[i]["TI"], results[i]["AU"], results[i]["AB"], i) + '</br>'

    return collapsibles


def create_table(results):
    table = "<table>" \
            "<tr bgcolor='#f44336'>" \
            "<th>Title</th>" \
            "<th>Author</th>" \
            "<th>Abstract</th>" \
            " </tr>"

    formatted_table = table
    for i in range(len(results)):
        formatted_table += "<tr bgcolor='#f1f1f1'>"
        formatted_table += "<td>" + str(results[i]["TI"]) + "</td>"
        formatted_table += "<td>" + str(results[i]["AU"]) + "</td>"
        formatted_table += "<td>" + str(results[i]["AB"]) + "</td>"
        formatted_table += "</tr>"
    formatted_table += "</table>"
    return formatted_table

