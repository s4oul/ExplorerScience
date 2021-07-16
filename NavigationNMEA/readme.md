# Navigation GPS

Dans cette article nous allons voir comment la navigation et plus particulièrement comment les communications entre équipement s'éffectuent.


## NMEA
`NMEA` National Marine & Electronics Association, est une association à but non lucratif fondée par un groupement de professionnels de l’industrie de l’électronique des périphériques marine, conjointement avec des fabricants, des distributeurs, des revendeurs, des institutions d’enseignements. Leur but entre autre, harmoniser et standardiser les équipements de la marine.<br>

Le format le plus fréquent étant la norme NMEA 0183 mais il commence à être remplacé par la norme NMEA 2000. De plus, le format NMEA OneNet est le futur standard qui sera utilisé pour complémenter les systèmes existant et non pour les remplacer.


## NMEA 0183

La norme 0183 utilise une communication série (RS422) pour transmettre des messages appellé `trame` elle est constitué de caractères ASCII.
| Baud Rate | Data bits | Stop bits | Handshake |
| :-------: | :-------: | :-------: | :-------: |
| 8         | None      | 1         | None      |

Il existe une alernative à la communication série, certains équipement utilise le protocol UDP.

__La trame suite la structure suivante :__


__Règles :__
* Tous les caractère appartient à la table ASCII.
* La taille maximun d'un message est de 82 caractères
* Le message commence par le caractère `$` ou `!`
* Le message fini par le caractère \<LF>
* Les cinq premier caractère après `$` ou `!` indique l'émetteur et le type de trame
    * Les deux premiers caractères après le caractère `$`
    * Les trois suivant indique le type de trame
* Toutes les données sont séparé par le caratère `,`
* Quand une donnée est invalide le champ est vide.
* Les caractère présent apres `*` est un indiquant de somme de parité (checksum), cette donné est optionnelle pour certaines trame.

__Caractère reservé par la norme NMEA 0183 :__
|ASCII 	 | Hex 	| Dec  | Use                                                                        |
| :----: | :--: | :--: | :------------------------------------------------------------------------: |
| \<CR>  | 0x0d | 13   | Carriage return                                                            |
| \<LF>  | 0x0a | 10   | Line feed, end delimiter                                                   |
|!       | 0x21 | 33   | Start of encapsulation sentence delimiter                                  |
|$       | 0x24 | 36   | Start delimiter                                                            |
|*       | 0x2a | 42   | Checksum delimiter                                                         |
|,       | 0x2c | 44   | Field delimiter                                                            |
|\       | 0x5c | 92   | TAG block delimiter                                                        |
|^       | 0x5e | 94   | Code delimiter for HEX representation of ISO/IEC 8859-1 (ASCII) characters |
|~       | 0x7e | 126  | Reserved                                                                   |

__Les principaux identifiant d'éméteur sont :__
| Identifiant | Émétteur |
| :---------: | :------: |
| BD          | Beidou   |
| GB          | Beidou   |
| GA          | Galileo  |
| GP          | GPS      |
| GL          | GLONASS  |


__Exemples :__

___Trame GGA___
```
$GPGGA,064036.289,4836.5375,N,00740.9373,E,1,04,3.2,200.2,M,,,,0000*0E
```
```
$GPGGA       : Type de trame (GPS + GGA)
064036.289   : Trame envoyée à 06 h 40 min 36 s 289 (heure UTC)
4836.5375,N  : Latitude 48,608958° Nord = 48° 36' 32.25" Nord
00740.9373,E : Longitude 7,682288° Est = 7° 40' 56.238" Est
1            : Type de positionnement (le 1 est un positionnement GPS)
04           : Nombre de satellites utilisés pour calculer les coordonnées
3.2          : Précision horizontale ou HDOP (Horizontal dilution of precision)
200.2,M      : Altitude 200,2, en mètres
,,,,,0000    : D'autres informations peuvent être inscrites dans ces champs ou valeurs invalide
*0E          : Somme de contrôle de parité, un simple XOR sur les caractères entre $ et *
```

___Trame RMC___
```
$GPRMC,053740.000,A,2503.6319,N,12136.0099,E,2.69,79.65,100106,,,A*53
```
```

$GPRMC       : type de trame
053740.000   : heure UTC exprimée en hhmmss.sss : 5 h 37 min 40 s
A            : état A=données valides, V=données invalides
2503.6319    : Latitude exprimée en ddmm.mmmm : 25° 03.6319' = 25° 03' 37,914"
N            : indicateur de latitude N=nord, S=sud
12136.0099   : Longitude exprimée en dddmm.mmmm : 121° 36.0099' = 121° 36' 00,594"
E            : indicateur de longitude E=est, W=ouest
2.69         : vitesse sur le fond en nœuds (2,69 nd = 3,10 mph = 4,98 km/h)
79.65        : route sur le fond en degrés
100106       : date exprimée en qqmmaa : 10 janvier 2006
,            : déclinaison magnétique en degrés (souvent vide pour un GPS)
,            : sens de la déclinaison E=est, W=ouest (souvent vide pour un GPS)
A            : mode de positionnement A=autonome, D=DGPS, E=DR
*53          : somme de contrôle de parité au format hexadécimal
```

## Informations
* [série](https://fr.wikipedia.org/wiki/Transmission_s%C3%A9rie)
* [ASCII](https://fr.wikipedia.org/wiki/American_Standard_Code_for_Information_Interchange)
* [UDP](https://en.wikipedia.org/wiki/User_Datagram_Protocol)
* [OpenCpn](https://opencpn.org/)
