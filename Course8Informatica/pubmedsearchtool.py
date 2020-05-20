from flask import Markup
from Bio import Entrez, Medline
Entrez.email = 'A.N.Other@example.com'
Entrez.api_key = "4bcbe73b19b2c6ca3c473e48a056f5dab709"


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
                  '<input type ="checkbox" name="checkbox" id="{}" class ="check">' \
                  '<b> Mark this data </b> </div>' \
                  '</div>'

    collapsible_data = []
    for i in range(len(results)):
        try:
            x = results[i]["TI"]
        except KeyError:
            results[i]["TI"] = "No title available"
        try:
            x = results[i]["AU"]
        except KeyError:
            results[i]["AU"] = "No author(s) available"
        try:
            x = results[i]["AB"]
        except KeyError:
            results[i]["AB"] = "No abstract available"

        collapsible_data.append([])
        collapsible_data[i].append(results[i]["TI"])
        collapsible_data[i].append(results[i]["AU"])
        collapsible_data[i].append(results[i]["AB"])
        collapsible_data[i].append(i)

    return collapsible_data


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
        try:
            formatted_table += "<td>" + str(results[i]["TI"]) + "</td>"
            try:
                formatted_table += "<td>" + str(results[i]["AU"]) + "</td>"
            except KeyError:
                formatted_table += "<td>" + "NO AUTHORS AVAILABLE" + "</td>"
            try:
                formatted_table += "<td>" + str(results[i]["AB"]) + "</td>"
            except KeyError:
                formatted_table += "<td>" + "NO ABSTRACT AVAILABLE" + "</td>"
        except KeyError:
            formatted_table += "<td>" + "NO RESULTS" + "</td>"
            formatted_table += "</tr>"
    formatted_table += "</table>"
    return formatted_table

