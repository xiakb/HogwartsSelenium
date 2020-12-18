class Page(object):
    def __init__(self, driver):
        """
        初始化网址与浏览器对象
        :param driver: 接收浏览器对象
        """
        self.driver = driver
        self.path = '../data/'
        self.timeout = 10

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

