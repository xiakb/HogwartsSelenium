import yaml
from selenium import webdriver


def get_cookie():
    """
    复用浏览器，获取cookie
    :return: 获取的cookie数据
    """
    opt = webdriver.ChromeOptions()
    # 设置debug地址
    opt.debugger_address = "127.0.0.1:9222"
    driver = webdriver.Chrome(options=opt)
    driver.implicitly_wait(5)
    driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
    cookie = driver.get_cookies()
    return cookie


def write_data(filename, data):
    """
    将指定的数据写入yaml文件中
    :param filename: 要写入的yaml文件
    :param data: 需要写入的数据
    :return:
    """
    path = '../data/' + filename
    print(path)
    with open(path, "w", encoding="UTF-8") as file:
        yaml.dump(data, file)


def get_data(filename):
    file_path = '../data/' + filename
    with open(file_path) as file:
        data = file.read()
        result = yaml.safe_load(data)
    return result



