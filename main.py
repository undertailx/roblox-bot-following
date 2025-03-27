from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import re  
from selenium.webdriver.firefox.options import Options  

# 固定用户名和密码 (Fixed username and password)
putUsername = "typeyourusernamehere"
putPassword = "yourpassword"

# 默认使用 Firefox 浏览器 (Using Firefox browser)
print("Ok. Starting Firefox ")
firefox_options = Options()

# 启动浏览器 (Launch the browser)
browser = webdriver.Firefox(options=firefox_options)  

try:
    # 访问 Roblox 登录页面 (Visit the Roblox login page)
    print("Logging in... ")
    browser.get("https://roblox.com/login")

    # 等待输入框加载 (Wait for the input fields to load)
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "login-username")))
    username = browser.find_element(By.ID, "login-username")
    password = browser.find_element(By.ID, "login-password")

    # 输入用户名和密码 (Enter the username and password)
    username.send_keys(putUsername)
    password.send_keys(putPassword)

    # 点击登录按钮 (Click the login button)
    loginBtn = browser.find_element(By.ID, "login-button")
    loginBtn.click()

    # 等待登录完成 (Wait for the login to complete)
    time.sleep(10)

    # 开始循环随机关注用户 (Start looping through random users to follow)
    while True:
        # 生成随机用户 ID (Generate a random user ID)
        idRandom = random.randint(1500000001, 8214240812)
        print(f"Checking user with ID: {idRandom}")

        # 访问用户页面 (Visit the user profile page)
        browser.get(f"https://roblox.com/users/{idRandom}")

        try:
            # 检测是否是 404 页面 (Check if it's a 404 page)
            error_element = WebDriverWait(browser, 3).until(
                EC.presence_of_element_located((By.XPATH, "//h3[@class='error-title']"))
            )
            if "Page cannot be found or no longer exists" in error_element.text:
                print(f"User {idRandom} does not exist (404). Skipping to next user.")
                continue
        except:
            pass  

        try:
            # 等待 "Add Friend" 按钮加载完毕 (Wait for the "Add Friend" button to load)
            WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[text()='Add Friend']"))
            )

            # 获取好友数 (Get the friend count)
            friend_count_element = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[text()='Friends']/following-sibling::a/span"))
            )

            # 提取好友数 (Extract the friend count)
            match = re.search(r"\d+", friend_count_element.text)
            friend_count = int(match.group()) if match else 0

            print(f"User {idRandom} has {friend_count} friends.")

            # 如果好友数小于 20，则跳过该用户 (If friend count is less than 20, skip the user)
            if friend_count < 20:
                print("Skipping user due to insufficient friends.")
                continue

            # 点击 "More" 按钮 (Click the "More" button)
            WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@id='popover-link']"))
            ).click()

            # 等待并点击 "Follow" 按钮 (Wait and click the "Follow" button)
            followUser = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@role='menuitem' and text()='Follow']"))
            )
            followUser.click()
            print(f"FOLLOWED user {idRandom}! Moving to next random ID...")

        except Exception as e:
            print(f"Could not process user {idRandom}. Error: {e}")

        # 等待 3 秒后执行下一个操作 (Wait for 3 seconds before performing the next action)
        time.sleep(3)

except Exception as e:
    print(f"Critical error: {e}")

finally:
    # 关闭浏览器，释放资源 (Close the browser and release resources)
    if browser:
        browser.quit()
