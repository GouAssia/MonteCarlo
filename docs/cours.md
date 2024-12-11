Executor 

-  On peut lui passer des Runnable (pour faire tourner) et des callable (qu'on peut appeler)
- Avec callable l'algorithme exécutera les tâches dans l'ordre en fonction des dépendances
- On l'appelle et elle envoie le résultat à un moment dans le code (on ne sait pas quand)

Future 
-  renvoie des résultats 
- méthodes : isDone et get


Introduction évaluation de performance

si on mesure des choses qui vont trop vite on peut pas le mesurer 
Speedup : plus T1 est petit par rapport à TP alors SP est plus grand 
    