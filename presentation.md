#Projet : [Frontrooms]
#Auteurs : [Alexandre Blacharz , Anas El Adarissi , Robin Sanders , Lénael Lapeine]


Naissance de l'idée :

L'idée de notre projet est née d'une discussion sur les mystères d'internet. On avait regardé une vidéo sur Cicada 3301, et on a trouvé super intéressant le concept d'énigmes cachées dans des fichiers ou des images. Comme on aime beaucoup l'univers des Backrooms, on s'est dit que c'était le mélange parfait. Les Backrooms offrent énormément de possibilités créatives car chaque niveau peut avoir son propre style et ses propres règles. On a donc voulu créer un jeu où le joueur doit vraiment chercher des indices partout, comme dans Cicada, mais dans l'ambiance étrange et stressante des niveaux des Backrooms. Notre but est de proposer des énigmes variées, allant de la simple logique à l'utilisation d'outils plus techniques comme le décodage de sons ou de coordonnées.



Présentation de l'équipe:
Eleves du lycée Clemenceau de la Terminale NSI.


Chef de projet .............. Anas
Responsable des bugs ........ Lenaël
Concepteur des énigmes ...... Alexandre
Expert en ambiances glauques . Robin

Responsable des images flippantes . Robin
Architecte backend .......... Lenaël
Expert en théories backrooms . Alexandre
Responsable de la bonne gestion du projet : Robin

Direction visuelle .......... Robin
Responsable "et si on faisait..." . Alexandre
Responsable des corrections de bugs . Lenaël
Vision artistique ........... Robin

Créateur de l'atmosphère .... Alexandre
Testeur principal ........... Anas
Responsable de la base de données . Anas
Directeur créatif ........... Robin

Concepteur des niveaux ...... Alexandre
Designer principal .......... Robin
Responsable des fausses bonnes idées . Alexandre
Ingénieur des idées ......... Anas

Temps passé sur le projet : 50h
Voilà le résumé complet, niveaux 0 à 5 :

---

**Niveau 0 — L'Entrée**
Le joueur découvre les Backrooms via un texte typewriter d'ambiance, puis visionne une vidéo d'introduction. Il est ensuite plongé dans une salle avec des hotspots cliquables : un mur griffé, une flèche, un trou dans le sol, une échelle. Chaque élément donne un indice sur un ordre logique. Le puzzle consiste à reconstituer la séquence correcte (mur → flèche → trou = code "391") et à l'entrer sur un panneau. Un mauvais ordre déclenche un jumpscare accompagné d'un message expliquant l'erreur.

---

**Niveau 1 — Le Parking**
Un parking souterrain abandonné avec des voitures et des tuyaux qui fuient. Trois zones à explorer mènent à trois sous-niveaux. En 1.2, des voitures sont disposées dans le parking : identifier la bonne voiture révèle une latitude (51°30'00.3"N). En 1.3, des tuyaux au plafond sont à faire pivoter comme un puzzle de circuits pour les relier tous — la solution révèle une longitude (0°07'36.5"W). Une fois les deux coordonnées trouvées, le sous-niveau 1.1 se déverrouille : Google Maps permet de localiser le point exact et d'en lire l'heure sur Street View (juillet 2024). Ce code horaire final ouvre la sortie.

---

**Niveau 2 — Zone Aquatique**
L'eau monte lentement dans des piscines et couloirs abandonnés. Le joueur explore trois salles interconnectées. En 2.2, il faut mémoriser et reproduire une séquence de néons — trois erreurs et l'eau monte plus vite. En 2.3, des tuyaux sous pression doivent être gérés sans dépasser 100%. Les indices des deux salles se combinent pour former un code d'évacuation à entrer sur le panneau central. Un mauvais code déclenche un jumpscare.

---

**Niveau 3 — La Fuite**
Un monstre a entendu le joueur. Trois épreuves enchaînées pour fuir, avec retour au début en cas d'échec : un memory (6 paires en 20 secondes), une séquence de flèches à reproduire (5 flèches, 3 manches, 2 vies), puis un jeu de tir (15 cibles en 25 secondes). Le code de sortie est construit à partir des chiffres clés de chaque mini-jeu.

---

**Niveau 4 — Found Footage VHS (1991)**
Le joueur visionne une vieille bande VHS d'une rue mystérieuse. Trois points d'intérêt à explorer : une cassette dont les scènes sont mélangées à remettre dans l'ordre, une maison dont il faut allumer les bonnes fenêtres par étage pour déduire le numéro de rue (n°19), et un lampadaire qui clignote en code Morse à décoder (message : "1974"). Les trois codes combinés déverrouillent la sortie.

---

**Niveau 5 — L'Extérieur Illusoire**
Le joueur croit être sorti, mais les maisons sont toutes identiques — une boucle sans fin. Dans la maison 5.1, un tableau accroché au mur cache une image à 4 éléments dont il faut trouver le point commun numérique. Dans la maison 5.2, un vieux magnétophone contient un fichier audio : en analysant son spectrogramme avec un outil de stéganographie, une image cachée révèle le mot-clé. Une fois les deux énigmes résolues, le château flottant au centre devient accessible.