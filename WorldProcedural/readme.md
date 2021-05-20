# Génération Procédurale
Nous allons voir dans cet article comment créer un [biome](https://fr.wikipedia.org/wiki/Biome)
à l'aide de la [génération procédurale](https://fr.wikipedia.org/wiki/G%C3%A9n%C3%A9ration_proc%C3%A9durale). <br>
Le principe étant de créer un monde différent entre chaque itération. <br>

Dans cet article nous allons exposer les méthodes utilisée pour la création de biomes. <br>
Pour cela nous allons partir du postulat que notre monde doit :
* Avoir des chemins reliant `x` points.
* Avoir des bordures pour limiter la zone explorable.
* Avoir des reliefs.

## Labyrinthe

Nous allons voir comment produire `labyrinthe parfait` en s'inspirant de l'algorithme de [Kruskal](https://fr.wikipedia.org/wiki/Algorithme_de_Kruskal) ! <br>
Un labyrinthe est dit `imparfaites` lorsqu'il contient des `boucles`, `îlots`, `cellules inaccessibles`.
<br>
<img src="https://upload.wikimedia.org/wikipedia/commons/b/ba/Yl_maze.5.png" width=300/>

Un labyrinthe est dit `parfaits` lorsque chaque cellule est relié à toutes les autres.
<br>
<img src="https://upload.wikimedia.org/wikipedia/commons/2/26/Yl_maze.3.png?uselang=fr" width=300.>
<br>

### Théorie

***Base :***
<br>
Le labyrinthe est composé de `y` colonnes `x` lignes représentant `y * x` cellules. <br>
Le contour de notre labyrinthe représente notre `bordule non explorable` par le joueur. <br>
Chacune de nos `cellules` contiennent 4 `bords`.
<br>
<img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Yl_maze.cell.png" width=150/>
<br>

***Algorithme :***
<br>
Pour notre exemple nous allons prendre un labyrinthe de `5 colonnes` et `5 lignes`. <br>
Nous avons donc un ensemble de `25` cellules. <br>
Nous allons attribuer un identifiant unique à chaque cellule afin de créer une structure de données appelée `Union-Find`. <br>
```
___________
|A|B|C|D|E|
___________
|F|G|H|I|J|
___________
|K|L|M|N|O|
___________
|P|Q|R|S|T|
___________
|U|V|W|X|Y|
___________
```

Le principe est d'itérer sur toutes cellules du labyrinthe tant qu'elles n'ont pas toutes la même valeur. <br>
A chaque itération il faut sélectionner une cellule aléatoirement dans le labyrinthe que l'on nomme `CR`,
puis sélectionner l'une des quatre cellules adjacentes (droite, gauche, haut, bas) à `CR` que l'on nomme `CA`.<br>
Enfin il faut comparer `CA` avec `CR` :
* Si `CR == CA` alors il existe déjà un chemin les reliant, on ne fait rien.
* Si `CR != CA` alors `CA` et toutes les cellules équivalentes prennent la même valeur que `CR`, puis on détruit le mur entre `CR` et `CA`.
    
***Exemple :***
<br>
<img src="https://upload.wikimedia.org/wikipedia/commons/6/69/Yl_maze_ani_algo1.gif?uselang=fr" width=200>
<br>
Cela nous permet de créer un labyrinthe parfait ! <br>
Toutes les cellules sont reliées entre elles. <br>

### Tests

Un code source écrie en python est disponible, il permet de générer un labyrinthe parfait.
Commandes :
```
python3 main.py --type=labyrinthe --width=10 --height=10
```

## Un Monde De Salles
Nous allons voir comment créer un monde contenant un nombre fixe de salle accessible.
Cette technique est présente dans un certains nombres de jeux tel que `Diablo`, `Path of Exile`. <br>
Si vous souhaitez générer une carte aléatoire, il existe toutes sortes de façons de procéder. <br>
Vous pouvez écrire une logique simple pour créer des rectangles de taille aléatoire à des emplacements aléatoires,
mais cela peut vous laisser avec des cartes pleines de pièces qui se chevauchent, sont groupées, orphelines ou étrangement espacées. <br>
Cela rend également un peu plus difficile la connexion des chambres les unes aux autres et de s'assurer qu'il n'y a pas de chambres orphelines. <br>
<br>
Avec la [partition binaire de l'espace](https://fr.wikipedia.org/wiki/Partition_binaire_de_l%27espace)
plus connue sous le nom de `BSP (Binary space partitioning)`, vous pouvez garantir des pièces plus uniformément espacées,
tout en vous assurant de pouvoir connecter toutes les pièces. <br>


### Théorie
***Base*** : <br>
Le monde se compose de `x` colonnes et `y` lignes formant un ___monde___ `z` de ___cellules___ soit `x * y`. <br>
Chaque cellule est inaccessible par le joueur par défaut. <br>
Une ___salle___ prend `n` colonnes et `m` lignes. <br>
Une salle `s` à une taille minimum de `2` colonnes et `2` lignes,
plus ces ___bordures___ formant donc un carré de `(n + 2) * (m + 2)` cellules. <br>
Un ___chemin___ `c` est un ensemble de cellules permettant la liaison entre deux salles. <br>
Un ___bloc___ `b` contient une salle, des cellules, un chemin et des ___cellules___ inaccessible,
soit `b > s + (n + 2 + m + 2) * 2`. <br>

***Étapes*** :
1) Toutes les cellules seront regroupées par bloc inégalement.
2) Créer une salle par bloc.
3) Relié les salles.

