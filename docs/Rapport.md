Gouabi Assia <br>
INF3

<div align="center">
<img height="95" width="400" src="../img/iut_velizy.png" title="logo vélizy"/>

# Rapport programmation avancée

<br><br>
Ce document permet de mettre en avant ce qui a été vu lors des séances de TP de programmation avancée en développant les démarches à suivre

</div>

<br><br><br><br><br><br><br>

## Plan
- ### [I - Introduction](#p1)
- ### [II - TP](#p2)
    - ### [Méthode Monte Carlo](#p3)
	- ### [Algorithme et parallélisation](#p3A)
    - ### [Mise en oeuvre sur machine à mémoire partagée (Assignment102.java) ](#p4)
    - ### [Mise en oeuvre sur machine à mémoire partagée (Pi.java) ](#p5)
    - ### [Mise en oeuvre en mémoire distribuée](#p6)
    - ### [Communication avec d'autres machines ](#p7)
	- ### [Qualité et test de performance ](#p8)

<br><br><br>

----------

## <a name="p1"></a> I - Introduction

Dans ce document, nous avons commencé par introduire la méthode de Monte Carlo qui est une technique statistique utilisée pour résoudre des problèmes mathématiques complexes en faisant des simulations aléatoires. 

## <a name="p2"></a> II - TP

## <a name="p3"></a> Méthode Monte Carlo
----------

## <a name="p3A"></a> Alogorithme et parallélisation

## <a name="p4"></a> Mise en oeuvre sur machine à mémoire partagée (Assignment102.java)

### Introduction MonteCarlo en mémoire partagée 

Durant cette deuxième séance de TP, nous avons analyser le code d'une des deux classes Java du TP Monte carlo et réaliser le diagrammes UML lui appartenant.
Nous avons commencé par analyser la classe Assignment102.

### Explication : 

Assignment102 utilise des classes de l'API concurrent tels que AtomicInteger, ExecutorService ou Executors. Ces nouveaux éléments ont été recherché dans la documentation Java afin de comprendre leur utilité. 
AtomicInteger permet de manipuler des entiers dans un environnement multithreads. ExecutorService et Executors permettent de gérer l'exécution des tâches.

Dans ce code, on peut distinguer plusieurs classes qui sont liées et interagissent pour estimer la valeur de PI en utilisant la méthode Monte-Carlo. 
On a les classes principales : MonteCarlo, PiMonteCarlo et Assignment102. PiMonteCarlo contient la classe interne MonteCarlo.21 brd 192.168.31.255 scope global dynamic noprefixroute eno1


### PiMonteCarlo

La classe PiMonteCarlo contient un objet de type AtomicInteger *nAtomSuccess* en attribut. Il correspond dans le cas de la conception établie pour la méthode de Monte Carlo dans la première séance de TP à *nCible*. Le nombre de fois où les points sont dans la cible. 
Nous avons également l'entier *nThrows* qui correspond au nombre d'itérations (nombre de lancers) donc à *nTotal*. Enfin, le troisième attribut de la classe PiMonteCarlo est *value* de type double qui correspond à la valeur estimée de PI.

Dans la méthode getPi(), l'idée principale est de répartir le travail sur plusieurs threads pour accélérer l'exécution. On utilise ainsi le paradigme de l'itération parallèle, qui découpe un problème en sous-problèmes indépendants pouvant être résolus en parallèle. Chaque itération de la boucle dans getPi() est une tâche indépendante, qui génère un point aléatoire et vérifier s'il tombe à l'intérieur de la cible. 

Dans cette méthode, on commence par récupérer le nombre de processeurs disponibles sur la machine pour déterminer le nombre de Thread à utiliser avec Runtime. Runtime qui est l'environnement d'exécution à ne pas confondre avec CPUTime qui est le temps d'exécution. Cette étape est utile puisqu'elle va nous permettre de définir le même nombre de Threads et coeurs. 
Par la suite, on crée un ExecutorService avec en paramètre le nombre de Thread en utilisant Workstealing permettant à d'autres threads de voler des tâches si un thread est inactif. Le vol de tâches est le fait qu'un processeur puisse se rattacher à une autre tâche si elle est bloquée par la section critique.
La classe ExecutorService est gère l'exécution parallèle des tâches. Au lieu de créer un thread pour chaque tâche, Executor permet de découpler les tâches ce qui veut dire qu'on peut avoir un nombre peu important de Threads comparé aux tâches. Jusqu'ici on instancié un nouveau thread on lui passé la Runnable maintenant on utilise Executor et on définit le nombre de threads et tâches.

