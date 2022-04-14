# 自媒体平台的登录页面对象
import time

from selenium.webdriver.common.by import By

from base.mp.base import BasePage, BaseHandle


# 定义对象库层
class LoginPage(BasePage):
    def __init__(self):
        super().__init__()
        # 手机号码输入框
        self.mobile = By.XPATH, '//*[@placeholder="手机号/邮箱"]'
        # 密码输入框
        self.password = By.XPATH, '//*[@placeholder="密码"]'
        # 验证码输入框
        self.code = By.XPATH, '//*[@placeholder="验证码"]'
        # 登录按钮
        self.login_btn = By.XPATH, '//*[@class="J-login-submit"]'

    # 定位手机号码输入框
    def find_mobile(self):
        return self.get_element(self.mobile)

    # 定位密码输入框
    def find_password(self):
        return self.get_element(self.password)

    # 定位验证码输入框
    def find_code(self):
        return self.get_element(self.code)

    # 定位登录按钮
    def find_login_btn(self):
        return self.get_element(self.login_btn)


# 定义操作层
class LoginHandle(BaseHandle):
    def __init__(self):
        self.login_page = LoginPage()

    # 输入手机号码
    def input_mobile(self, mobile):
        self.input_text(self.login_page.find_mobile(), mobile)

    # 输入密码
    def input_password(self, password):
        self.input_text(self.login_page.find_password(), password)

    # 输入验证码
    def input_code(self, code):
        self.input_text(self.login_page.find_code(), code)

    # 点击登录按钮
    def click_login_btn(self):
        self.login_page.find_login_btn().click()

# 定义业务层
class LoginProxy:
    def __init__(self):
        self.login_handle = LoginHandle()

    # 登录业务
    def login(self, mobile, password, code):
        self.login_handle.input_mobile(mobile)  # 输入用户名
        self.login_handle.input_password(password)  # 输入密码
        time.sleep(20)
        self.login_handle.input_code(code)  # 输入验证码
        self.login_handle.click_login_btn()  # 点击登录按钮