### 1) Toutes les cellules seront regroupées par bloc inégalement
On sépare notre monde en `j` blocs. <br>
Nous pouvons faire `z / j` pour connaitre la taille de tous les blocs
mais nous obtiendrons des blocs équilibrés et on ne garantit pas que `(z / j) <= (z / b)`! <br>
Il faut donc que `j` prenne pour valeur maximum `z / b`. <br>
<br>

On va donc diviser notre monde en plusieurs bloc de manière inégale ! <br>
Exemple : <br>
<img src="https://i.stack.imgur.com/Kdgah.jpg" width=300/>
<img src="https://i.stack.imgur.com/mDGjA.jpg" width=300/>
<br>

La ___taille minimum___ des salles doit être ***respecté*** sinon nous allons créer des blocs bien trop étroit. <br>
Résultat possible :
<br>
<img src="https://eskerda.com/wp-content/uploads/2013/12/not_bad.png" width=300/>
<img src="https://eskerda.com/wp-content/uploads/2013/12/room2.png" width=300/>

### 2) Chaque bloc correspond à une zone pouvant accueillir une salle
À présent que nous avons `j` blocs nous allons créer nos salles à l'intérieur de chaque bloc. <br>
Il faut donc créer des salles dans chaque bloc sans dépasser le bloc ni prendre toute la place ! <br>
Chaque cellule qui constitue la salle est à présent une cellule accessible par notre joueur. <br>
Nos blocs de départs :
<br>
<img src="https://cdn.tutsplus.com/cdn-cgi/image/width=1200/gamedev/uploads/2013/10/Binary_Space_Partitioning_for_Maps_Gamedev_Screen-01.jpg" width=300/>
<br>
Nos blocs contenant les salles :
<br>
<img src="https://cdn.tutsplus.com/cdn-cgi/image/width=1200/gamedev/uploads/2013/10/Binary_Space_Partitioning_for_Maps_Gamedev_Screen-02.jpg" width=300/>
<br>
Nous avons vue précédemment que seul les cellules formant les salles sont accessible ! <br>
Nous pouvons donc à présent représenter notre monde comme ceci :
<br>
<img src="https://cdn.tutsplus.com/cdn-cgi/image/width=1200/gamedev/uploads/2013/10/Binary_Space_Partitioning_for_Maps_Gamedev_Screen-03.jpg" width=300/>
<br>

### 3) Relié les salles
Il nous reste plus qu'à rendre accessible toutes les salles ! <br>
<br>
Le raccordement des salles s'effectue par des lignes droites ou des coudes (en angle droit).<br>
Il est important de s'assurer que toutes les salles soient reliée, aucune ne doit être orpheline et il ne doit
pas exister de groupe isolé, toutes les salles doivent être accessibles si un parcours entièrement le monde.<br>
<br>
Pour cela nous allons utiliser la structure de donnée `Union-Find`,
nous effectuerons la même méthode que la création d'un labyrinthe parfait afin d'assurer que toutes les salles soient accessible.<br>
Soit :
* Nous allons donner un numéro unique à chaque salle.
* À chaque fois qu'un lien entre deux salles ou plusieurs se créer elles acquièrent le même numéro.

Une fois que toutes les salles ont le même numéro nous obtenons :
<br>
<img src="https://cdn.tutsplus.com/cdn-cgi/image/width=1200/gamedev/uploads/2013/10/Binary_Space_Partitioning_for_Maps_Gamedev_Screen-04.jpg" width=300/>
<br>


## Sources
* [Modélisation Mathématique de labyrinthe](https://fr.wikipedia.org/wiki/Mod%C3%A9lisation_math%C3%A9matique_de_labyrinthe)
* [Algorithme de Kruskal](https://fr.wikipedia.org/wiki/Algorithme_de_Kruskal)
* [biome](https://fr.wikipedia.org/wiki/Biome)
* [Génération Procédurale](https://fr.wikipedia.org/wiki/G%C3%A9n%C3%A9ration_proc%C3%A9durale)
* [Partition binaire de l'espace](https://fr.wikipedia.org/wiki/Partition_binaire_de_l%27espace)
* [Démo BPS Dungeon](https://eskerda.com/bsp-dungeon-generation/)
  

