from flask import Markup
from Bio import Entrez, Medline
Entrez.email = 'A.N.Other@example.com'
Entrez.api_key = "4bcbe73b19b2c6ca3c473e48a056f5dab709"
""" Pubmed search tool

Todo:
 - don't use 'A.N.Other@example.com' as Entrez email, as this might cause
   issues where the server could get a timeout or ban for making
   requests through the Entrez API
"""


def run_query(search, method):
    """Runs a query (search) against the medline database
    through biopythons Entrez api (esearch)

    Args:
        - search (list) : list of search terms
        - method (string) : method

    Returns:
        if method == "ids":
            -  idlist (list) ) list of Id's
        if method == "amount":
            - len(idlist) (int) : amount of id's
        if method == "abstract":
            - dataList (list) : list with data

    """
    query = ""
    for term in search[:3]:
        if term:
            query += term + " "
    query.strip()

    date = '(("1900/12/12"[Date - Completion] : "3000"[Date - Completion]))'
    if search[3]:
        date = date.replace("1900/12/12", search[3])
    if search[4]:
        date = date.replace("3000", search[4])

    if search[3] or search[4]:
        query = query + " AND " + date
    handle = Entrez.esearch(db='pubmed',
                            sort='relevance',
                            retmax='10000',
                            retmode='xml',
                            term=query)
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
                dataList[counter]["PMID"] = record["PMID"]
            except KeyError:
                print("No Title, Authors or Abstract found!\n")
            counter += 1
        return dataList


def create_collapsible(results):
    """Creates a collapsible html element for a search result
    Args:
        - results (dict): mapping of result attributes

    Returns:
        - collapsible_data (list): list result attributes in
          order for collapsible element

    """
    collapsible_data = []
    for i in range(len(results)):
        try:
            x = results[i]["TI"]
        except KeyError:
            results[i]["TI"] = "No title available"
        try:
            x = results[i]["PMID"]
        except KeyError:
            results[i]["PMID"] = "No pubmed identifier available"
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
        collapsible_data[i].append(results[i]["PMID"])
        collapsible_data[i].append(i)

    return collapsible_data