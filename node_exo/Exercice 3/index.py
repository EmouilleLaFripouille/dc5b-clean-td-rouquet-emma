import pandas as pd

fichier = pd.read_csv('/Users/emmarouquet/DC5B/dc5b-clean-td-rouquet-emma/node_exo/Exercice 3/electronic-card-transactions-december-2022-csv-tables.csv', usecols=[1, 2, 10])
fichier = fichier.dropna()
fichier = fichier[fichier['Series_title_2'].isin(['Credit', 'Debit', 'Services'])]
fichier = fichier.reset_index(drop=True)
fichier.to_csv('/Users/emmarouquet/DC5B/dc5b-clean-td-rouquet-emma/node_exo/Exercice 3/result.csv', index_label='ID', columns=['Period', 'Data_value', 'Series_title_2'])