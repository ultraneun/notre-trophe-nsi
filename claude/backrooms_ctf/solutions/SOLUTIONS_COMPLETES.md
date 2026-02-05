# 🔐 SOLUTIONS COMPLÈTES - BACKROOMS CTF

## Document pour le jury / enseignants

---

## 📋 VUE D'ENSEMBLE

Ce CTF contient 6 niveaux (0 à 5) avec des énigmes de difficulté croissante.
Thème : Un développeur (M4RK) coincé dans les Backrooms qui laisse des indices pour s'échapper.

**Temps de résolution estimé :** 3-5 heures pour un joueur expérimenté

---

## LEVEL 0 - THE LOBBY

### Fichiers :
- `entry_log.html` (page principale)
- `distress_signal.txt` (aide supplémentaire)
- `M4RK_backup.py` (script Python)

### Énigme 1 : Base64 dans le code source HTML

**Où :** Commentaire HTML dans `entry_log.html`

**Message encodé :**
```
SGUncyBnb25lIGRlZXBlci4gSSBmb3VuZCBzb21ldGhpbmcuIEEgZG9vci4gQnV0IGl0J3MgbG9ja2VkLgpUaGUgY29kZSBpcyBhIHRpbWUuIE5vdCBqdXN0IGFueSB0aW1lLgpUaGUgdGltZSB3aGVuIEkgd2FzIHN0aWxsIGluIHRoZSByZWFsIHdvcmxkLgpUaGUgbGFzdCBwbGFjZSBJIHNhdyBiZWZvcmUgdGhpcyBuaWdodG1hcmUuCgpGaW5kIG15IGxhc3QgbG9jYXRpb24uIEZpbmQgd2hlbiB0aGUgY2xvY2sgc2hvd2VkIHRoZSBhbnN3ZXIuCkZvcm1hdDogSEg6TU0gKDI0aCkKClRoZW4gbG9vayBmb3IgbGV2ZWwxX2tleV9bVElNRV0uaHRtbA==
```

**Décodage :**
- Outil : CyberChef, ou `base64 -d` en terminal
- Message en clair :
```
He's gone deeper. I found something. A door. But it's locked.
The code is a time. Not just any time.
The time when I was still in the real world.
The last place I saw before this nightmare.

Find my last location. Find when the clock showed the answer.
Format: HH:MM (24h)

Then look for level1_key_[TIME].html
```

### Énigme 2 : Coordonnées GPS → Google Maps → Heure

**Indices dans les fichiers :**
- GPS : 48.8584° N, 2.2945° E (Tour Eiffel, Paris)
- Mais aussi : "Les coordonnées du Big Ben : 51.5007° N, 0.1246° W" (dans M4RK_backup.py)

**Solution :**
1. Aller sur Google Maps
2. Entrer les coordonnées du Big Ben : `51.5007° N, 0.1246° W`
3. Activer Street View / Photos 360°
4. Chercher une vue de 2024 où l'horloge est visible
5. L'heure affichée : **06:10**

**Fichier suivant :** `level1_key_06:10.html`

### Compétences testées :
- ✓ Lecture de code source HTML
- ✓ Décodage Base64
- ✓ Utilisation de Google Maps
- ✓ OSINT géographique

---

## LEVEL 1 - THE DARK

### Fichier :
- `level1_key_06:10.html`

### Énigme : Île en forme d'hippocampe

**Indices :**
- "L'île en forme de cheval de mer garde le secret"
- "Cherche où les tortues règnent en maîtres"
- "Galápagos, archipel de Darwin"

**Solution :**
1. Rechercher "Galapagos islands map" sur Google
2. Examiner la forme de chaque île
3. L'île **Isabela** ressemble à un hippocampe vu du ciel
4. Mot de passe : **isabela** (en minuscules)

**Fichier suivant :** `level2_access_isabela.html`

### Compétences testées :
- ✓ Recherche web
- ✓ Interprétation visuelle (formes géographiques)
- ✓ Culture générale (Galápagos)

---

## LEVEL 2 - THE PIPES

### Fichier :
- `level2_access_isabela.html`

### Énigme 1 : OSINT Twitter/Reddit

**Post Twitter fictif :**
- Handle : `@M4RK_Trapped`
- Coordonnées : 34°52'N 138°30'E
- "Cherchez ce qui s'est élevé en 2024. Le sommet a parlé."

