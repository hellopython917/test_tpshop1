# 自媒体平台的首页页面对象
from selenium.webdriver.common.by import By

from base.mp.base import BasePage, BaseHandle


# 定义对象库层
class HomePage(BasePage):
    def __init__(self):
        super().__init__()

        # 返回商城首页
        self.shop_home_page = By.XPATH, " //*[@class='home']"
        # 定位苹果钢化膜
        self.apple = By.XPATH, "//div[text()='苹果7钢化膜iphone8plus手机7plus全屏全覆盖8贴膜水凝7p抗蓝光3D']"

    # 定位返回商城首页
    def find_shop_home_page(self):
        return self.get_element(self.shop_home_page)

    # 定位苹果钢化膜
    def find_apple(self):
        return self.get_element(self.apple)


# 定义操作层
class HomeHandle(BaseHandle):
    def __init__(self):
        self.home_page = HomePage()

    # 获取返回商城首页信息
    def click_shop_home(self):
        self.home_page.find_shop_home_page().click()

    # 获取定位苹果钢化膜
    def click_apple(self):
        self.home_page.find_apple().click()

# 定义业务层
class HomeProxy:
    def __init__(self):
        self.home_handle = HomeHandle()

    # 跳转到首页
    def go_shop_home(self):
        self.home_handle.click_shop_home()
        self.home_handle.click_apple()
