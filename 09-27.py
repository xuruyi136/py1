import random
import time, re
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
import requests
from io import BytesIO

class HuXiu(object):
    # def __init__(self):
    #     chrome_option = webdriver.ChromeOptions()
    #     # chrome_option.set_headless()
    #
    #     self.driver = webdriver.Chrome()
    #     self.driver.set_window_size(1440, 900)
    # def visit_index(self):
    #     self.driver.get("https://www.huxiu.com/app")
    #     WebDriverWait(self.driver, 10, 0.5).until(EC.element_to_be_clickable((By.XPATH, '//*[@class="js-js-login"]')))
    #     reg_element = self.driver.find_element_by_xpath('//*[@class="js-login"]')
    #     reg_element.click()
    #     time.sleep(5)
    #     self.driver.quit()

    def get_offset_distance(self, cut_image, full_image):
        for x in range(cut_image.width):
            for y in range(cut_image.height):
                cpx = cut_image.getpixel((x, y))
                fpx = full_image.getpixel((x, y))
                if not self.is_similar_color(cpx, fpx):
                    img = cut_image.crop((x, y, x + 50, y + 40))
                    # 保存一下计算出来位置图片，看看是不是缺口部分
                    img.save("1.jpg")
                    return x
        print(x)
    def is_similar_color(self, x_pixel, y_pixel):
        for i, pixel in enumerate(x_pixel):
            if abs(y_pixel[i] - pixel) > 50:
                return False
        return True
if __name__ == '__main__':
    Hx=HuXiu()
    cut_image=Image.open('cut.jpg','w')
    full_image=Image.open('full.jpg', 'r')
    Hx.get_offset_distance(cut_image,full_image)