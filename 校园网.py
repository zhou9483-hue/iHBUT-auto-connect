import time  # 导入time模块
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# 指定Edge WebDriver的路径
edge_driver_path = 'E:/APP/webdrive/msedgedriver.exe'  #

# 创建Edge WebDriver服务
service = Service(executable_path=edge_driver_path)

# 创建Edge浏览器实例
options = webdriver.EdgeOptions()
options.add_argument("--headless")  # 启用无头模式
#ptions.add_argument("--inprivate")  # 添加参数以启动无痕浏览模式
driver = webdriver.Edge(service=service, options=options)

# 打开网页
driver.get("http://202.114.177.246/srun_portal_pc?ac_id=1&theme=pro")

# 使用JavaScript将网页设置为全屏
driver.execute_script("document.body.requestFullscreen();")

# 创建WebDriverWait实例，用于显式等待
wait = WebDriverWait(driver, 30)  # 设置等待时间为30秒

try:
    # 等待页面加载完成
    username_input = wait.until(EC.presence_of_element_located((By.ID, "username")))
    password_input = wait.until(EC.presence_of_element_located((By.ID, "password")))

    # 输入用户名和密码
    username_input.send_keys("*")
    password_input.send_keys("*")

    # 定位登录按钮并点击
    login_button = wait.until(EC.element_to_be_clickable((By.ID, "login-account")))
    login_button.click()

    # 等待登录过程完成，这里等待10秒，根据实际情况调整
    time.sleep(10)

except TimeoutException as e:
    print("超时错误：", e)
    driver.quit()  # 退出浏览器
except Exception as e:
    print("发生错误：", e)
    driver.quit()  # 退出浏览器

finally:
    if driver is not None:

        driver.quit()  # 确保浏览器在脚本结束时关闭
