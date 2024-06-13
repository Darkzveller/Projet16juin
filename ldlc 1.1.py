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


    card_number = "1234 5678 9012 3456"
    card_Expiry_Date ="11/22"
    #prenon
    Card_Holder = "nasdas"
    CVV = "234"
    
    page.wait_for_load_state("networkidle")  # Attendre que la page soit chargée
    page.wait_for_selector("#sdpx-hosted-cardNumber")  # Attendre que l'élément soit présent
    page.click("#sdpx-hosted-cardNumber")  # Cliquer sur l'élément
    page.fill("#sdpx-hosted-cardNumber", "1234 5678 9012 3456")  # Remplir le champ

    

    page.wait_for_selector("#sdpx-hosted-cardExpiryDate")
    page.fill("#sdpx-hosted-cardExpiryDate", "11/22")

    page.wait_for_selector("#CardHolder")
    page.fill("#CardHolder", "nasdas")

    page.wait_for_selector("#sdpx-hosted-cardCvc")
    page.fill("#sdpx-hosted-cardCvc", "234" )

    page.screenshot(path="example.png")
    page.wait_for_timeout(20000)
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
