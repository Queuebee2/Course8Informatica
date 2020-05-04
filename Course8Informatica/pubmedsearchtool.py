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


