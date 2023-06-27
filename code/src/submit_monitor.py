# -*- coding: utf-8 -*-
# 小红书上传对应的图片到 平台上
import threading

from future.backports.datetime import time
from selenium.webdriver.support.wait import WebDriverWait
import time

from twisted.conch.insults.insults import privateModes

from code.src.utils.constants import OUTPUT_DIR
from code.src.utils.getObjectUtils import getObjectUtils
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class submit_monitor:
    objectUtils = getObjectUtils()
    # 测试完成
    def convertMode(self, driver):
        wait = WebDriverWait(driver, 100)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='publish-video']")))
        element = wait.until(EC.visibility_of_element_located(('xpath','//span[@class="title"][text()="上传图文"]')))
        change_click = driver.find_elements('xpath','//span[@class="title"][text()="上传图文"]')
        change_click[0].click()
        print("已切换上传模式为图文模式")


    # 负责主要的上传工作
    def submit_picture(self, driver, img_path, top, bot):
        picturePaths = self.objectUtils.getFileList(img_path)
        if len(picturePaths) == 0:
            print(img_path + "路径下无文件")
            return -1

        input_buttons = driver.find_elements('xpath','//*[@id="publisher-dom"]/div/div[1]/div/div[1]/div[2]/div[1]/div/input')
        input_buttons[0].send_keys(picturePaths[0])
        time.sleep(10)
        dex = len(picturePaths)
        if (bot < dex):
            dex = bot

        for i in range(top,dex):
            input_buttons[0].send_keys(picturePaths[i])
            time.sleep(5)
        time.sleep(60)
        print("文件已上传")

    # 在提交前设置一些必要的信息
    def setUpInformationBeforeSubmit(self, driver):
        print("测试 向标题写入内容")
        title_input = driver.find_elements('xpath','//*[@id="publisher-dom"]/div/div[1]/div/div[2]/div[2]/div[2]/input')
        title_input[0].send_keys("AI 作画 test")
        desc_input = driver.find_elements('xpath', '//*[@id="post-textarea"]')
        desc_input[0].send_keys("AI 作画 内容")
        # timing_input = driver.find_elements('xpath', '//*[@id="publisher-dom"]/div/div[1]/div/div[2]/div[2]/div[6]/div[5]/div[2]/label[2]/div[1]')
        # timing_input[0].click()



    def submit_button(self, driver):
        ele = driver.find_elements('xpath','//*[@id="publisher-dom"]/div/div[1]/div/div[2]/div[2]/div[7]/button[1]')
        driver.maximize_window()
        time.sleep(20)
        ele[0].click()
        print("=========== 完成任务 ===============")



    def start(self, top, bot):
        objectUtils = getObjectUtils()
        driver = objectUtils.getDriverWithLoginCookie(name="xiaoXiongMao")
        # 已经获取指定的driver
        print("已经获取指定的driver，并尝试使用cookie连接新的网页")
        driver.get("https://creator.xiaohongshu.com/publish/publish?source=official")
        # # tmp
        time.sleep(10)
        print("开始转换网页")
        self.convertMode(driver)
        self.submit_picture(driver, output_dir, top, bot)
        # 调整对应的发布状态
        self.setUpInformationBeforeSubmit(driver)
        self.submit_button(driver)

if __name__ == '__main__':
    # output_dir = OUTPUT_DIR
    output_dir = 'D:\Desktop\workRelated\chatgpt\pythonProject1\code\data\img\\2023_6_16_21'
    threads = []
    start_time = time.time()
    # 使用多线程
    sm = submit_monitor()
    for i in range(10):
        t = threading.Thread(target=sm.start,args=(i*10, (i+1)*10))
        threads.append(t)
        t.start()

    # 等待所有线程执行完毕
    for t in threads:
        t.join()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("运行时间为：", elapsed_time, "秒")