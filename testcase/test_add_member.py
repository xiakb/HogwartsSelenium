import pytest
from page.start_page import LoginPage


class TestAddMember:
    def setup_class(self):
        self.login = LoginPage()

    def teardown_class(self):
        self.login.quit()

    def test_address_book_add_member(self):
        res = self.login.login().\
            goto_address_book().\
            goto_add_member().\
            add_member("杉杉", "shan", "15800000002").\
            get_member()
        assert "杉杉" in res

    def test_home_add_member(self):
        res = self.login.login().home_goto_add_member().add_member("木木", "mu", "15800000001").get_member()
        assert "木木" in res


