import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Définir l'URL de connexion et les informations d'identification
url = "https://www.instagram.com/login"
username = "Abderraouf@gmail.com"
password = "Password123"

# Démarrer un navigateur Firefox
driver = webdriver.Firefox()


# Ouvrir l'URL de connexion de Facebook
driver.get(url)
obscuring_element = WebDriverWait(driver, 1).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "._a9--._a9_1"))

)
obscuring_element.click()
# Remplir les champs de formulaire pour les informations d'identification
time.sleep(4)
email_input = driver.find_element(By.NAME, "username")
password_input = driver.find_element(By.NAME, "password")
email_input.send_keys(username)
password_input.send_keys(password)

# Cliquer sur le bouton de connexion


login_button = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "._acan._acap._acas._aj1-"))
)
login_button.click()

# Vérifier si la connexion a réussi
if "https://www.instagram.com/login" in driver.current_url:
    print("Mot de passe erroné")
else:
    print("Mot de passe correct")

# Fermer le navigateur
driver.quit()
