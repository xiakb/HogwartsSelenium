from common.common_fun import *
from common.basePage import Page


class LoginPage(Page):
    def login(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
        cookies = get_data("cookie.yaml")
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")


