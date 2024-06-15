import time
import pyautogui
import webbrowser
import easyocr
import requests
from PIL import Image
from io import BytesIO

# URL de l'image à analyser
image_url = "https://www.idfcfirstbank.com/content/dam/idfcfirstbank/images/blog/credit-card/cvv-comps-1.jpg"

# Télécharger l'image
response = requests.get(image_url)
img = Image.open(BytesIO(response.content))
fichier = 'img.png'
img.save(fichier)

# Initialiser le lecteur OCR
reader = easyocr.Reader(['fr'])

def process_image():
    # Lire le texte à partir de l'image
    result = reader.readtext(fichier)
    
    # Afficher les résultats OCR pour débogage
    print("Résultats OCR :")
    for res in result:
        print(res)
    
    # Variable pour le motif CVV trouvé
    motif_cvv = None
    
    # Parcourir les résultats pour rechercher le motif CVV
    for (bbox, mot, prob) in result:
        # Supprimer les espaces et caractères non numériques pour le traitement
        mot_sans_espace = ''.join(filter(str.isdigit, mot))
        
        # Vérifier si un motif de trois ou quatre chiffres est trouvé pour CVV
        if 3 <= len(mot_sans_espace) <= 4:
            motif_cvv = mot_sans_espace
            print(f"Motif CVV trouvé : {motif_cvv}")
            break
    
    # Si aucun motif CVV n'a été trouvé, afficher un message
    if motif_cvv is None:
        print("Aucun motif CVV (3 ou 4 chiffres) n'a été trouvé.")

# Appeler la fonction pour traiter l'image
process_image()
