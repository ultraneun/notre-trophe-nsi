# 🚪 Frontrooms

> *"Ce que vous voyez n'est peut-être pas ce que vous cherchez."*

**Frontrooms** est un jeu d'énigmes et d'exploration psychologique inspiré de l'univers des Backrooms et des mystères Internet comme Cicada 3301. Le concept repose sur une immersion totale dans des espaces liminaux — des lieux familiers mais profondément dérangeants — où la progression dépend de la capacité du joueur à décoder son environnement.

L'objectif est de s'échapper de **6 niveaux thématiques** (du niveau 0 au niveau 5). Contrairement à un jeu d'action classique, **la réflexion est l'arme principale** : il faut analyser des fréquences sonores, manipuler des fichiers, utiliser des outils de géolocalisation réels et résoudre des puzzles logiques complexes pour progresser.

---

## 📋 Table des matières

- [Pré-requis](#-pré-requis)
- [Installation](#-installation)
- [Démarrage](#-démarrage)
- [Aspects Techniques](#️-aspects-techniques)
- [Fabriqué avec](#️-fabriqué-avec)
- [Versions](#-versions)
- [Auteurs](#-auteurs)
- [Licence](#-licence)

---

## ✅ Pré-requis

Avant de commencer, assurez-vous d'avoir :

- **Python 3.x** — [Télécharger Python](https://www.python.org/downloads/)
- **Un navigateur moderne** — Chrome, Firefox, Edge ou Safari (version récente)
- **Une connexion internet** — requise pour certaines énigmes faisant appel à des outils externes (géolocalisation, etc.)

---

## 📦 Installation

1. **Clonez le dépôt :**

```bash
git clone https://github.com/votre-organisation/notre-trophe-nsi.git
cd notre-trophe-nsi
```

2. **Installez les dépendances Python nécessaires :**

```bash
pip install flask
```

> Ou si un fichier `requirements.txt` est présent :

```bash
pip install -r requirements.txt
```

---

## 🚀 Démarrage

Lancez le serveur Flask avec la commande suivante depuis la racine du dépôt :

```bash
python sources/main.py
```

Une fois lancé, ouvrez votre navigateur et rendez-vous à l'adresse :

```
http://127.0.0.1:5000
```

> 💡 **Conseil :** Jouez dans un environnement calme, avec un casque audio. Certaines énigmes reposent sur l'écoute attentive.

---

## 🛠️ Aspects Techniques

Ce projet met en œuvre plusieurs concepts avancés du programme de **NSI** :

| Domaine | Description |
|---|---|
| **Développement Web & Interface** | Interface interactive avec hotspots cliquables et effets de texte dynamiques (typewriter) |
| **Traitement de données** | Analyse de spectrogrammes audio pour la stéganographie et décodage de signaux (Code Morse) |
| **Logique Algorithmique** | Séquences logiques, drag-and-drop pour les puzzles, timers pour les phases de survie |
| **Interactivité Externe** | Intégration de Google Maps / Street View pour la résolution d'énigmes géographiques |

---

## 🗂️ Structure du projet

```
frontrooms/
├── sources/
│   └── main.py          # Point d'entrée du projet
├── static/
│   ├── css/             # Feuilles de style
│   ├── js/              # Scripts JavaScript
│   └── assets/          # Médias (images, sons, fichiers cachés...)
├── templates/           # Pages HTML des niveaux
├── requirements.txt     # Dépendances Python
└── README.md
```

---

## ⚙️ Fabriqué avec

- **Python 3** — Serveur backend et logique principale
- **Flask** — Framework web pour le serveur local (`http://127.0.0.1:5000`)
- **HTML5 / CSS3** — Structure et mise en page des niveaux
- **JavaScript** — Interactivité, puzzles et effets visuels
- **Web Audio API** — Analyse et génération de fréquences sonores
- **Google Maps / Street View** — Énigmes de géolocalisation

---

## 🔖 Versions

- `v1.0.0` — Version initiale : 6 niveaux jouables, puzzles complets, ambiance visuelle finalisée.

---

## 👥 Auteurs

| Pseudo | Rôle |
|---|---|
| **Anas El Adarissi** ([@ultraneun](https://github.com/ultraneun)) | Chef de projet, base de données, testeur principal |
| **Lénaël Lapeine** ([@LenGame](https://github.com/LenGame)) | Architecte backend, débogage et stabilité technique |
| **Alexandre Blacharz** ([@Alekzio](https://github.com/Alekzio)) | Concepteur des énigmes, expert Backrooms, ingénieur des "fausses bonnes idées" |
| **Robin Sanders** ([@rbnnn111](https://github.com/rbnnn111)) | Directeur créatif, création des niveaux, ambiance visuelle |

> *Projet développé en collaboration constante, mêlant narration cryptique et défis techniques.*

---

## 📜 Licence

Ce projet est distribué sous une double licence :

- **Code source** — [GNU General Public License v3.0 (GPLv3)](./Licence.txt)
- **Documentation** (fichiers `.md`, `.txt`) — [Creative Commons CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)

Vous trouverez le texte complet de la licence GPLv3 dans le fichier [`Licence.txt`](./Licence.txt).
