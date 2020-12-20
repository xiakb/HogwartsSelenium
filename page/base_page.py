from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    def __init__(self, driver=None):
        """
        初始化网址与浏览器对象
        :param driver: 接收浏览器对象
        """
        driver: WebDriver  # 不是赋值操作，用作ide的类型提示
        if driver is None:
            self.driver = webdriver.Chrome()
            self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
        else:
            self.driver = driver
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def find_element(self, *loc):
        """
        find_element定位器
        :param loc: 接收可变参数
        :return: 返回find_element定位器
        """
        return self.driver.find_element(*loc)

    def find_elements(self, *loc):
        """
        find_elements定位器
        :param loc: 接收可变参数
        :return: 返回find_elements定位器
        """
        return self.driver.find_elements(*loc)

    def wait_click(self, locator):
        """
        显示D等待
        :param locator: 需要等待的元素
        :return:
        """
        return WebDriverWait(self.driver, 9).until(expected_conditions.element_to_be_clickable(locator))

    def quit(self):
        """
        退出浏览器
        :return:
        """
        return self.driver.quit()

