from home_page import HomePage
from login_page import LoginPage


class TestAddDepartment:
    def setup_class(self):
        self.login = LoginPage()
        self.main = self.login.login()

    def teardown_class(self):
        self.main.quit()

    def teardown(self):
        self.main.back_home()

    def test_add_department(self):
        """
        添加部门
        :return:
        """
        dep = self.main.\
            goto_address_book().\
            goto_add_department().\
            add_department("人事部").\
            dep_goto_address_book().\
            get_department()
        assert "人事部" in dep
