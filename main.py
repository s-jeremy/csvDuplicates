# Import
import csv
import pandas as pd
import numpy as np
import fileinput

# Duplicates functionality
def duplicates():

    # Excel File
    #data = pd.ExcelFile('data.xlsx')  # On lit le fichier Excel dans un DataFrame data
    #print(data.sheet_names)  # On affiche le nom des feuilles du classeur Excel
    #data.parse('sheet name') # On accède à la feuille souhaitée

    # CSV File
    data = pd.read_csv("data/data_duplicates.csv", usecols=['Nom','Prénom'], sep=';', header=0)  # data.csv correspond au chemin menant à votre dataset.
    #data.head()  # On affiche les 5 premières lignes
    #data.duplicated()   #La méthode duplicated() permet de savoir s'il y a des doublons dans la dataframe, on peut spécifier une colonne entre guillemets ou une partie des colonnes entre crochets
    #data.duplicated().sum()    #La méthode sum() appliquée à la méthode duplicated permet de connaître le nombre de doublons
    #data.drop_duplicates()     #La méthode drop_duplicates() permet de supprimer les doublons au sein de la dataframe, on peut spécifier une colonne entre guillemets ou une partie des colonnes entre crochets
    print('Le nombre de doublons dans le fichier est de ', data.duplicated().sum())
    #print(data.duplicated())
    #print(data.loc[data.duplicated(),:])               # Doublons affichés sans True/False
    print(data.loc[data.duplicated(keep='last'),:])     # Premiers doublons sélectionnés
    print(data.loc[data.duplicated(keep='first'),:])    # Derniers doublons sélectionnés

# Main
if __name__ == '__main__':
    duplicates()

