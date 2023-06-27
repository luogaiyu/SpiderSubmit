# -*- coding: utf-8 -*-
# 获取不同的对象
import os
import time

from selenium import webdriver
import logging

from code.src.utils.constants import LOGIN_COOKIES_little_pandas, LOGIN_COOKIES_shuqian


class getObjectUtils:
    # 获取普通驱动
    def getPureDriver(self):
        # 创建 ChromeDriver 实例
        driver = webdriver.Chrome(executable_path=r"D:\software\chrome_driver\chromedriver.exe")
        return driver

    # 获取带着 login cookie的driver, 通过账号名称获取对应的cookie
    def getDriverWithLoginCookie(self, name):
        driver = webdriver.Chrome(executable_path=r"D:\software\chrome_driver\chromedriver.exe")
        driver.get("https://creator.xiaohongshu.com/publish/publish?source=official")
        if (name =='shuQian'):
            LOGIN_COOKIES = LOGIN_COOKIES_shuqian
        elif(name == 'xiaoXiongMao'):
            LOGIN_COOKIES = LOGIN_COOKIES_little_pandas
        for cookie in LOGIN_COOKIES:
            driver.add_cookie(cookie_dict = cookie)
        return driver


    # 获取日志生成器
    def getLogger(self):
        format = '%(levelname)s - %(asctime)s - %(message)s '
        # 添加控制台
        logger = logging.getLogger('spider')
        ch = logging.StreamHandler()
        file_handler = logging.FileHandler('my_log.txt')
        file_handler.setFormatter(logging.Formatter(format))
        file_handler.setLevel("DEBUG")
        logger.addHandler(file_handler)
        return logger

    def getFileList(self, path):
        files = os.listdir(path)
        result_path_list = []
        for file in files:
            result_path_list.append(path + '\\' + file)
        return result_path_list

if __name__ == '__main__':
    pass


