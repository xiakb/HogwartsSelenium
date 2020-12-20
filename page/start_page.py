from page.base_page import BasePage
from page.login_page import LoginPage
from selenium.webdriver.common.by import By
from page.registration_page import RegistrationPage


class StartPage(BasePage):
    """
    企业微信官网页面
    """
    _enterprise_login = (By.XPATH, "//*[@class='index_top_operation_loginBtn']")
    _registered = (By.XPATH, "//*[@class='index_head_info_pCDownloadBtn']")

    def goto_login_page(self):
        """
        跳转到登录页面
        :return: 登录页面
        """
        self.find_element(*self._enterprise_login).click()
        return LoginPage(self.driver)

    def goto_registration_page(self):
        """
        跳转到注册页面
        :return: 注册页面
        """
        self.find_element(*self._registered).click()
        return RegistrationPage(self.driver)
