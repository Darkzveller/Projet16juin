from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    
    try:
        # Aller sur la page d'accueil d'Amazon
        page.goto("https://www.amazon.fr/")
        
        # Cliquer sur le bouton de connexion
        page.click("#nav-link-accountList")
        
        # Remplir l'adresse email et le mot de passe
        page.fill("#ap_email", "votre_email@example.com")
        page.click("#continue")
        page.wait_for_timeout(3000)
        page.fill("#ap_password", "votre_mot_de_passe")
        page.wait_for_timeout(4000)
        page.click("#signInSubmit")
        
        # Attendre que la connexion soit effectuée
        page.wait_for_timeout(2000)
        
        # Aller sur la page du panier
        page.click("#nav-cart")
        page.wait_for_timeout(1500)
        
        # Cliquer pour procéder au paiement
        page.click("input[name='proceedToRetailCheckout']")
        
        # Sélectionner l'adresse de livraison (si nécessaire)
        page.wait_for_selector("[data-testid='Address_selectShipToThisAddress']", timeout=60000)
        page.click("[data-testid='Address_selectShipToThisAddress']")
        
        # Ajouter une nouvelle carte de crédit
        # Essayer avec un sélecteur de classe
        page.wait_for_selector(".a-link-emphasis.pmts-add-cc-default-trigger-link", timeout=60000)
        page.click(".a-link-emphasis.pmts-add-cc-default-trigger-link")
        
        # Augmenter le délai d'attente
        page.wait_for_load_state("networkidle")
        try:
            page.wait_for_selector("#addCreditCardNumber", timeout=60000)  # Augmenter le délai d'attente à 60 secondes
        except Exception as e:
            print(f"Erreur : {e}")
            page.screenshot(path="debug_screenshot.png")  # Prendre une capture d'écran pour diagnostiquer le problème
            browser.close()
            return
        
        # Remplir les informations de la carte bancaire
        card_number = "1234 5678 9012 3456"
        card_expiry_date = "11/22"
        card_holder = "John Doe"
        cvv = "234"
        
        page.fill("#addCreditCardNumber", card_number)
        
        page.wait_for_selector("#addCreditCardMonth")
        page.select_option("#addCreditCardMonth", "11")
        
        page.wait_for_selector("#addCreditCardYear")
        page.select_option("#addCreditCardYear", "2022")
        
        page.wait_for_selector("#ccAddCardHolderName")
        page.fill("#ccAddCardHolderName", card_holder)
        
        page.wait_for_selector("#addCreditCardVerificationNumber")
        page.fill("#addCreditCardVerificationNumber", cvv)
        
        # Confirmer les informations de paiement
        page.wait_for_selector("input.a-button-input[type='submit']")
        page.click("input.a-button-input[type='submit']")
        
        # Capturer une capture d'écran
        page.screenshot(path="amazon_example.png")
        
    except Exception as e:
        print(f"Erreur : {e}")
        page.screenshot(path="error_screenshot.png")
    finally:
        # Attendre un peu avant de fermer le navigateur
        page.wait_for_timeout(20000)
        browser.close()

with sync_playwright() as playwright:
    run(playwright)
