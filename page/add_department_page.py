from selenium.webdriver.common.by import By
from base_page import BasePage
import time
from department_page import DepartmentPage


class AddDepartmentPage(BasePage):
    """
    添加部门页
    """
    _department_name = (By.XPATH, "//*[@class='qui_inputText ww_inputText']")
    _confirm_button = (By.XPATH, "//*[@class='qui_btn ww_btn ww_btn_Blue']")

    def type_dep_name(self, dep_name):
        """
        输入部门名称
        :param dep_name: 需要输入的部门名称
        :return:
        """
        self.find_elements(*self._department_name)[0].send_keys(dep_name)

    def click_confirm(self):
        """
        点击确定
        :return:
        """
        self.find_element(*self._confirm_button).click()

    def add_department(self, dep_name):
        """
        添加部门信息
        :param dep_name: 需要输入的部门名称
        :return: 部门页
        """
        self.type_dep_name(dep_name)
        time.sleep(1)
        self.click_confirm()
        time.sleep(1)
        return DepartmentPage(self.driver)
