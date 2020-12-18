from common.basePage import Page
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time


class AddEmployee(Page):
    address_list = (By.XPATH, "//*[@class='frame_nav_item_title']")
    add_emp = (By.XPATH, "//*[@class='qui_btn ww_btn js_add_member']")
    username_loc = (By.ID, 'username')
    # alias = (By.ID, 'memberAdd_english_name')
    account_number = (By.ID, 'memberAdd_acctid')
    phone_number = (By.XPATH, "//*[@class='qui_inputText ww_inputText ww_telInput_mainNumber']")
    save = (By.XPATH, "//*[@class='qui_btn ww_btn js_btn_save']")
    modify_name = (By.XPATH, "//*[@class='js_mod_party_name']")

    def entrance_address_book(self):
        self.find_elements(*self.address_list)[1].click()

    def entrance_add_emp(self):
        # time.sleep(10)
        # self.find_elements(*self.add_emp)[1].click()
        while True:
            try:
                element = self.find_elements(*self.add_emp)[1]
                if element.is_displayed():
                    element.click()
                    break
            except:
                pass

    def click_save(self):
        self.find_elements(*self.save)[1].click()

    def type_username(self, username):
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)

    def type_account_number(self, account_num):
        self.find_element(*self.account_number).clear()
        self.find_element(*self.account_number).send_keys(account_num)

    def type_phone_number(self, phone):
        self.find_element(*self.phone_number).clear()
        self.find_element(*self.phone_number).send_keys(phone)

    def add_employee(self, username, account_num, phone):
        self.entrance_address_book()
        self.entrance_add_emp()
        time.sleep(1)
        self.type_username(username)
        time.sleep(1)
        self.type_account_number(account_num)
        time.sleep(1)
        self.type_phone_number(phone)
        time.sleep(1)

    def check_add_employee(self):
        try:
            self.find_element(*self.modify_name)
        except NoSuchElementException:
            return False
        else:
            return True




