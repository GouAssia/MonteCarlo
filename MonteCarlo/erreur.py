import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def plot_errors_vs_iterations(file_path1):
    
    # Charger les données des fichiers CSV
    df1 = pd.read_csv(file_path1, sep=';', header=0)  # Premier fichier CSV avec les bons noms de colonnes
    
    # Convertir les colonnes pertinentes en flottants
    df1['Error'] = pd.to_numeric(df1['Error'], errors='coerce')
    df1['Nombre d\'itérations'] = pd.to_numeric(df1['Nombre d\'itérations'], errors='coerce')

    # Vérifier qu'il n'y a pas de NaN dans les colonnes essentielles
    df1 = df1.dropna(subset=['Error', 'Nombre d\'itérations'])
    
    # Appliquer la valeur absolue pour les colonnes nécessaires
    df1['Error'] = df1['Error'].abs()
    df1['Nombre d\'itérations'] = df1['Nombre d\'itérations'].abs()
    
    # Extraire les colonnes pertinentes pour l'erreur et le nombre de points
    errors1 = df1['Error']
    npoints1 = df1['Nombre d\'itérations']
    
    # Fonction pour calculer les médiants par Npoint
    def calculate_median_by_npoint(npoints, errors):
        df = pd.DataFrame({'Nombre d\'itérations': npoints, 'Error': errors})
        
        # Regrouper par Npoint et calculer le médiant pour chaque groupe
        median_df = df.groupby('Nombre d\'itérations').agg({'Error': 'median'}).reset_index()
        
        return median_df

    # Calcul des médiants pour chaque Npoint
    median1 = calculate_median_by_npoint(npoints1, errors1)
    
    # Créer une figure avec deux sous-graphiques
    fig, axs = plt.subplots(1, 2, figsize=(15, 6))  # 1 ligne et 2 colonnes de graphiques

    # Tracer un nuage de points pour le premier fichier (graphique à gauche)
    axs[0].scatter(npoints1, errors1, color='blue', label='Erreur vs Nombre d\'itérations(Fichier 1)', s=10)
    axs[0].scatter(median1['Nombre d\'itérations'], median1['Error'], color='black', s=50, zorder=5, label='Médiant par Nombre d\'itérations (Fichier 1)')
    axs[0].set_xlabel('Nombre d\'itérations (Nombre d\'itérations)', fontsize=12)
    axs[0].set_ylabel('Erreur (Error)', fontsize=12)
    axs[0].set_title('Nuage de points : Fichier 1', fontsize=14)
    
    # Appliquer l'échelle logarithmique
    axs[0].set_xscale('log')
    axs[0].set_yscale('log')
    axs[0].grid(True)
    axs[0].legend()

    # Afficher les graphiques
    plt.show()

# Appeler la fonction avec les chemins des fichiers
plot_errors_vs_iterations('Pi_stabFaible_G24.csv')
