# 爬取对应的数据
import json
import threading
import time
import os
from code.src.utils.constants import OUTPUT_DIR, HEADERS
from code.src.utils.getObjectUtils import getObjectUtils
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.request

# https://www.midjourney.com/showcase/recent/
class spider_midjourney:
    objectUtils = getObjectUtils()
    def parse(self, driver):
        # 打开目标网页
        driver.get('https://www.midjourney.com/showcase/recent/')
        # 设置最长等待时间为10秒
        wait = WebDriverWait(driver, 100)
        # 等待元素出现并变为可见状态
        # element = wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@role="gridcell"]//div[@class="relative col-span-1 row-span-1"]/span/img')))
        # driver.implicitly_wait(30)
        time.sleep(120)
        # 获取所有图片元素和描述信息元素
        imgs = driver.find_elements("xpath",'//div[@role="gridcell"]//div[@class="relative col-span-1 row-span-1"]/span/img')

        # # # 遍历图片元素和描述信息元素，并下载图片到本地
        if (not os.path.exists(output_dir)):
            os.mkdir(output_dir)
        return imgs


    def add_suffix(self, save_path, suffix_str):
        return save_path + "." + suffix_str


    def save_files(self, imgs, top, bot):
        desc_save =[]
        logger = self.objectUtils.getLogger()
        for i, img in enumerate(imgs):
            if(i >= top and i < bot):
                url = img.get_property("src")
                desc = img.get_property("alt")
                suffix = url.split(".")[-1]
                print(str(i) + " %% " + url + " %% " + desc + "\n")
                print("========================================= \n")
                req = urllib.request.Request(url, headers=HEADERS)
                try:
                    response = urllib.request.urlopen(req)
                except Exception as e:
                    logger.error("error index : " + str(i))
                    logger.error(str(e))
                    logger.error("==============================================================================")
                    continue
                data = response.read()
                # 这个逻辑需要改,把文件名改掉
                desc_save.append({str(i) : desc})
                final_name = self.add_suffix(output_dir + str(i), suffix)
                if (not os.path.exists(final_name)):
                    try:
                        with open(final_name, 'wb') as f:
                            f.write(data)
                    except Exception as e:
                        logger.error("error index : " + str(i))
                        logger.error(str(e))
                        logger.error("==============================================================================")
                        continue
                    print("=== done ======")
                else:
                    print("=== skip =======")
                time.sleep(3)
        with open(OUTPUT_DIR + str(top) + "-" + str(bot) + ".json", "w+") as f:
            json.dump(desc_save, f)


    def start(self, top, bot):
        # 创建 ChromeDriver 实例
        driver = self.objectUtils.getPureDriver()
        imgs = self.parse(driver)
        self.save_files(imgs, top, bot)
        driver.quit()


if __name__ == '__main__':
    sm = spider_midjourney()
    # 后期需要改成多线程
    # 首先需要将爬虫
    output_dir = OUTPUT_DIR
    threads = []
    start_time = time.time()
    # 使用多线程
    for i in range(10):
        t = threading.Thread(target=start,args=(i*10, (i+1)*10))
        threads.append(t)
        t.start()

    # 等待所有线程执行完毕
    for t in threads:
        t.join()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("运行时间为：", elapsed_time, "秒")