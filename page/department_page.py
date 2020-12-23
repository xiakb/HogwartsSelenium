from selenium.webdriver.common.by import By
from base_page import BasePage


class DepartmentPage(BasePage):
    """
    部门信息页
    """
    _address_list = (By.ID, "menu_contacts")

    def dep_goto_address_list(self):
        """
        在首页跳转到通讯录页
        :return: 通讯录页面
        """
        from address_list_page import AddressListPage
        self.find_element(*self._address_list).click()
        return AddressListPage(self.driver)


