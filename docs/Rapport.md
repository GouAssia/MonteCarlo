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
    - ### [Mise en oeuvre sur machine à mémoire partagée (Assignment102.java) ](#p4)
    - ### [Mise en oeuvre sur machine à mémoire partagée (Pi.java) ](#p5)
    - ### [Qualité et test de performance ](#p6)
    - ### [Mise en oeuvre en mémoire distribuée](#p7)
    - ### [Sixième séance de TP ](#p8)
- ### [III - Qualité de développement](#p3)

<br><br><br>

----------

## <a name="p1"></a> I - Introduction

Dans ce document, nous avons commencé par introduire 

## <a name="p2"></a> II - TP

## <a name="p3"></a> Méthode Monte Carlo

Durant cette première séance de TP, la méthode de Monte Carlo nous a été introduite. 
sur papier 
----------

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

Elle permet de réaliser l'affichage de données de la méthode Monte Carlo notamment dans un fichier csv.

### Diagramme de classe Assignment102.java


## <a name="p5"></a> Mise en oeuvre sur machine à mémoire partagée (Pi.java) 

Utiliser la javadoc Executor 
suivi le cours sur Executor "cours.md"

Au lieu de regarder ceux qui sont dans le quart de cercle on peut regarder ceux qui ne sont pas dedans. 

Analyse Pi.java : 
Diagramme des classes sur lucidchart

Il s'agit d'un paradigme Master/Worker
total = ncible
totalCount / nb Worker = ntotal

Class Pi : classe de test 
Class Master : on mesure le temps puis on crée une collection de tâches renvoyer des resultats de type Long 
on va associé les tâches aux exectors 
On met un nombre de tâches égal à celui de threads 
On créer une liste de résultats qui vont apparaitre dans le futur en lui donnant toutes les tâches
Pour chaque future on fait un get et on ajoute le résultat dans total
Puis on calcule PI

Conclusion : Paradigme Master Worker qui repose sur des futures 
un master qui créer des tâches, les lance et on récupère le résultat de ces tâches (avec futures)

Class Worker : 
CircleCount = le nombre de points dans la cible

Pourquoi Master/Worker plus intéressant et performant?
on fait le choix de répartir le travail et de moins chargé les coeurs
temps d'ordonnancement plus long que le temps de calcul 

## <a name="p6"></a> Qualité et test de performance 

Nous aimerions faire en sorte de pouvoir comparer les deux codes et sorties plus facilement alors nous allons modifier les codes assignment102.java  et Pi.java afin d’obtenir les mêmes sorties même affichage du temps d’exécution, du nombre d’itération, du nombre de processus, erreur.

````
public class Assignment102 {
	public static void main(String[] args) {
		int numIterations = 500000;
		PiMonteCarlo PiVal = new PiMonteCarlo(numIterations);
		long startTime = System.currentTimeMillis();
		double value = PiVal.getPi();
		long stopTime = System.currentTimeMillis();
		System.out.println("Pi:" + value);
		System.out.println("Time Duration: " + (stopTime - startTime) + "ms");
		System.out.println("Ntot : " + numIterations);
		System.out.println("Available processors: " + Runtime.getRuntime().availableProcessors());
		System.out.println("Nombre de points : " + PiVal.nAtomSuccess);
		System.out.println("Error: " + ((value - Math.PI) / Math.PI));
		System.out.println("Difference to exact value of pi: " + (value - Math.PI));
	}
}
````

````
long stopTime = System.currentTimeMillis();

	System.out.println("\nPi : " + pi );

	System.out.println("Time duration : " + (stopTime - startTime));

	System.out.println("Ntot: " + totalCount*numWorkers);

	System.out.println("Available processors: " + numWorkers);

	System.out.println("Nombre de points: " + total);

	System.out.println("Error: " + (Math.abs((pi - Math.PI)) / Math.PI) +"\n");

	System.out.println("Différence : " + (pi - Math.PI));
````

Puis faire un fichier avec les données pour les comparer (Assignment102 a été fait, le faire pour Pi)

