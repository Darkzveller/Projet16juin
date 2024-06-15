import time
import pyautogui
import webbrowser
import easyocr

# Ouvrir le lien dans un navigateur web
webbrowser.open("https://www.snapchat.com/add/naslachiente/dX6SMH4gRGOdtCKqVvUksAAAgdnZ1ZHl3emZrAZAToFL6AZAToEAAAAAAAA")

# Attendre 5 secondes pour que la page se charge
time.sleep(5)
fichier = 'img.png'

# Initialiser le lecteur OCR
reader = easyocr.Reader(['fr'])

def process_image():
    x = 764
    y = 440
    width = 394
    height = 252
    
    # Prendre une capture d'écran
    screen = pyautogui.screenshot(region=(x, y, width, height))
    screen.save(fichier)

    # Lire le texte à partir de l'image
    result = reader.readtext(fichier)
    
    # Initialiser une liste pour les motifs trouvés dans l'ordre
    motifs_trouves = []
    
    # Parcourir les résultats pour rechercher quatre motifs de chiffres différents consécutivement
    for (bbox, mot, prob) in result:
        # Supprimer les espaces du motif pour le traitement
        mot_sans_espace = mot.replace(' ', '')
        
        if len(mot_sans_espace) == 4 and mot_sans_espace.isdigit() and mot_sans_espace not in motifs_trouves:
            motifs_trouves.append(mot_sans_espace)
            
            # Vérifier si nous avons trouvé quatre motifs différents consécutivement
            if len(motifs_trouves) == 4:
                print(f"Motifs consécutifs trouvés dans l'ordre : {motifs_trouves}")
                break

# Appeler la fonction pour traiter l'image
process_image()














import time
import pyautogui
import webbrowser
import easyocr

# Ouvrir le lien dans un navigateur web
webbrowser.open("https://www.snapchat.com/add/naslachiente/dX6SMH4gRGOdtCKqVvUksAAAgdnZ1ZHl3emZrAZAToFL6AZAToEAAAAAAAA")

# Attendre 5 secondes pour que la page se charge
time.sleep(5)
fichier = 'img.png'

# Initialiser le lecteur OCR
reader = easyocr.Reader(['fr'])

def process_image():
    x = 700
    y = 400
    width = 400
    height = 250
    
    # Prendre une capture d'écran
    screen = pyautogui.screenshot(region=(x, y, width, height))
    screen.save(fichier)

    # Lire le texte à partir de l'image
    result = reader.readtext(fichier)
    
    # Variable pour le motif composé trouvé
    motif_compose = None
    
    # Parcourir les résultats pour rechercher le motif composé spécifique
    for (bbox, mot, prob) in result:
        # Supprimer les espaces du motif pour le traitement
        mot_sans_espace = mot.replace(' ', '')
        
        # Vérifier si le motif composé est trouvé
        if len(mot_sans_espace) == 5 and mot_sans_espace[2] == '/' and mot_sans_espace[:2].isdigit() and mot_sans_espace[3:].isdigit():
            motif_compose = mot_sans_espace
            print(f"Motif composé trouvé : {motif_compose}")
            break
    
    # Si aucun motif composé n'a été trouvé, afficher un message
    if motif_compose is None:
        print("Aucun motif composé de la forme 'XX/XX' n'a été trouvé.")

# Appeler la fonction pour traiter l'image
process_image()












import time
import pyautogui
import webbrowser
import easyocr
import requests
from PIL import Image
from io import BytesIO

# URL de l'image à analyser
image_url = "https://www.snapchat.com/add/naslachiente/dX6SMH4gRGOdtCKqVvUksAAAgdnZ1ZHl3emZrAZAToFL6AZAToEAAAAAAAA"

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


























#Coucou batard
from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.ldlc.com/")
    page.click(".icon.icon-user")
    page.fill("#Email", "dzvellox@gmail.com")
    page.wait_for_timeout(3000)
    page.fill(".input-group input", "Dark2008@")
    page.wait_for_timeout(4000)
    page.wait_for_selector(".button")
    page.click("form button.button")
    page.wait_for_timeout(2000)
    page.click(".icon.icon-basket")
    page.wait_for_timeout(1500)
    page.click(".maxi.color2.noMarg")

    motifs_trouves = "1234 5678 9012 3456"
    motif_compose ="11/22"
    #prenon
    Card_Holder = "nasdas"
    motif_cvv = "234"
    




    
    #a refaire cette partir puisque system de payment ne marche pas
    page.wait_for_load_state("networkidle")  # Attendre que la page soit chargée
    page.wait_for_selector(".sdpx-hosted-cardNumber")  # Attendre que l'élément soit présent
    page.click(".sdpx-hosted-cardNumber")  # Cliquer sur l'élément
    page.fill(".sdpx-hosted-cardNumber", motifs_trouves)  # Remplir le champ

    

    page.wait_for_selector("#sdpx-hosted-cardExpiryDate")
    page.fill("#sdpx-hosted-cardExpiryDate", motif_compose)

    page.wait_for_selector("#CardHolder")
    page.fill("#CardHolder", "nasdas")

    page.wait_for_selector("#sdpx-hosted-cardCvc")
    page.fill("#sdpx-hosted-cardCvc", motif_cvv )

    page.screenshot(path="example.png")
    page.wait_for_timeout(20000)
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
