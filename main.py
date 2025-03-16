from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# 获取用户输入 (Prompt user for input)
putBrowser = input("Please enter the number to choose your browser (1 Chrome, 2 Safari, 3 Firefox, 4 Edge): ")
putUsername = input("Type your Roblox Account username here: ")
putPassword = input("Type Roblox Account Password here: ")

# 选择浏览器 (Select the browser based on user input)
match putBrowser:
    case "1":
        print("Ok. Starting Chrome... ")
        browser = webdriver.Chrome()  
    case "2":
        print("Ok. Starting Safari... ")
        browser = webdriver.Safari()  
    case "3":
        print("Ok. Starting Firefox... ")
        browser = webdriver.Firefox()  
    case "4":
        print("Ok. Starting Edge... ")
        browser = webdriver.Edge()  
    case _:
        print("Unknown browser!")  
        exit()

# 访问 Roblox 登录页面 (Navigate to the Roblox login page)
print("Logging in... ")
browser.get("https://roblox.com/login")

# 等待输入框加载 (Wait for the username and password fields to load)
WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "login-username")))
username = browser.find_element(By.ID, "login-username")
password = browser.find_element(By.ID, "login-password")

# 输入用户名和密码 (Enter username and password)
username.send_keys(putUsername)
password.send_keys(putPassword)

# 点击登录按钮 (Click the login button)
loginBtn = browser.find_element(By.ID, "login-button")
loginBtn.click()

# 等待登录完成 (Wait for the login process to complete)
time.sleep(10)

# 开始循环随机关注用户 (Loop for following a random user)
while True:
    # 生成随机用户 ID (Generate a random user ID)
    idRandom = random.randint(100000000, 1000000000)
    print("Following user with ID:", idRandom)

    # 访问用户页面 (Go to the user's profile page)
    browser.get(f"https://roblox.com/users/{idRandom}")

    try:
        # 等待 "More" 按钮加载并点击 (Wait for the "More" button to appear and click it)
        WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='More']"))
        ).click()
        time.sleep(2)  # 等待菜单展开

        # 等待并点击 "Follow" 按钮 (Wait for and click the "Follow" button)
        followUser = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//li[.//span[text()='Follow']]"))
        )
        followUser.click()
        print("FOLLOWED! Moving to next random ID...")

    except Exception as e:
        print(f"Could not follow user with ID {idRandom}. Error: {e}")

    # 等待 3 秒后执行下一个操作 (Wait for 3 seconds before following the next user)
    time.sleep(3)
