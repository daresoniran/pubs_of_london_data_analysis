## Create a list of dictionaries

import csv

london_borough_data = []

with open('../4_Extended_Tasks/london_pubs.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)

    for row in spreadsheet:
        london_borough_data.append(row)


    def get_local_authority_from_row(local_authority_row):
        return local_authority_row['local_authority']

print(london_borough_data)