En clair, dans cette méthode getPI() on estime la valeur de Pi en utilisant la méthode de Monte Carlo, répartie sur plusieurs threads grâce à ExecutorService, 
Le résultat du calcul de PI est déterminé à partir du nombre de points arrivant dans la cible.

### MonteCarlo 

Dans cette classe, qui va être exécutée par chaque Thread, on définit un point de coordonnées x,y et on incrémente le nombre de succès si le point est dans la cible.    

### Assignment102

Elle permet de réaliser l'affichage de données telles que le nombre d'itérations, la valeur de Pi ou le temps d'exécution de la méthode Monte Carlo notamment dans un fichier csv.

### Diagramme de classe Assignment102.java


## <a name="p5"></a> Mise en oeuvre sur machine à mémoire partagée (Pi.java) 

Une fois que nous avons analysé le code Assignment102.java, nous allons procéder à l'analyse de Pi.java. Tout d'abord, en observant l'architecture et la structure du code on s'aperçoit qu'il s'agit d'un paradigme Master/Worker. 

<img height="200" width="250" src="../img/schema.jpg">

### Pi 

La classe Pi est une classe de test, elle va afficher les résultats de l'exécution 5 fois en ayant spécifier le nombre de workers et le nombre d'itérations que chaque worker devra effectuer. Ici, grâce aux explications sur la méthode Monte Carlo, on affirme que le nombre d'itérations que chaque worker devra effectuer est ntotal et que total est ncible. 

### Master 
 
La classe Master gère la distribution des tâches aux workers et l'agrégation des résultats. 

On commence par mesurer le temps actuel en millisecondes puis on crée une collection, une liste de tâches qui renvoyeront des résultats de type Callable<Long>. Chaque tâche correspond à un worker qui effectue un certain nombre d'itérations dans la simulation de Monte Carlo pour estimer π. Puis, un ExecutorService est crée et qui va être associé aux tâches. Ainsi, il va exécuter toutes les tâches en parallèle via la méthode invokeAll(). 
Une fois que toutes les tâches sont exécutées, les résultats vont apparaitre dans le future et seront récupérés et ajoutés dans total.

Suivant du calcul de Pi, des données telles que la valeur de Pi, le temps d'exécution ou le nombre de processeurs sont affichées dans un fichier csv comme dans la classe Assignment102.

### Callable 

L'interface Callable est similaire à Runnable. Cependant, elle peut retourner un résultat. Elle est utilisée pour des tâches qui peuvent s'exécuter en parallèle et qui ont une valeur de retour (ici <long>).

### Future 

Le but de Future est de fournir un moyen de gérer le résultat d'une tâche qui sera exécutée de manière asynchrone (dans un autre thread). Future permet de vérifier si la tâche est terminée, peut annuler une tâche si nécessaire et récupère le résultat de la tâche une fois terminée. 

### Worker  

La classe Worker peut être exécutée en parallèle dans un autre thread et retourne un résultat de type <Long>. 
La méthode Call() génère aléatoirement des points de coordonnées x et y. Puis elle vérifie si ses points se trouvent dans la cible. Si ils sont présents dedans, on incrémente le compteur circleCount qui représente le nombre de points dans la cible. 


### Pourquoi le paradigme Master/Worker est plus intéressant et performant? 

Il est plus intéressant et plus performant puisqu'on fait le choix de répartir le travail en plusieurs travailleurs et de moins chargé les coeurs. 

## <a name="p6"></a> Mise en oeuvre en mémoire distribuée

### 1. Contextualisation

Pour réaliser la méthode Monte Carlo en mémoire distribuée, nous avons récupéré les classes *MasterSocket.java* et *WorkerSocket*. 
En mémoire distribuée, on travaille par envoie de messages entre un serveur et un client à travers l'intermédiaire de Socket. 
Un Socket est un fichier contenant des informations telles que la source et le contenu de l'envoi ou encore le destinateur avec des flux qui permet l'échange de données entre deux applications. On manipule ses flux en faisant une lecture ou écriture dessus.

