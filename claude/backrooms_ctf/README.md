# 🎮 BACKROOMS CTF - ESCAPE THE MAZE

## Projet NSI Terminal - Trophée NSI 2024-2025

---

## 🎯 CONCEPT

Un CTF (Capture The Flag) immersif basé sur le thème des Backrooms.

**Histoire :** M4RK, un développeur, est coincé dans les Backrooms après avoir "noclippé" hors de la réalité. Il laisse des messages et indices partout pour trouver la sortie. Le joueur doit résoudre des énigmes cryptographiques, OSINT, stéganographie, et reverse engineering pour progresser à travers 6 niveaux.

**Objectif :** Échapper des Backrooms en résolvant toutes les énigmes.

---

## 📂 STRUCTURE DU PROJET

```
backrooms_ctf/
│
├── level0/           Level 0 - The Lobby (Introduction)
│   ├── entry_log.html
│   ├── distress_signal.txt
│   └── M4RK_backup.py
│
├── level1/           Level 1 - The Dark (Géographie)
│   └── level1_key_06:10.html
│
├── level2/           Level 2 - The Pipes (OSINT)
│   └── level2_access_isabela.html
│
├── level3/           Level 3 - The Electrical Station (Reverse)
│   ├── level3_the_electrical_station.html
│   └── system_restore.exe
│
├── level4/           Level 4 - The Poolrooms (Crypto avancée)
│   └── level4_poolrooms.html
│
├── level5/           Level 5 - The Exit (Final)
│   └── level5_final_exit.html
│
└── solutions/        Solutions complètes (pour le jury)
    └── SOLUTIONS_COMPLETES.md
```

---

## 🚀 COMMENT JOUER

### Point de départ :
Ouvrir `level0/entry_log.html` dans un navigateur.

### Règles :
1. Chaque level contient des énigmes à résoudre
2. La résolution débloque le nom du fichier suivant
3. Certaines énigmes nécessitent des outils externes (Google Maps, CyberChef, etc.)
4. Prendre des notes est ESSENTIEL
5. Tout est logique, mais parfois bien caché

