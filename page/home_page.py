from page.add_member_page import AddMemberPage
from page.address_book_page import AddressBookPage
from page.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    """
    首页
    """
    # _address_list = (By.XPATH, "//*[@class='frame_nav_item_title']")
    _address_list = (By.ID, "menu_contacts")
    _home = (By.ID, "menu_index")
    _add_member = (By.XPATH, "//*[@class='ww_indexImg ww_indexImg_AddMember']")

    def home_goto_add_member(self):
        """
        在首页跳转到添加成员页
        :return: 添加成员页面
        """
        while True:
            try:
                element = self.find_element(*self._add_member)
                if element.is_displayed():
                    element.click()
                    break
            except:
                pass
        return AddMemberPage(self.driver)

    def goto_address_book(self):
        """
        在首页跳转到通讯录页
        :return: 通讯录页面
        """
        self.find_element(*self._address_list).click()
        return AddressBookPage(self.driver)

    def back_home(self):
        """
        返回首页
        :return:
        """
        self.find_element(*self._home).click()

