import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    URL = "https://denticloud.co"

    USERNAME_FIELD = (By.CSS_SELECTOR, 'input[type="email"]')
    PASSWORD_FIELD = (By.CSS_SELECTOR, 'input[type="password"]')
    LOGIN_BUTTON = (By.XPATH, "//div[@class='font-lato']/div/div/div/button")  # Adjusted XPath

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def open(self):
        print("[Step] Opening home page...")
        self.driver.get(self.URL)
        time.sleep(2)  # Allow time for page to load

    def login(self, username, password):
        print(f"[Step] Filling in username: {username}")
        self.wait.until(EC.element_to_be_clickable(self.USERNAME_FIELD)).send_keys(username)

        print(f"[Step] Filling in password.")
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD)).send_keys(password)

        print(f"[Step] Submitting login form.")
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()
        time.sleep(2)

    def is_logged_in(self):
        print("[Step] Checking for successful login...")
        self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")
        return "dashboard" in self.driver.current_url.lower()
