from page.address_book_page import AddressBookPage
from page.base_page import BasePage
from selenium.webdriver.common.by import By
import time


class AddMemberPage(BasePage):
    """
    添加成员页
    """
    _username_loc = (By.ID, 'username')
    # alias = (By.ID, 'memberAdd_english_name')
    _account_number = (By.ID, 'memberAdd_acctid')
    _phone_number = (By.XPATH, "//*[@class='qui_inputText ww_inputText ww_telInput_mainNumber']")
    _save = (By.XPATH, "//*[@class='qui_btn ww_btn js_btn_save']")

    def click_save(self):
        """
        点击保存
        :return:
        """
        self.find_elements(*self._save)[1].click()

    def type_username(self, username):
        """
        输入姓名
        :param username: 需要输入的姓名
        :return:
        """
        self.find_element(*self._username_loc).clear()
        self.find_element(*self._username_loc).send_keys(username)

    def type_account_number(self, account_num):
        """
        输入账号
        :param account_num: 需要输入的账号
        :return:
        """
        self.find_element(*self._account_number).clear()
        self.find_element(*self._account_number).send_keys(account_num)

    def type_phone_number(self, phone):
        """
        输入手机号
        :param phone: 需要输入的手机号
        :return:
        """
        self.find_element(*self._phone_number).clear()
        self.find_element(*self._phone_number).send_keys(phone)

    def add_member(self, username, account_num, phone):
        """
        添加成员信息
        :param username: 需要输入的姓名
        :param account_num: 需要输入的账号
        :param phone: 需要输入的手机号
        :return: 通讯录页面
        """
        self.type_username(username)
        time.sleep(1)
        self.type_account_number(account_num)
        time.sleep(1)
        self.type_phone_number(phone)
        time.sleep(1)
        self.click_save()
        time.sleep(1)
        return AddressBookPage(self.driver)





