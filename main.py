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

# 启动 Firefox 浏览器
print("Ok. Starting Firefox ")
firefox_options = Options()
browser = webdriver.Firefox(options=firefox_options)  

try:
    # 访问 Roblox 登录页面
    print("Logging in... ")
    browser.get("https://roblox.com/login")

    # 等待用户名输入框加载，并输入信息
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "login-username"))).send_keys(putUsername)
    browser.find_element(By.ID, "login-password").send_keys(putPassword)
    browser.find_element(By.ID, "login-button").click()

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
                EC.presence_of_element_located((By.XPATH, "//h3[contains(text(), 'Page cannot be found')]"))
            )
            print(f"User {idRandom} does not exist. Skipping.")
            continue
        except:
            pass  # 没有找到 404 提示，说明用户页面存在

        try:
            # **等待 "Add Friend" 按钮加载**，确保页面已完全加载
            add_friend_button = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.ID, "friend-button"))
            )

            # **获取好友数**
            friend_count_element = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/friends')]/span/b"))
            )
            friend_count = int(re.search(r"\d+", friend_count_element.text).group())

            print(f"User {idRandom} has {friend_count} friends.")

            # **如果好友数小于 20，则跳过该用户**
            if friend_count < 20:
                print("Skipping user due to insufficient friends.")
                continue
        
        except Exception as e:
            print(f"Error fetching friend count for user {idRandom}: {e}")
            continue

        try:
            # **点击 "More" 按钮**
            more_button = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-label, 'See More')]"))
            )
            more_button.click()

            # **等待并点击 "Follow" 按钮**
            followUser = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.ID, "follow-button"))
            )
            followUser.click()
            print(f"FOLLOWED user {idRandom}!")

        except Exception as e:
            print(f"Could not follow user {idRandom}. Error: {e}")

        # 等待 3 秒后执行下一个用户
        time.sleep(3)

except Exception as e:
    print(f"Critical error: {e}")

finally:
    # 关闭浏览器
    browser.quit()