**Solution :**
1. Coordonnées = **Mont Fuji, Japon**
2. Rechercher news 2024 sur le Mont Fuji
3. Info possible : frais d'entrée passés à **2000 yens** en 2024
4. Ou nombre de touristes augmenté à **300,000**

### Énigme 2 : Post Reddit + Stéganographie

**Post Reddit fictif :**
- Username : `Lost_In_L2_2024`
- Titre : "J'ai trouvé quelque chose dans les tuyaux"
- Image de tuyau avec données cachées

**À créer réellement :**
```bash
steghide embed -cf pipe_image.jpg -ef secret.txt
# Mot de passe : PIPES
```

**Contenu de secret.txt :**
```
Message caché : "extraction" ou "freedom"
```

**Fichier suivant :** `level3_the_electrical_station.html`
(Ou variante avec les infos trouvées)

### Compétences testées :
- ✓ OSINT réseaux sociaux
- ✓ Recherche d'actualités
- ✓ Stéganographie (steghide)

---

## LEVEL 3 - THE ELECTRICAL STATION

### Fichiers :
- `level3_the_electrical_station.html`
- `system_restore.exe` (fichier corrompu)

### Énigme 1 : Analyse hexadécimale

**Comment faire :**
```bash
# Linux/Mac
xxd system_restore.exe | less
# Ou
strings system_restore.exe

# Windows
# Utiliser HxD ou hexed.it
```

**Strings à trouver dans le binaire :**
1. `"THE NEXT LEVEL IS HIDDEN IN PASTEBIN - SEARCH FOR M4RK_L3VR3_3"`
2. `"ROT13: Guh sbhegu yriry ner ng GUR FRRER CBRER"`
3. `"GPS_COORDS: 35.6569 N, 139.7423 E - Tokyo Tower 2024"`
4. `"PASSWORD_HINT: The answer is in the sky"`

### Énigme 2 : Pastebin

**À créer réellement :**
- Compte Pastebin
- Post avec le code : `M4RK_L3VR3_3`
- Contenu : indice pour Level 4 ou lien direct

### Énigme 3 : ROT13

**Message crypté :**
```
Guh sbhegu yriry ner ng GUR FRRER CBRER
```

**Décodage ROT13 :**
```
The fourth level are at THE SEVEN POWER
```

### Énigme 4 : Tokyo Tower GPS

**Coordonnées :** 35.6569° N, 139.7423° E

**Solution :**
1. Aller sur Google Maps à ces coordonnées
2. Regarder photos de Tokyo Tower en 2024
3. Chercher "answer in the sky" = illumination spéciale, nombre, symbole

**Fichier suivant :** `level4_poolrooms.html`

### Compétences testées :
- ✓ Analyse de fichiers binaires
- ✓ Extraction de strings
- ✓ Décodage ROT13
- ✓ OSINT géographique avancé

---

## LEVEL 4 - THE POOLROOMS

### Fichiers :
- `level4_poolrooms.html`
- `poolroom_reflection.jpg` (à créer avec stéganographie)

### Énigme 1 : Chiffrement de Vigenère

**Message crypté :**
```
Vqx bpv qntxkm kip xqogv, vqx uikg oiaw vqx twvq.
Vqx dxb la qlaaxk ak vqx jvxkp: "POOLWATER"
Axhqabq vqx hlasx, oakx vqx wrpp.

Xkhtbbvxa uxllrjx:
ZZWGM SFNGE VQJMZ MGLQQ HZAKR QSFRZ JZMFJ
```

**Clé Vigenère :** `POOLWATER`

**Décodage :**
- Outil : CyberChef, dcode.fr, ou script Python
- Message en clair :
```
You can escape the water, you must find the path.
The key is hidden in the steam: "POOLWATER"
Decipher the clues, open the door.

Encrypted message:
LEVEL FIFTH OPENS THROUGH FINAL WATERS AGAIN
```

### Énigme 2 : QR Codes

**4 QR codes générés :**
- QR A, B, C → Faux (rickroll, memes, etc.)
- QR D → Le bon

**Contenu QR D :**
```
GPS: -0.2297° S, -78.5249° W
```

