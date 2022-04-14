# 定义工具类
from selenium import webdriver


class UtilsDriver:
    _mp_driver = None  # 表示的是自媒体平台的浏览器驱动
    _mis_driver = None  # 表示的是后台管理的浏览器驱动
    _app_driver = None  # 表示的是app的浏览器驱动

    # 定义获取自媒体平台的浏览器驱动
    @classmethod
    def get_mp_driver(cls):
        if cls._mp_driver is None:
            cls._mp_driver = webdriver.Chrome()
            cls._mp_driver.maximize_window()
            cls._mp_driver.get("http://tp.shop.com/Home/user/login.html")
        return cls._mp_driver

    # 定义退出自媒体平台的浏览器驱动
    @classmethod
    def quit_mp_driver(cls):
        if cls._mp_driver is not None:
            cls.get_mp_driver().quit()
            cls._mp_driver = None

    # 定义获取后台管理系统的浏览器驱动
    @classmethod
    def get_mis_driver(cls):
        if cls._mis_driver is None:
            cls._mis_driver = webdriver.Chrome()
            cls._mis_driver.maximize_window()
            cls._mis_driver.get("http://tp.shop.com/index.php/Admin/Admin/login")
        return cls._mis_driver

    # 定义退出自媒体平台的浏览器驱动
    @classmethod
    def quit_mis_driver(cls):
        if cls._mis_driver is not None:
            cls.get_mis_driver().quit()
            cls._mis_driver = None