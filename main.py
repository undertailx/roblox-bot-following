from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# รับข้อมูลจากผู้ใช้ (Prompt user for input)
putBrowser = input("Please enter the number to choose your browser (1 is Chrome, 2 is Safari, 3 is Firefox): ")
putUsername = input("Type your Roblox Account username here: ")
putPassword = input("Type Roblox Account Password here: ")

# เลือกเบราว์เซอร์ที่ต้องการใช้งาน (Select the browser based on user input)
match putBrowser:
    case "1":
        print("Ok. Starting Chrome... ")
        browser = webdriver.Chrome()  # เปิดเบราว์เซอร์ Chrome
    case "2":
        print("Ok. Starting Safari... ")
        browser = webdriver.Safari()  # เปิดเบราว์เซอร์ Safari
    case "3":
        print("Ok. Starting Firefox... ")
        browser = webdriver.Firefox()  # เปิดเบราว์เซอร์ Firefox
    case _:
        print("Unknown browser!")  # หากเลือกเบราว์เซอร์ไม่ถูกต้อง จะหยุดโปรแกรม
        exit()

# เข้าสู่ระบบ Roblox (Navigate to the Roblox login page)
print("Logging in... ")
browser.get("https://roblox.com/login")

# รอให้ input field สำหรับ username และ password โหลดขึ้นมา (Wait for the username and password fields to load)
WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "login-username")))
username = browser.find_element(By.ID, "login-username")  # หา input field สำหรับ username
password = browser.find_element(By.ID, "login-password")  # หา input field สำหรับ password

# กรอก username และ password (Enter the username and password into the respective fields)
username.send_keys(putUsername)
password.send_keys(putPassword)

# คลิกปุ่มล็อกอิน (Click the login button)
loginBtn = browser.find_element(By.ID, "login-button")
loginBtn.click()

# รอให้เข้าสู่ระบบสำเร็จ (Wait for the login process to complete)
time.sleep(10)

# ลูปสำหรับการติดตามผู้ใช้แบบสุ่ม (Loop for following a random user)
while True:
    # สุ่มเลือก ID ผู้ใช้ (Randomly select a user ID)
    idRandom = random.randint(100000000, 1000000000)  # สามารถปรับช่วง ID ได้ตามต้องการ (Adjust the ID range as needed)
    print("Following user with ID:", idRandom)

    # เข้าหน้าของผู้ใช้ที่ต้องการติดตาม (Go to the user's page that we want to follow)
    browser.get(f"https://roblox.com/users/{idRandom}")

    try:
        # รอให้ตัวเลือกผู้ใช้โหลดขึ้นมา (Wait for the user options to load)
        WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.ID, "popover-link"))
        )
        userOptions = browser.find_element(By.ID, "popover-link")
        userOptions.click()  # คลิกที่ตัวเลือกของผู้ใช้ (Click on the user options)
        time.sleep(2)

        # หาปุ่ม Follow โดยใช้ XPath (Find the Follow button using XPath)
        followUser = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Follow')]"))
        )
        followUser.click()  # คลิกปุ่ม Follow (Click the Follow button)
        print("FOLLOWED! Moving to next random ID...")

    except Exception as e:
        print("Could not follow user with ID:", idRandom, "Error:", e)  # แสดงข้อความหากไม่สามารถติดตามผู้ใช้ได้ (Print error if unable to follow the user)

    # หน่วงเวลา 3 วินาทีก่อนสุ่มติดตามผู้ใช้ถัดไป (Wait for 3 seconds before following the next user)
    time.sleep(3)
