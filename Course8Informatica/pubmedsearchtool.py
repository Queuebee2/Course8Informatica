import matplotlib.pyplot as plt
import numpy as np
from Bio import Entrez
Entrez.email = 'A.N.Other@example.com'


YEAR_CATEGORIES = {"71-75": ['71', '72', '73', '74', '75'],
                   "76-80": ['76', '77', '78', '79', '80'],
                   "81-85": ['81', '82', '83', '84', '85'],
                   "86-90": ['86', '87', '88', '89', '90'],
                   "91-95": ['91', '92', '93', '94', '95'],
                   "96-00": ['96', '97', '98', '99', '00'],
                   "01-05": ['01', '02', '03', '04,' '05'],
                   "06-10": ['06', '07', '08', '09', '10'],
                   "11-15": ['11', '12', '13', '14,' '15'],
                   "16-20": ['16', '17', '18', '19', '20']}

#
# def main():
#     search_terms = get_search_terms()
#     run_querries(search_terms)
#
#
# def get_search_terms():
#     search_terms = []
#     search_term = "notempty"
#
#     while search_term != "":
#         search_term = input("Please fill in your search term and press Enter. \nLeave this empty if you do not wish to fill in (anymore) search terms. :\n")
#         if search_term != "":
#             search_terms.append(search_term)
#
#     return search_terms
#
#
# def run_querries(search_terms):
#     amount_dicts = []
#
#     for search_term in search_terms:
#         ids = run_querry(search_term)
#         amount_dicts.append(parse_ids(ids))
#
#     create_plot(amount_dicts, search_terms)


def run_querry(search_term):
    print(search_term)
    handle = Entrez.esearch(db='pubmed',
                            sort='relevance',
                            retmax='10000',
                            retmode='xml',
                            term=search_term)
    results_handle = Entrez.read(handle)
    ids = ','.join(results_handle['IdList'])

    return ids


def parse_ids(ids):
    handle = Entrez.esummary(db="pubmed", id=ids,
                              retmode="xml")
    records = Entrez.parse(handle)

    titles = []

    for record in records:
        titles.append(record['Title'])

    return titles

def create_plot(amount_dicts, search_terms):
    for amount_dict in amount_dicts:
        print(amount_dict)
        x_list = []
        for i in range(len(amount_dict)):
            x_list.append(i)

        x = np.array(x_list)
        y = np.array(list(amount_dict.values()))
        my_xticks = list(amount_dict.keys())
        plt.xticks(x, my_xticks)
        plt.plot(x, y)

    plt.title("Amount of papers published per year")
    plt.xlabel("Year of publishing")
    plt.ylabel("Amount of papers published")
    plt.legend(search_terms)
    plt.show()


# main()