### 2. Paradigme Master/Worker

Le paradigme utilisé est Master/Worker. Le Master distribue le calcul entre plusieurs workers, qui calculent chacun une partie du travail. Ces workers envoient leur résultat au Master qui le récupère pour obtenir l'estimation finale de PI.
L'utilisation de ce paradigme et de plusieurs workers permettent d'exécuter des parties du code simultanément, d'améliorer l'efficacité du code et de réduire le temps global d'exécution. 

Dans le contexte de ses classes, la classe WorkerSocket écoute un port spécifique et attend une connexion du Master et la classe MasterSocket se connecte aux workers via leurs ports.

### 3. Explication des classes 

### 3.1 MasterSocket

Cette classe MasterSocket contient 7 champs statiques : le nombre maximum de worker *maxServer*, des ports que les workers utilisent pour communiquer avec le client *tab_port* mais également un tableau contenant les résultats envoyés par chaque worker *tab_total_workers*. 
Nous avons aussi l'adresse IP et des tableaux pour gérer les entrées et sorties et les connexions de socket.

Le programme va demander à l'utilisateur de rentrer le nombre de worker qu'il souhaite utiliser et enregistre la valeur. Par la suite, on effectue une connexion avec chaque worker en utilisant un socket qui se connecte à L'IP du client et le port spécifié parmis la liste *tab_port*. Les messages des worker sont lus avec *reader* et envoyés avec *writer*. 
Dans la boucle while, on répète le calcul de PI autant de fois que l'on veut et on additionne les résultats de chaque worker pour faire une estimation globale de la valeur de PI. 

BufferRead est utilisé pour lire des données, un texte provenant de l'entrée au clavier de l'utilisateur dans le programme. BufferWriter quant à lui est utilisé pour envoyé des données à un worker via un flux de sortie. 

### 3.2 WorkerSocket 

On commence par définir le port sur lequel le serveur va écouté les connexions entrantes. 

Un objet ServeurSocket est crée pour écouter sur le port spécifié. Le serveur attend qu'un client se connecte avec accept(). On peut lire les données envoyées par le client avec BufferedReader et envoyé des réponses avec PrintWriter. 
Enfin, tant que le message reçu n'est pas "END", le serveur effectue le calcul de PI à l'aide de la méthode doRun et envoie le résultat. 

### 3.3 Application 

Nous avons commencer par essayer d'exécuter le code WorkerSocket sauf que nous ne pouvions pas passer 2 arguments à la méthode main. Ce qui a été fait est que nous avons editer dans configurations/programs/arguments, nous avons mis le port à 25545 par exemple. 
Puis, on s'aperçoit quand relançant le code on reçoit bien le port indiqué. 

Pour établir, la connexion entre le Master et un Worker, on lance la classe MasterSocket en précisant 1 pour le nombre de worker suivi du port 25545 qui a été ouvert précédemment. 

Pour lancer plusieurs workers, dans la configuration, nous allons ajouter une nouvelle application et définir un nouveau port en plus de celui précédent. En exécutant MasterSocket, au lieu de préciser 1 seul worker dans la console, on en met 2. Enfin, on entre les deux ports l'un à la suite de l'autre. 


Remarque : On modifie la conception du code

Ce qu'il faut faire il faut que le masterSocket écrive dans un fichier les résultats que leur envoie chaque worker concernant le calcul de Pi avec un seul Thread par worker 
Reprendre les tableaux que nous avions fait en qualité dev et faire les tests 
mais cette fois-ci c'est en mémoire distribuée avec Socket et par envoie de message 


## <a name="p7"></a> Communication avec d'autres machines 

Durant une des séances de TP, nous avons fait en sorte d'établir une communication entre différentes machines de la salle à l'aide de leur adresse IP. 

Nous avons basculé sur CentOs et tenter d'installer Java sur celui-ci avec la commande suivante :

```
yum install java-devel
```
Une fois Java installé, nous avons récupérer le dossier *distributedMC_step1_javaSocket* fourni par notre professeur pour récupérer le MakeFile

Par la suite, nous avons effectuer des tests du code Java des deux classes avec : 

