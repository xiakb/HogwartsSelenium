import pytest
from common.common_fun import *
from login_page import LoginPage


class TestAddDepartment:
    def setup_class(self):
        self.login = LoginPage()
        self.main = self.login.login()

    def teardown_class(self):
        self.main.quit()

    def teardown(self):
        self.main.back_home()

    @pytest.mark.parametrize(
        "dep",
        get_data("department.yaml")["dep_name"],
        ids=get_data("department.yaml")["case_name"]
    )
    def test_add_department(self, dep):
        """
        添加部门
        :return:
        """
        deps = self.main.\
            goto_address_list().\
            goto_add_department().\
            add_department(dep).\
            dep_goto_address_list().\
            get_department()
        assert dep in deps
