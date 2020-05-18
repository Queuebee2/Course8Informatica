import re
from Course8Informatica import file_reader as fr

excludeList = ['DNA', 'RNA', 'SNP', 'PCR', 'RARE', 'LOD', 'USA']
US_states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
abbreviationList = fr.read_disease_abbreviation_file()
heritanceList = fr.read_genepanel_file('heritance_list')

joinedExcludeList = excludeList + US_states + abbreviationList + heritanceList

def mark_genes(text):
    extra_index = 0
    for match in re.finditer(r'( |\()([A-Z]([A-Z]|[0-9]|-)+)( |\)|,)', text):
        s = match.start()
        e = match.end()
        match_text = text[s+extra_index:e+extra_index]
        if_state_text = re.sub(r'\(|\)|,', '', match_text).strip()

        if if_state_text not in joinedExcludeList and not allCharSame(if_state_text):
            text = text[:s+extra_index] + '<b>' + text[s+extra_index:e+extra_index] + '</b>' + text[e+extra_index:]
            extra_index += 7

    return text


def allCharSame(text):
    for i in range(len(text)):
        if text[0] != text[i]:
            return False

    return True

