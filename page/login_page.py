from common.common_fun import *
from page.base_page import BasePage
from page.home_page import HomePage
import time


class LoginPage(BasePage):
    """
    登录页面
    """
    def login(self):
        """
        登录企业微信
        :return: 首页
        """
        # self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
        cookies = get_data("cookie.yaml")
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        time.sleep(5)
        return HomePage(self.driver)


