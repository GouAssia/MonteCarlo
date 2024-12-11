import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("pi_res_G26.csv", sep=";")
df_duree = df["Duree"].tolist()
durees = [int(duree.replace('ms', '')) for duree in df_duree]

meanDuration = []

for i in range(0, len(durees), 5):
    group = durees[i:i+5]
    avg = int(sum(group) / len(group))
    meanDuration.append(avg)

print(meanDuration)

nbProcessor = list(set(df["nbProcessor"].tolist()))

duree_1_processeur = meanDuration[0]  # Temps avec 1 processeur
speedup = [duree_1_processeur / duree for duree in meanDuration]

pente, ordonnee_origine = np.polyfit(nbProcessor, speedup, 1)
droite = [pente * x + ordonnee_origine for x in nbProcessor]

# Tracer la droite de régression
plt.figure(figsize=(10, 6))
plt.plot(nbProcessor, droite, label="Droite de régression", color='r')

# Ajouter la courbe y = x
plt.plot(nbProcessor, nbProcessor, label="Droite linéaire", color='b', linestyle='--')

plt.title("Scalabilité forte", fontsize=14)
plt.xlabel("Nombre de processeurs", fontsize=12)
plt.ylabel("Speedup", fontsize=12)

plt.legend()
plt.grid(True)
plt.show()