```
 java WorkerSocket.java 25545
```

et : 

```
 java MasterSocket.java 
```
Suivi du nombre de worker et l'adresse Ip de la machien ayant lancé le port 25545

Nous avons rencontrer quelques problèmes à exécuter ses codes car il fallait désactiver le parfeu sur les machines : 

```
firewall-cmd --zone=public --add-port=25545/tcp
```

## <a name="p8"></a> Qualité et test de performance 

Dans cette partie, nous allons effectuer des tests de performance afin de tester la capacité de notre système à fonctionner efficacement sous différentes conditions des classes énumérées précédemment : Assignment102.java, Pi.java, MasterSocket.java et WorkerSocket.java 

Les tests ci-dessous et les graphiques ont été réalisé sur mon architecture personnelle, il est important de spécifier les caractéristiques ci-dessous puisque d'une machine à une autre tout peu changer

Les caractéristiques : 

|Elements| Architecture | 
|--------|-----|
| Processeur   | Intel(R) Core(TM) i5-8265U CPU @ 1.60GHz   1.80 GHz  | 
| Mémoire RAM  | 8,00 Go  | 
| Nombre de coeurs | 4  | 
| Nombre de Threads | 8  | 

Le but était de réaliser des tests de performance en illustrant la scalabilité forte et faible à travers des graphique pour les classes évoquées précédemment. 

- Scalabilité forte : Vise à réduire le temps d'exécution d'une charge de travail donnée en augmentant les ressources.

- Scalabilité faible : Vise à maintenir les performances constantes malgré une augmentation de la charge de travail, en ajoutant des ressources.
 
 Pour cela, il fallait déterminer certains facteurs notamment le speedup. 

Le speedup est utilisé pour évaluer l'efficacité du parallélisme dans les calculs. Il mesure le gain de performance obtenu en augmentant le nombre de cœurs utilisés.
Il se calcule par la formule suivante : 

```
speedUp = Temps 1coeurs / Temps nCoeurs
```

### Assignment102 

* Scalabilité forte 

Tests effectués : 

| **numIterations** | **nbProcessor**                                | **Time Duration** |
|-------------------|------------------------------------------------|-------------------|
| 1 000 000         | 1 | 195.8 ms             |
| 1 000 000           | 2  | 247,4 ms             |
| 1 000 000        | 4      | 476,2 ms             |
| 1 000 000         | 8      | 553,2 ms             |
| 1 000 000         | 16    | 533,8 ms            |

<img height="300" width="600" src="../img/stabForteAssignment102.png" title="stab forte Assign"/>
<br><br>

* Scalabilité faible 

| **numIterations** | **nbProcessor**                                | **Time Duration** |
|-------------------|------------------------------------------------|-------------------|
| 1 000 000         | 1 | 177.8 ms             |
| 2 000 000           | 2  | 535.2 ms             |
| 4 000 000        | 4      | 1923 ms             |
| 8 000 000         | 8      | 4835.2 ms             |
| 16 000 000         | 16    | 9770.4 ms            |

<img height="300" width="600" src="../img/stabFaibleAssignment102.png" title="stab faible Assign"/>
<br>

### PI

* Scalabilité forte  

| **numIterations** | **nbProcessor**                                | **Time Duration** |
|-------------------|------------------------------------------------|-------------------|
| 1 000 000         | 1 | 516.4 ms             |
| 1 000 000           | 2  | 231.2 ms             |
| 1 000 000        | 4      | 200 ms             |
| 1 000 000         | 8      | 103.6 ms             |
| 1 000 000         | 16    | 131 ms            |

<img height="300" width="600" src="../img/stabFortePI.png" title="stab forte PI"/>
<br><br>

* Scalabilité faible  

| **numIterations** | **nbProcessor**                                | **Time Duration** |
|-------------------|------------------------------------------------|-------------------|
| 1 000 000         | 1 | 63.8 ms             |
| 1 000 000           | 2  | 72.6 ms             |
| 1 000 000        | 4      | 71 ms             |
| 1 000 000         | 8      | 103.2 ms             |
| 1 000 000         | 16    | 196.6 ms            |

<img height="300" width="600" src="../img/stabFaiblePI.png" title="stab Faible PI"/>
<br><br>
