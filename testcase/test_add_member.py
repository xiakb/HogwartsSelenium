import pytest
from page.start_page import LoginPage


class TestAddMember:
    def setup_class(self):
        self.login = LoginPage()
        self.main = self.login.login()

    def teardown_class(self):
        self.main.quit()

    def teardown(self):
        self.main.back_home()

    def test_address_book_add_member(self):
        """
        通讯录页面添加成员
        :return:
        """
        res = self.main.\
            goto_address_book().\
            goto_add_member().\
            add_member("杉杉", "shan", "15800000002").\
            get_member()
        assert "杉杉" in res

    def test_home_add_member(self):
        """
        首页添加成员
        :return:
        """
        res = self.main.home_goto_add_member().add_member("木木", "mu", "15800000001").get_member()
        assert "木木" in res