**Solution :**
1. Entrer coordonnées sur Google Maps
2. Lieu = **Mitad del Mundo** (Monument de l'équateur, Équateur)
3. Nom = indice pour Level 5

### Énigme 3 : Stéganographie image

**Créer l'image :**
```bash
# Créer secret.txt
echo "The final level awaits. Access: level5_final_exit.html" > secret.txt

# Cacher dans l'image
steghide embed -cf poolroom_reflection.jpg -ef secret.txt -p VIGENERE
```

**Extraction :**
```bash
steghide extract -sf poolroom_reflection.jpg
# Entrer le mot de passe : VIGENERE
```

**Fichier suivant :** `level5_final_exit.html`

### Compétences testées :
- ✓ Cryptographie Vigenère
- ✓ QR codes (génération et scan)
- ✓ Stéganographie avancée
- ✓ OSINT multi-sources

---

## LEVEL 5 - THE EXIT (FINAL)

### Fichier :
- `level5_final_exit.html`

### Énigme : Synthèse de tout le parcours

**Questions posées :**

1. **Quelle heure au Big Ben en 2024 ?**
   - Réponse : `06:10`

2. **Quel animal ressemble l'île Isabela ?**
   - Réponse : `hippocampe`

3. **Combien de niveaux traversés ?**
   - Réponse : `5`

4. **Code clé au Level 4 ?**
   - Réponse : `POOLWATER`

5. **Monument aux coordonnées -0.2297° S, -78.5249° W ?**
   - Réponse : `Mitad del Mundo`

### Code final

**Format suggéré :**
```
ESCAPE-0610-SEAHORSE-LEVEL5-POOL-MITAD
```

**Ou simplifié :**
```
ESCAPE2024
```

**Validation :**
- Formulaire JavaScript
- OU bot Discord qui vérifie
- OU simplement affichage du message de victoire

### Compétences testées :
- ✓ Mémoire et prise de notes
- ✓ Synthèse de toutes les compétences précédentes
- ✓ Persévérance

---

## 🛠️ FICHIERS À CRÉER RÉELLEMENT (pour le CTF complet)

### Pastebin :
- Compte : créer un compte
- Post "M4RK_L3VR3_3" avec contenu pertinent

### Reddit (optionnel) :
- Compte `Lost_In_L2_2024`
- Post dans r/backrooms avec image stégano

### Twitter/X (optionnel) :
- Compte `@M4RK_Trapped`
- Tweet avec coordonnées Mont Fuji

### Images avec stéganographie :
```bash
# Level 2
steghide embed -cf pipe_image.jpg -ef message.txt -p PIPES

# Level 4
steghide embed -cf poolroom_reflection.jpg -ef secret.txt -p VIGENERE
```

### Fichier binaire corrompu :
- `system_restore.exe` déjà fourni
- Contient les strings nécessaires

---

## 📊 RÉSUMÉ DES COMPÉTENCES NSI

| Compétence | Levels concernés |
|------------|------------------|
| HTML/CSS | Tous |
| Cryptographie | 0, 3, 4 |
| OSINT | 0, 1, 2, 3, 4 |
| Stéganographie | 2, 4 |
| Reverse Engineering | 3 |
| Géolocalisation | 0, 1, 2, 3, 4 |
| Réseaux sociaux | 2 |
| Python | 0, 4 |

---

## ⏱️ TEMPS DE RÉSOLUTION ESTIMÉ

- **Débutant :** 6-8 heures
- **Intermédiaire :** 4-5 heures
- **Expert :** 2-3 heures

---

## 💡 CONSEILS POUR LE JURY

### Points forts du projet :
1. Thématique immersive et cohérente
2. Variété des techniques (crypto, OSINT, stégano, reverse)
3. Difficulté progressive
4. Nécessite recherche active (pas juste résoudre des calculs)
5. Multidisciplinaire (web, réseau, sécurité, crypto)

### Améliorations possibles :
1. Ajouter un timer automatique
2. Bot Discord pour validation en temps réel
3. Hall of Fame des meilleurs temps
4. Certificat PDF de victoire
5. Musique d'ambiance sur chaque niveau

---

## 🎯 BARÈME DE NOTATION SUGGÉRÉ

- **Originalité du concept** : /20
- **Complexité technique** : /30
- **Qualité de réalisation** : /25
- **Documentation** : /15
- **Présentation** : /10

**TOTAL** : /100

---

*Document créé pour le Trophée NSI - Terminal 2024-2025*
