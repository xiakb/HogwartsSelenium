import pytest
from page.start_page import LoginPage
from common.common_fun import *


class TestAddMember:
    def setup_class(self):
        self.login = LoginPage()
        self.main = self.login.login()

    def teardown_class(self):
        self.main.quit()

    def teardown(self):
        self.main.back_home()

    @pytest.mark.parametrize(
        "name, id, phone",
        get_data("member.yaml")["member_address_list"],
        ids=get_data("member.yaml")["address_list_case"]
    )
    def test_address_book_add_member(self, name, id, phone):
        """
        通讯录页面添加成员
        :return:
        """
        res = self.main.\
            goto_address_list().\
            goto_add_member().\
            add_member(name, id, phone).\
            get_member()
        assert name in res

    @pytest.mark.parametrize(
        "name, id, phone",
        get_data("member.yaml")["member_address_list"],
        ids=get_data("member.yaml")["address_list_case"]
    )
    def test_home_add_member(self, name, id, phone):
        """
        首页添加成员
        :return:
        """
        res = self.main.home_goto_add_member().add_member(name, id, phone).get_member()
        assert name in res


