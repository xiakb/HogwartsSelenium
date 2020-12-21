from page.base_page import BasePage
from add_department_page import AddDepartmentPage
from selenium.webdriver.common.by import By
import time


class AddressBookPage(BasePage):
    """
    通讯录页面
    """
    _add_emp = (By.XPATH, "//*[@class='qui_btn ww_btn js_add_member']")
    _add_dep = (By.XPATH, "//*[@class='js_add_sub_party']")
    _member_list = (By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
    # _party_name = (By.ID, "department_name")
    _party_name = (By.XPATH, "//*[@class='jstree-anchor']")

    def goto_add_member(self):
        """
        在通讯录页面跳转到添加成员页面
        :return: 添加成员页面
        """
        from page.add_member_page import AddMemberPage
        # time.sleep(10)
        # self.find_elements(*self._add_emp)[1].click()
        while True:
            try:
                element = self.find_elements(*self._add_emp)[2]
                if element.is_displayed():
                    element.click()
                    break
            except:
                pass
        return AddMemberPage(self.driver)

    def get_member(self):
        """
        获取成员列表，用来做断言信息
        :return: 成员列表
        """
        member_list = self.find_elements(*self._member_list)
        member_list_res = [i.text for i in member_list]
        return member_list_res

    def goto_add_department(self):
        """
        跳转到新建部门页面
        :return: 新建部门页
        """
        self.wait_click(self._add_dep)
        self.find_element(*self._add_dep).click()
        return AddDepartmentPage(self.driver)

    def get_department(self):
        """
        获取部门名称
        :return: text文本信息
        """
        time.sleep(1)
        party_name_list = self.find_elements(*self._party_name)
        party_name = [i.text for i in party_name_list]
        return party_name


