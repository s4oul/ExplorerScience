# Génération Procédurale

Nous allons voir dans cet article comment créer [biome](https://fr.wikipedia.org/wiki/Biome) à l'aide de la génération procédurale. <br>
La génération procédurale est présente dans un certains nombres de jeux tel que `Diablo`, `The Binding of Isaac`. <br>
Le principe étant de créer un monde différent entre chaque itération. <br>

Dans cet article nous allons exposer les méthodes utilisée pour la création de biomes. <br>
Pour cela nous allons partir du postulat que notre monde doit :
* Avoir des chemins reliant `x` points.
* Avoir des bordures pour limiter la zone explorable.
* Avoir des reliefs.

## Labyrinthe

Pour créer notre monde nous allons déjà produire un `labyrinthe parfait ` et soluble ! <br>
Un labyrinthe est dit `imparfaites` lorsqu'il contient des `boucles`, `îlots`, `cellues inaccessible`.
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

### Réalisation
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

## Cheminement entre les salles

TODO !


## Sources Références
[Modélisation Mathématique de labyrinthe](https://fr.wikipedia.org/wiki/Mod%C3%A9lisation_math%C3%A9matique_de_labyrinthe)
