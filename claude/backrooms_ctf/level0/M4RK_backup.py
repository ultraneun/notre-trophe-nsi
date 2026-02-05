#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
M4RK's Backup System - Version 3.7.1
Emergency Photo Metadata Extractor

[FICHIER PARTIELLEMENT CORROMPU]
[DERNIÈRE MODIFICATION: 2024-01-15 14:32:07]
"""

import sys
import base64

# ATTENTION : Ce script contient des erreurs volontaires
# M4RK était pressé quand il l'a écrit

class PhotoMetadata:
    def __init__(self):
        self.location = None
        self.timestamp = None
        self.camera = None
        self.hidden_data = None
        
    def extract_metadata(self, photo_data):
        """
        Extrait les métadonnées d'une photo
        Mais ce code est cassé... ou pas ?
        """
        # Coordonnées GPS de la dernière photo
        # Prise à la Tour Eiffel, Paris
        self.location = {
            'latitude': 48.8584,
            'longitude': 2.2945,
            'altitude': 324,  # mètres
            'location_name': 'Tour Eiffel, Paris, France'
        }
        
        # Timestamp de la photo
        # Format: YYYY-MM-DD HH:MM:SS
        # Mais... l'heure est incorrecte ici
        # C'est PAS la vraie heure de la photo
        self.timestamp = "2024-01-15 14:32:07"
        
        # Info caméra
        self.camera = "iPhone 13 Pro"
        
        # Données cachées (encodées en base64)
        # M4RK a caché quelque chose ici
        self.hidden_data = "VGhlIHJlYWwgdGltZSBpcyBub3QgaW4gdGhpcyBmaWxlLgpZb3UgbmVlZCB0byBGSU5EIGl0LgpHbyB0byB0aGUgY29vcmRpbmF0ZXMuCkxvb2sgYXQgdGhlIHZpZXcgZnJvbSAyMDI0Lgpbwqd04YeEPC3iiaXiiaDCqV3huIjiiJjiiaXiiaDEu-KImOG4iF0="
        
        return True
    
    def decode_hidden_message(self):
        """
        Décode le message caché
        Mais seulement si tu le demandes explicitement
        """
        try:
            decoded = base64.b64decode(self.hidden_data).decode('utf-8')
            return decoded
        except:
            return "[ERREUR: Impossible de décoder]"
    
    def get_next_clue(self):
        """
        Retourne l'indice pour le prochain level
        """
        # Le nom du fichier suivant dépend de l'heure trouvée
        # Format: level1_key_[TIME].html
        # Où [TIME] est au format HH:MM (24h)
        
        # Mais quelle heure ?
        # Pas celle dans self.timestamp
        # Pas 14:32
        # Pas 06:10 non plus
        
        # Tu dois VRAIMENT aller voir les coordonnées GPS
        # Sur Google Maps / Street View
        # En 2024
        # Et trouver une horloge
        
        print("\n[INDICE SYSTÈME]")
        print("Format du fichier: level1_key_XX:XX.html")
        print("Remplace XX:XX par l'heure trouvée")
        print("\nMais d'abord, trouve l'heure.")
        print("Va aux coordonnées. Regarde autour de toi.")
        print("En 2024. Une horloge. Un temps figé.")


def main():
    print("=" * 60)
    print("M4RK's PHOTO METADATA EXTRACTOR")
    print("=" * 60)
    print("\n[AVERTISSEMENT] Fichier partiellement corrompu")
    print("[AVERTISSEMENT] Certaines données peuvent être incorrectes")
    
    metadata = PhotoMetadata()
    
    print("\n[INFO] Extraction des métadonnées de la dernière photo...")
    metadata.extract_metadata(None)
    
    print("\n[LOCATION DATA]")
    print(f"  Latitude  : {metadata.location['latitude']}° N")
    print(f"  Longitude : {metadata.location['longitude']}° E")
    print(f"  Lieu      : {metadata.location['location_name']}")
    print(f"  Altitude  : {metadata.location['altitude']}m")
    
    print("\n[TIMESTAMP DATA]")
    print(f"  Date/Heure : {metadata.timestamp}")
    print(f"  ⚠ ATTENTION : Cette heure est INCORRECTE")
    print(f"  ⚠ Trouvez la vraie heure en allant à cette position")
    
    print("\n[CAMERA INFO]")
    print(f"  Modèle : {metadata.camera}")
    
    print("\n[HIDDEN DATA DETECTED]")
    choice = input("Voulez-vous décoder les données cachées ? (o/n): ")
    
    if choice.lower() == 'o':
        decoded_msg = metadata.decode_hidden_message()
        print("\n[MESSAGE CACHÉ]")
        print(decoded_msg)
    
    print("\n" + "=" * 60)
    metadata.get_next_clue()
    print("=" * 60)


# Easter Egg dans le code
# Si tu lis ça, tu es sur la bonne voie
# Mais les coordonnées GPS ne suffisent pas
# Tu dois VOIR la Tour Eiffel
# En 2024
# Et trouver l'heure sur une horloge visible

# Indice bonus : Ce n'est pas 14:32
# Ce n'est pas non plus l'heure qu'il est maintenant
# C'est l'heure FIGÉE sur une vue de 2024

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[INTERRUPTION] Programme arrêté")
        print("M4RK est toujours coincé quelque part...")
        sys.exit(0)


"""
DEBUG NOTES (pour M4RK):

Dernière photo prise : Tour Eiffel, matin du 15/01/2024
Position exacte : 48.8584° N, 2.2945° E
L'horloge de Big Ben visible sur une vue de la Tour (wtf???)

Attends non, je confonds tout
C'est pas Big Ben
C'est une horloge À la Tour Eiffel
Ou une montre
Ou...

Je sais plus. Mon esprit est confus ici.
Tout se mélange.

Trouve l'heure. C'est tout ce qui compte.

Les coordonnées du Big Ben sont : 51.5007° N, 0.1246° W
Mais c'est pas ça qu'il faut chercher

OU PEUT-ÊTRE QUE SI ???

Merde je deviens fou ici

[FIN DES NOTES]
"""
