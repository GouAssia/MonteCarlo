import pandas as pd
import matplotlib.pyplot as plt
#import numpy as np

def plot_scalability(csv_file, group_size=5):
    """
    Trace un graphique de scalabilité forte avec une ligne reliant les points de données et la courbe y = x.

    :param csv_file: Chemin du fichier CSV contenant les données.
    :param group_size: Nombre de données à regrouper pour calculer la moyenne (par défaut 5).
    """
    # Charger les données
    df = pd.read_csv(csv_file, sep=";")
    df_duree = df["Time"].tolist()
    durees = [int(duree.replace('ms', '')) for duree in df_duree]

    # Calculer les durées moyennes
    meanDuration = []
    for i in range(0, len(durees), group_size):
        group = durees[i:i + group_size]
        avg = int(sum(group) / len(group))
        meanDuration.append(avg)

    # Liste des processeurs
    nbProcessor = sorted(list(set(df["nombre de processeur"].tolist())))

    # Calculer le speedup
    duree_1_processeur = meanDuration[0]  # Temps avec 1 processeur
    speedup = [duree_1_processeur / duree for duree in meanDuration]

    print(speedup)
    print(nbProcessor)

    # Tracer le graphique
    plt.figure(figsize=(10, 6))

    # Ligne reliant les points de données
    plt.plot(nbProcessor, speedup, label="Droite de SpeedUp", color='r', marker='o')

    #Pour la scalabilité faible (y=1)
    plt.plot(nbProcessor, [1]*len(nbProcessor), label="SpeedUp idéal", color='g', linestyle='--')

    # Configuration du graphique
    plt.title("Pi : Scalabilité faible", fontsize=14)
    plt.xlabel("Nombre de processeurs", fontsize=12)
    plt.ylabel("Speedup", fontsize=12)
    plt.legend()
    plt.grid(True)

    # Afficher le graphique
    plt.show()

plot_scalability("Pi_stabFaible_PCperso.csv")