### Outils recommandés :
- **Navigateur web** (Firefox, Chrome)
- **Éditeur de texte** (Notepad++, VS Code)
- **CyberChef** (décodage : https://gchq.github.io/CyberChef)
- **Google Maps** (OSINT géographique)
- **Éditeur hexadécimal** (HxD, xxd, hexed.it)
- **Steghide** (stéganographie)
- **Python 3** (pour certains scripts)

---

## 🧩 APERÇU DES ÉNIGMES

### Level 0 - The Lobby
- Décodage Base64
- OSINT Google Maps
- Recherche de coordonnées GPS
- **Difficulté** : ⭐ Facile

### Level 1 - The Dark
- Recherche géographique
- Identification de formes d'îles
- Culture générale (Galápagos)
- **Difficulté** : ⭐⭐ Facile-Moyen

### Level 2 - The Pipes
- OSINT réseaux sociaux (Twitter, Reddit)
- Stéganographie (steghide)
- Recherche d'actualités 2024
- **Difficulté** : ⭐⭐⭐ Moyen

### Level 3 - The Electrical Station
- Analyse hexadécimale de fichier
- Extraction de strings
- Décodage ROT13
- OSINT multi-sources
- **Difficulté** : ⭐⭐⭐⭐ Difficile

### Level 4 - The Poolrooms
- Chiffrement de Vigenère
- QR codes (vrais et faux)
- Stéganographie avancée
- Coordonnées GPS complexes
- **Difficulté** : ⭐⭐⭐⭐ Difficile

### Level 5 - The Exit
- Synthèse de toutes les énigmes
- Questions récapitulatives
- Code final combiné
- **Difficulté** : ⭐⭐⭐⭐⭐ Très difficile

---

## 🛠️ COMPÉTENCES NSI MOBILISÉES

### Programmation :
- Python (scripts, cryptographie)
- JavaScript (validation, interactions)
- HTML/CSS (structure des pages)

### Cryptographie :
- Base64 (encodage)
- ROT13 (chiffrement par substitution)
- Vigenère (chiffrement polyalphabétique)
- Stéganographie (données cachées)

### Réseau & Web :
- Code source HTML
- OSINT (Open Source Intelligence)
- APIs géographiques (Google Maps)

### Sécurité :
- Reverse engineering (analyse binaire)
- Extraction de strings
- Analyse hexadécimale

### Bases de données / Stockage :
- Métadonnées (EXIF)
- Fichiers binaires

---

## ⏱️ TEMPS DE JEU ESTIMÉ

- **Joueur débutant** : 6-8 heures
- **Joueur intermédiaire** : 4-5 heures
- **Joueur expert** : 2-3 heures

---

## 📝 NOTES IMPORTANTES

### Pour les joueurs :
- **Prenez des notes** de TOUT (coordonnées, codes, indices)
- Regardez TOUJOURS le code source des pages HTML
- Si vous êtes bloqués >30 min, consultez un indice
- Certaines énigmes nécessitent de créer des comptes (Pastebin, etc.)

### Pour les créateurs (vous) :
Ce projet est **partiellement complet**. Pour un CTF 100% fonctionnel, vous devez :

1. **Créer les comptes réseaux sociaux :**
   - Pastebin avec post "M4RK_L3VR3_3"
   - (Optionnel) Reddit `Lost_In_L2_2024`
   - (Optionnel) Twitter `@M4RK_Trapped`

2. **Créer les images avec stéganographie :**
   ```bash
   steghide embed -cf pipe_image.jpg -ef message.txt -p PIPES
   steghide embed -cf poolroom_reflection.jpg -ef secret.txt -p VIGENERE
   ```

3. **Générer les QR codes :**
   - 4 QR codes pour Level 4
   - 3 faux, 1 vrai avec coordonnées GPS

4. **Ajuster les énigmes :**
   - Vérifier que toutes les infos 2024 sont à jour
   - Adapter les coordonnées GPS si besoin
   - Personnaliser les messages

---

## 🎓 POUR LE JURY / ENSEIGNANTS

Un document de **solutions complètes** est disponible dans :
`solutions/SOLUTIONS_COMPLETES.md`

Il contient :
- Toutes les réponses
- Les étapes de résolution
- Les outils à utiliser
- Le barème de notation suggéré

---

## 🏆 OBJECTIFS PÉDAGOGIQUES

Ce projet démontre la maîtrise de :

1. **Programmation web** (HTML/CSS/JS)
2. **Cryptographie** (chiffrements classiques et modernes)
3. **OSINT** (recherche d'informations en ligne)
4. **Sécurité informatique** (reverse, stégano)
5. **Géolocalisation** (coordonnées GPS, cartes)
6. **Gestion de projet** (planification, documentation)
7. **Créativité** (thématique immersive)

---

## 👥 ÉQUIPE

[VOS 4 NOMS]

**Rôles :**
- Développeur Web : [Nom]
- Cryptographe : [Nom]
- Intégrateur OSINT : [Nom]
- Chef de projet / Testeur : [Nom]

**Classe :** Terminal NSI  
**Année :** 2024-2025  
**Établissement :** [Votre lycée]

---

## 📞 CONTACT

Pour toute question ou bug :
- Email : [votre email]
- Discord : [votre Discord]

---

## 📜 LICENCE & CRÉDITS

**Thème :** Les Backrooms (domaine public, création communautaire)  
**Projet :** Original, créé pour le Trophée NSI  
**Code :** Libre d'utilisation dans un cadre éducatif

---

## 🚨 AVERTISSEMENT

Ce CTF contient des énigmes difficiles nécessitant :
- Recherche active sur internet
- Utilisation d'outils de cryptographie
- Analyse de fichiers
- Patience et persévérance

**Déconseillé aux joueurs facilement frustrés !** 😄

Mais si vous êtes bloqués, les indices sont là pour vous aider.

---

## 🎮 COMMENCER À JOUER

### Installation :
Aucune installation nécessaire ! Tout fonctionne dans un navigateur.

### Lancement :
1. Télécharger/Cloner ce repository
2. Ouvrir `level0/entry_log.html` dans votre navigateur
3. Lire attentivement tous les messages
4. Commencer à chercher !

### Premier indice gratuit :
Si vous êtes perdus au Level 0, rappelez-vous :
- Les coordonnées GPS sont écrites en clair
- Google Maps est votre ami
- Regardez le code source HTML (Clic droit → Afficher le code source)
- Il y a un message en Base64 dans un commentaire

---

**Bonne chance. Vous en aurez besoin.**

*"If you're not careful and noclip out of reality in the wrong areas, you'll end up in the Backrooms..."*

---

**VERSION** : 1.0  
**DERNIÈRE MISE À JOUR** : Janvier 2025
