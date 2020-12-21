from selenium.webdriver.common.by import By
from common.common_fun import *
from page.base_page import BasePage
from page.home_page import HomePage
import time
from registration_page import RegistrationPage


class LoginPage(BasePage):
    """
    登录页面
    """
    _enterprise_register = (By.XPATH, "//*[@class='login_registerBar_link']")

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

    def goto_registration_page(self):
        """
        跳转到注册页面
        :return: 注册页面
        """
        self.find_element(*self._enterprise_register).click()
        return RegistrationPage(self.driver)



