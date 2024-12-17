import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math

def plot_errors_vs_iterations(file_path1):
    # Lire le fichier CSV
    df = pd.read_csv(file_path1, sep=";")

    # Extraire les colonnes 'Error' et 'Nombre d\'itérations'
    error = df['Error'].to_list()
    nb_iter = df["Nombre d'itérations"].to_list()

    # Liste pour les erreurs log transformées
    error_log = []

    # Appliquer la transformation logarithmique sur les erreurs
    for i in error:
        try:
            # Remplacer la virgule par un point et calculer le logarithme
            log_error = math.log10(float(i.replace(',', '.')))
            error_log.append(log_error)
        except ValueError as e:
            print(f"Erreur avec la valeur {i}: {e}")  # Afficher l'erreur
            error_log.append(float('nan'))  # Ajouter NaN si l'erreur persiste

    # Vérification du contenu des listes
    print(error_log)  # Afficher les valeurs calculées

    # Tracer les données
    plt.plot(nb_iter, error_log, "ob")
    plt.xlabel("Nombre d'itérations")
    plt.ylabel("Log(Error)")
    plt.title("L\'erreur en fonction du nombre d\'itérations")

    # Ajuster l'espacement entre les graphiques
    plt.tight_layout()

    # Afficher le graphique
    plt.show()

# Exemple d'appel de la fonction avec le chemin du fichier
plot_errors_vs_iterations("Pi_stabFaible_PCperso.csv")
