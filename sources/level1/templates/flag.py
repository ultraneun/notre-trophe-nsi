# flags.py

CHALLENGES = {
    0: {
        "nom": "Niveau 0 - Les Bureaux Jaunes",
        "description": "Tu viens de clipper. Les murs jaunes s'étendent à l'infini. \
Quelqu'un a laissé un message caché dans cette page...",
        "type": "html_cache",   # le flag est caché dans le code source HTML
        "flag": "BCKRM{w3lc0m3_t0_th3_backr00ms}",
        "points": 100,
        "indice": "Fais clic droit → Inspecter l'élément 👀"
    },
    1: {
        "nom": "Niveau 1 - Le Parking",
        "description": "L'humidité colle à ta peau. Une note est scotchée sur un pilier. \
Elle est illisible... ou presque : `QkNLUk17bjBfY2wxcF9uMF8zc2M0cDN9`",
        "type": "base64",       # le flag est encodé en base64 dans la description
        "flag": "BCKRM{n0_cl1p_n0_3sc4p3}",
        "points": 200,
        "indice": "Base64... ça te dit quelque chose ?"
    },
    2: {
        "nom": "Niveau 2 - La Piscine",
        "description": "L'eau ne reflète rien. Au fond, une image flotte. \
Télécharge-la et regarde de plus près.",
        "type": "steganographie",  # le flag est caché dans une image
        "flag": "BCKRM{th3_3nt1ty_s4w_y0u}",
        "points": 300,
        "indice": "Les métadonnées d'une image peuvent cacher des secrets..."
    },
    3: {
        "nom": "Niveau 3 - Les Salles de Fête",
        "description": "La musique joue en boucle depuis des années. \
Un script Python tourne sur un vieux PC dans le coin. \
Qu'est-ce qu'il calcule ? \n\ndef secret(n):\n    return n * 7 + 3\n\nTrouve x tel que secret(x) == 108",
        "type": "code",         # le joueur doit résoudre une énigme Python
        "flag": "BCKRM{15_3st_l4_r3p0ns3}",
        "points": 400,
        "indice": "Résous l'équation : x * 7 + 3 = 108"
    },
}
```

---

**Ce que tu peux personnaliser facilement :**

- `"nom"` → le titre affiché
- `"description"` → le texte narratif du niveau
- `"flag"` → la réponse que le joueur doit trouver
- `"points"` → la valeur du challenge
- `"indice"` → un hint si le joueur est bloqué

---

**Le niveau 3 en détail** — l'énigme Python :
```
x * 7 + 3 = 108
x * 7 = 105
x = 15  ✅