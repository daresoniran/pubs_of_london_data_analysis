## Total Number of pubs per borough

import csv

# frequency of local authority == number of pubs

with open('../4_Extended_Tasks/london_pubs.csv', 'r') as pubs_csv:
    spreadsheet = pubs_csv.read()
    camden = spreadsheet.count("Camden")
    greenwhich = spreadsheet.count("Greenwhich")
    barnet = spreadsheet.count("Barnet")
    hackney = spreadsheet.count("Hackney")
    hammersmith = spreadsheet.count('Hammersmith')
    islington = spreadsheet.count('Islington')
    k_c = spreadsheet.count('Kensington and Chelsea')
    lamb = spreadsheet.count('Lambeth')
    lew = spreadsheet.count('Lewisham')
    sou = spreadsheet.count('Southwark')
    tow = spreadsheet.count('Tower Hamlets')
    wan = spreadsheet.count('Wandsworth')
    wes = spreadsheet.count('Westminster')
    bar = spreadsheet.count('Barking')
    bex = spreadsheet.count('Bexley')
    cro = spreadsheet.count('Croydon')
    eal = spreadsheet.count('Ealing')
    enf = spreadsheet.count('Enfield')
    har = spreadsheet.count('Haringey')
    harr = spreadsheet.count('Harrow')
    hav = spreadsheet.count('Havering')
    hil = spreadsheet.count('Hillingdon')
    hou = spreadsheet.count('Hounslow')
    kut = spreadsheet.count('Kingston upon Thames')
    mer = spreadsheet.count('Merton')
    new = spreadsheet.count('Newham')
    red = spreadsheet.count('Redbridge')
    ric = spreadsheet.count('Richmond upon Thames')
    sut = spreadsheet.count('Sutton')
    wal = spreadsheet.count('Waltham Forest')
    bre = spreadsheet.count('Brent')
    bro = spreadsheet.count('Bromley')
    city = spreadsheet.count('City of London')

fieldnames = ['Local Authority', 'Number of Pubs']
data = [{'Local Authority': 'Camden','Number of Pubs': camden},
        {'Local Authority': 'Hackney', 'Number of Pubs': hackney},
        {'Local Authority': 'Hammersmith', 'Number of Pubs': hammersmith},
        {'Local Authority': 'Islington', 'Number of Pubs': islington },
        {'Local Authority': 'Kensington and Chelsea', 'Number of Pubs': k_c},
        {'Local Authority': 'Lambeth', 'Number of Pubs': lamb},
        {'Local Authority': 'Lewisham', 'Number of Pubs': lew},
        {'Local Authority': 'Southwark', 'Number of Pubs':sou },
        {'Local Authority': 'Tower Hamlets', 'Number of Pubs': tow},
        {'Local Authority': 'Wandsworth', 'Number of Pubs': wan },
        {'Local Authority': 'Westminster', 'Number of Pubs': wes},
        {'Local Authority': 'Barking', 'Number of Pubs': bar},
        {'Local Authority': 'Barnet', 'Number of Pubs': barnet},
        {'Local Authority': 'Bexley', 'Number of Pubs': bex},
        {'Local Authority': 'Croydon', 'Number of Pubs': cro},
        {'Local Authority': 'Ealing', 'Number of Pubs': eal},
        {'Local Authority': 'Enfield', 'Number of Pubs': enf},
        {'Local Authority': 'Haringey', 'Number of Pubs': har},
        {'Local Authority': 'Harrow', 'Number of Pubs': harr},
        {'Local Authority': 'Havering', 'Number of Pubs': hav},
        {'Local Authority': 'Hillingdon', 'Number of Pubs': hil},
        {'Local Authority': 'Hounslow', 'Number of Pubs': hou},
        {'Local Authority': 'Kingston upon Thames', 'Number of Pubs': kut},
        {'Local Authority': 'Merton', 'Number of Pubs': mer},
        {'Local Authority': 'Newham', 'Number of Pubs': new},
        {'Local Authority': 'Redbridge', 'Number of Pubs': red},
        {'Local Authority': 'Richmond upon Thames', 'Number of Pubs': ric},
        {'Local Authority': 'Sutton', 'Number of Pubs': sut},
        {'Local Authority': 'Waltham Forest', 'Number of Pubs': wal},
        {'Local Authority': 'Greenwhich', 'Number of Pubs': greenwhich},
        {'Local Authority': 'Brent', 'Number of Pubs': bre},
        {'Local Authority': 'Bromley', 'Number of Pubs': bro},
        {'Local Authority': 'City of London', 'Number of Pubs': city},
        ]
with open('number_of_pubs_by_la.csv', 'w+') as numPub:
    pubs = csv.DictWriter(numPub, fieldnames=fieldnames)
    pubs.writeheader()
    pubs.writerows(data)
