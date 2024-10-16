import pandas
import glob

files = glob.glob('Autonomous*.xlsx')

books = []
for f in files:
    books.append(pandas.read_excel(f, skiprows=1, usecols='F'))

merged = pandas.concat(books)

merged['Rule'] = "-A INPUT -s " + merged['AS Range'] + " -j REJECT"

merged.to_csv('_rules.txt', header=False, index=False, columns=['Rule'])