Bonne Scalabilité forte et faible : 
faire des tests pour 1,2, 4 workers avec le même nombre d'itérations 
Regarder les informations et comment on passe de données à d'autres données

On peut ajouter des graphiques 

TP 4 : on veut envoyer des messages en utilisant la mémoire distribuée

On télécharge le zip contenant les classes MasterSocket et WorkerSocket 
Buffer : fichier (socket) en mémoire où l'on écrit et lit. 

Dans la classe Master, on s'occupe d'initialiser les sockets, d'envoyer des sockets et de recevoir des messages du serveur
Le worker quant à lui doit simplement attendre un message pour pouvoir faire quelque chose

Pour pouvoir lire et écrire on créer des InputStreamReader et InputStreamWriter

Faire un diagramme des classes et analyser le code 
in.readLine() : on attend un message
out.println() : envoie de message 

executer le code et voir si ça fonctionne 

## <a name="p7"></a> Mise en oeuvre en mémoire distribuée

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

Cette classe MasterSocket contient 7 champs statiques : le nombre maximum de worker *maxServer*

### 3.2 Application 


On doit passer 2 arguments à la méthode main 
On lance la méthode main de workerSocket 
On s'aperçoit que cela ne fonctionne pas alors on va dans run/edit configurations/programs arguments, on met le port 25545
Puis on re run et on reçoit bien le port 25545 
On lance le MasterSocket et on entre 1 pour le nombre de worker et on entre le port 25545

Si on veut lancer plusieurs workers, on va commencé par lancer un worker avec le port 25545 par exemple 
Puis une fois lancé, on edit la configuration et on met un autre port 25546 par exemple puis on relance un autre worker
Enfin, on run masterSocket on entre 2 worker et les ports 25545 et 25546. 
Ou l'on peut simplement dans edit configuration ajouté une nouvelle application "Worker2"

Maintenant, on va modifier WorkerSocket pour calculer Pi 
Pour ça on va remplir dans WorkerSocket la partie Todo : compute pour faire le calcul 


Remarque : On modifie la conception du code

Ce qu'il faut faire il faut que le masterSocket écrive dans un fichier les résultats que leur envoie chaque worker concernant le calcul de Pi avec un seul Thread par worker 
Reprendre les tableaux que nous avions fait en qualité dev et faire les tests 
mais cette fois-ci c'est en mémoire distribuée avec Socket et par envoie de message 

Tests :

Pour : 16000000
Worker :  1
Pi : 3.14177025

Pour : 16000000
Worker :  2
Pi : 

Pour : 160000000
Pi : 3.141615875

Si on rajoute un 0 en plus Pi devient négatif 
Si on retire ce 0, on obtient 

Pour : 160000000
Pi : 3.141538025

Si on met plusieurs worker par exemple 2, on s'aperçoit que Pi est multiplié par 2
Cela fonctionne bien pour 160000000 mais si on rajoute un 0, on obtient -2.22711204875. 
Le problème est le int alors on va le modifier en long partout
Maintenant on obtient la bonne valeur de PI 


Evolution du temps d'exécution : 

Premier lancement : 50713 ms 
Deuxième lancement : 45360 ms

## <a name="p8"></a> Sixième séance de TP 

Dans cette séance, nous avons mis au propre et présenter la conception, le paradigme choisi pour les codes MasterSocket et WorkerSocket. La partie qui an été modifié est présente dans la séance cinq. 

Faire en sorte de modifier le code pour ajouter l'adresse IP pour communiquer avec d'autres machines 
avec ping 

Commandes : 

yum install java-devel => installer java sur CentOs
Puis il faut récupérer le MakeFile mais tout le dossier distributedMC_step1_javaSocket
On ouvre un terminal dans ce dossier et on teste le code WorkerSocket sur une machine : java WorkerSocket.java 25545

Puis sur une autre machine on débloque le firewall : firewall-cmd --zone=public --add-port=25545/tcp
Sur la même machine, on teste la classe MasterSocket : java MasterSocket.java
On commence avec 1 worker 
Puis on entre l'adresse Ip de l'autre machine : 192.168.24.131


