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
    data = pd.read_csv("data/data_duplicates.csv")  # data.csv correspond au chemin menant à votre dataset.
    #data.head()  # On affiche les 5 premières lignes
    #data.duplicated()   #La méthode duplicated() permet de savoir s'il y a des doublons dans la dataframe, on peut spécifier une colonne entre guillemets ou une partie des colonnes entre crochets
    #data.duplicated().sum()    #La méthode sum() appliquée à la méthode duplicated permet de connaître le nombre de doublons
    #data.drop_duplicates()     #La méthode drop_duplicates() permet de supprimer les doublons au sein de la dataframe, on peut spécifier une colonne entre guillemets ou une partie des colonnes entre crochets
    print(data.duplicated().sum())

# Main
if __name__ == '__main__':
    duplicates()

