from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def wait_and_click(browser, by, value, timeout=10):
    try:
        element = WebDriverWait(browser, timeout).until(
            EC.element_to_be_clickable((by, value))
        )
        time.sleep(random.uniform(1, 2))
        element.click()
        return True
    except Exception as e:
        logger.error(f"Error clicking element: {str(e)}")
        return False

def follow_user(browser, user_id):
    try:
        # Navigate to user profile
        browser.get(f"https://roblox.com/users/{user_id}")
        time.sleep(random.uniform(2, 3))
        
        # Click the More button using the specific class names
        more_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 
                'button.profile-header-dropdown[aria-label="See More"]'))
        )
        more_button.click()
        time.sleep(random.uniform(1, 2))
        
        # Click the follow button using the specific follow button XPath
        follow_button = WebDriverWait(browser, 10).until(
           EC.element_to_be_clickable((By.XPATH, '//*[@id="follow-button"]'))
        )
        follow_button.click()
        return True
        
    except Exception as e:
        return False

def main():
    try:
        browser_choice = input("Choose browser (1 Chrome, 2 Safari, 3 Firefox, 4 Edge): ")
        username = input("Roblox Username: ")
        password = input("Roblox Password: ")
        
        browsers = {
            "1": ("Chrome", webdriver.Chrome),
            "2": ("Safari", webdriver.Safari),
            "3": ("Firefox", webdriver.Firefox),
            "4": ("Edge", webdriver.Edge)
        }
        
        if browser_choice not in browsers:
            raise ValueError("Invalid browser selection!")
            
        browser_name, browser_class = browsers[browser_choice]
        logger.info(f"Opening {browser_name}...")
        browser = browser_class()
        
        # Login
        logger.info("Logging in...")
        browser.get("https://roblox.com/login")
        
        username_field = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "login-username"))
        )
        password_field = browser.find_element(By.ID, "login-password")
        
        username_field.send_keys(username)
        password_field.send_keys(password)
        
        login_button = browser.find_element(By.ID, "login-button")
        login_button.click()
        
        time.sleep(3)
        
        # Main loop
        while True:
            try:
                user_id = random.randint(100000000, 1000000000)
                if follow_user(browser, user_id):
                    time.sleep(1)
                else:
                    time.sleep(1)
                    
            except KeyboardInterrupt:
                logger.info("\nStopping program...")
                break
            except Exception as e:
                time.sleep(2)
                
    except Exception as e:
        logger.error(f"Critical error: {str(e)}")
    finally:
        if 'browser' in locals():
            browser.quit()
            logger.info("Browser closed")

if __name__ == "__main__":
    main()
