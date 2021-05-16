# World Procedural

Nous allons voir dans cette article comment créer un monde alétoire pour les jeux vidéo.<br>
Cette technique est présente dans un certains nombre jeux tel que `Diablo`, `The Binding of Isaac`.<br>
Le principe étant de créer un monde différent entre chaque itération.<br>

Dans l'article nous allons essayer d'exposé les méthodes utilisé afin de créer des [biomes](https://fr.wikipedia.org/wiki/Biome). <br>
Pour nous allons partir du postulat que notre monde doit :
* Avoir des chemins reliant `x` points
* Avoir des bordures afin de limiter la zone explorable
* Avoir des reliefs

## Labyrinthe

Afin créer notre monde nous allons déjà produire un labyrinthe `imparfaits` et `v` soluble !<br>
Un labyrinthe est dits `imparfaites` lorsqu'il contient des `boucles`, `îlots`, `cellues inaccessible`.<br>
<img src="https://upload.wikimedia.org/wikipedia/commons/b/ba/Yl_maze.5.png" width=300/>

Un labyrinthe est dits `parfaits` lorsque chaque cellules est relié à toutes les autres et, ce, de manière unique.<br>
<img src="https://upload.wikimedia.org/wikipedia/commons/2/26/Yl_maze.3.png?uselang=fr" width=300.>
<br>

***Réalisation :***

Base : <br>
Dans notre exposé le labyrinthe est composé de `y` colonnes `x` lignes représentant `y * x` cellules. <br>
Le contour de notre labyrinthe représente notre `bordule non explorable` par le joueur. <br>
Chacune de notre `cellue` contient 4 `bords`. <br>
<img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Yl_maze.cell.png" width=150/> <br>

Algorithme : <br>
Pour notre exemple nous prendre un labyrinthe de `5 colonnes` et `5 lignes`. <br>
Nous avons donc un ensemble de `25` cellules. <br>
Nous allons attribuer un identifiant unique à chaque cellule. <br>
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
Le principe étant d'itérer sur toutes cellules du labyrinthe tant qu'elles ne sont pas toutes égales. <br>
A chaque itération il faut prendre une cellule de référence aléatoirement dans le labyrinthe. <br>
Puis de prendre une cellule adjacente et de la comparé avec notre cellule de référence. <br>
Si les deux cellules sont différentes alors la cellule adjacente et toutes les cellules ayant la même valeur que la cellule adjacente
prennent la même valeur que la cellule de référence. <br>
Exemple : <br>
<img src="https://upload.wikimedia.org/wikipedia/commons/6/69/Yl_maze_ani_algo1.gif?uselang=fr" width=200>
<br>
Cela nous permet de créer un labyrinthe parfait ! <br>
Toutes les cellules sont reliées à toutes les autres et, ce, de manière unique. <br>


## Sources Références
[Modélisation Mathématique de labyrinthe](https://fr.wikipedia.org/wiki/Mod%C3%A9lisation_math%C3%A9matique_de_labyrinthe)
