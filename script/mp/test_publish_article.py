from page.mp.home_page import HomeProxy
from page.mp.login_page import LoginProxy
from utils import UtilsDriver


class TestPublishArticle:
    # 定义类级别的fixtrue初始化操作方法
    def setup_class(self):
        self.login_proxy = LoginProxy()
        self.home_proxy = HomeProxy()

    # 定义类级别的fixtrue销毁操作方法
    UtilsDriver.quit_mp_driver()

    # 定义登录的测试用例
    def test_login(self):
        self.login_proxy.login("13800138006", "123456", "")
        username = self.home_proxy.go_shop_home()
        assert "red userinfo" == username

    # 定义测试方法
    def test_publish_article(self):
        self.home_proxy.go_shop_home()
        assert is_exist(UtilsDriver.get_mp_driver(), "购物车")
