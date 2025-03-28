from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import re  
from selenium.webdriver.firefox.options import Options  

# 固定用户名和密码
putUsername = "typeyourusernamehere"
putPassword = "typeyourpasswordhere"

# 默认使用 Firefox 浏览器（无代理）
print("Ok. Starting Firefox ")
firefox_options = Options()

# 启动浏览器
browser = webdriver.Firefox(options=firefox_options)  

try:
    # 访问 Roblox 登录页面
    print("Logging in... ")
    browser.get("https://roblox.com/login")

    # 等待输入框加载
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "login-username")))
    username = browser.find_element(By.ID, "login-username")
    password = browser.find_element(By.ID, "login-password")

    # 输入用户名和密码
    username.send_keys(putUsername)
    password.send_keys(putPassword)

    # 点击登录按钮
    loginBtn = browser.find_element(By.ID, "login-button")
    loginBtn.click()

    # 等待登录完成
    time.sleep(10)

    # 开始循环随机关注用户
    while True:
        # 生成随机用户 ID
        idRandom = random.randint(1500000001, 8214240812)
        print(f"Checking user with ID: {idRandom}")

        # 访问用户页面
        browser.get(f"https://roblox.com/users/{idRandom}")

        try:
            # 检测是否是 404 页面
            error_element = WebDriverWait(browser, 3).until(
                EC.presence_of_element_located((By.XPATH, "//h3[@class='error-title']"))
            )
            if "Page cannot be found or no longer exists" in error_element.text:
                print(f"User {idRandom} does not exist (404). Skipping to next user.")
                continue
        except:
            pass  

        try:
            # 等待好友数元素加载完毕
            friend_count_element = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a[title*='Friends'] b"))
            )

            # 获取文本
            friend_count_text = friend_count_element.text.strip()

            # 提取好友数
            match = re.search(r"\d+", friend_count_text)
            friend_count = int(match.group()) if match else 0

            print(f"User {idRandom} has {friend_count} friends.")

            # 如果好友数小于 20，则跳过该用户
            if friend_count < 20:
                print("Skipping user due to insufficient friends.")
                continue
        
        except Exception as e:
            print(f"Error fetching friend count for user {idRandom}: {e}")
            continue

        try:
            # 点击 "More" 按钮
            WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@id='popover-link']"))
            ).click()

            # 等待并点击 "Follow" 按钮
            followUser = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.ID, "follow-button"))
            )
            followUser.click()
            print(f"FOLLOWED user {idRandom}! Moving to next random ID...")

        except Exception as e:
            print(f"Could not process user {idRandom}. Error: {e}")

        # 等待 3 秒后执行下一个操作
        time.sleep(3)

except Exception as e:
    print(f"Critical error: {e}")

finally:
    # 关闭浏览器，释放资源
    if browser:
        browser.quit()
