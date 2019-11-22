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
    def __init__(self):
        chrome_option = webdriver.ChromeOptions()
        # chrome_option.set_headless()
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1440, 900)

    def visit_index(self):
        self.driver.get("https://www.huxiu.com/app")
        WebDriverWait(self.driver, 10, 0.5).until(EC.element_to_be_clickable((By.XPATH, '//*[@class="js-login"]')))
        reg_element = self.driver.find_element_by_xpath('//*[@class="js-login"]')
        reg_element.click()

        WebDriverWait(self.driver, 10, 0.5).until(
            EC.element_to_be_clickable((By.XPATH, '//div[@class="gt_slider_knob gt_show"]')))

        # 进入模拟拖动流程
        self.analog_drag()

    def analog_drag(self):
        # 鼠标移动到拖动按钮，显示出拖动图片
        element = self.driver.find_element_by_xpath('//div[@class="gt_slider_knob gt_show"]')
        ActionChains(self.driver).move_to_element(element).perform()
        time.sleep(2)

        # 刷新一下极验图片
        element = self.driver.find_element_by_xpath('//a[@class="gt_refresh_button"]')
        element.click()
        time.sleep(1)

        # 获取图片地址和位置坐标列表
        cut_image_url, cut_location = self.get_image_url('//div[@class="gt_cut_bg_slice"]')
        # print(cut_image_url,cut_location)
        full_image_url, full_location = self.get_image_url('//div[@class="gt_cut_fullbg_slice"]')
        # print(full_image_url, full_location)
        # 根据坐标拼接图片
        cut_image = self.mosaic_image(cut_image_url, cut_location)
        # print(cut_image)
        full_image = self.mosaic_image(full_image_url, full_location)
        # print(full_image)
        # 保存图片方便查看
        cut_image.save("cut.jpg")
        full_image.save("full.jpg")

        # 根据两个图片计算距离
        distance = self.get_offset_distance(cut_image, full_image)
        print('两个图片计算距离=============')
        print(distance)

        # 开始移动
        self.start_move(distance)

        # 如果出现error
        try:
            WebDriverWait(self.driver, 5, 0.5).until(
                EC.element_to_be_clickable((By.XPATH, '//div[@class="gt_ajax_tip gt_error"]')))
            print("验证失败")
            return
        except TimeoutException as e:
            pass

        # 判断是否验证成功
        try:
            WebDriverWait(self.driver, 10, 0.5).until(
                EC.element_to_be_clickable((By.XPATH, '//div[@class="gt_ajax_tip gt_success"]')))
        except TimeoutException:
            print("again times")
            time.sleep(5)
            # 失败后递归执行拖动
            self.analog_drag()
        else:
            # 成功后输入手机号，发送验证码
            self.register()

    # 获取图片和位置列表
    def get_image_url(self, xpath):
        link = re.compile('background-image: url\("(.*?)"\); background-position: (.*?)px (.*?)px;')
        elements = self.driver.find_elements_by_xpath(xpath)
        image_url = None
        location = list()
        for element in elements:
            style = element.get_attribute("style")
            groups = link.search(style)
            url = groups[1]
            x_pos = groups[2]
            y_pos = groups[3]
            location.append((int(x_pos), int(y_pos)))
            image_url = url
        # print(image_url,location)
        return image_url, location

    # 拼接图片
    def mosaic_image(self, image_url, location):
        resq = requests.get(image_url)
        # print(resq)
        file = BytesIO(resq.content)
        # print(file)
        img = Image.open(file)
        image_upper_lst = []
        image_down_lst = []
        for pos in location:
            if pos[1] == 0:
                # y值==0的图片属于上半部分，高度58
                image_upper_lst.append(img.crop((abs(pos[0]), 0, abs(pos[0]) + 10, 58)))
            else:
                # y值==58的图片属于下半部分
                image_down_lst.append(img.crop((abs(pos[0]), 58, abs(pos[0]) + 10, img.height)))

        x_offset = 0
        # 创建一张画布，x_offset主要为新画布使用
        new_img = Image.new("RGB", (260, img.height))
        for img in image_upper_lst:
            new_img.paste(img, (x_offset, 58))
            x_offset += img.width

        x_offset = 0
        for img in image_down_lst:
            new_img.paste(img, (x_offset, 0))
            x_offset += img.width

        return new_img


    # 判断颜色是否相近
    def is_similar_color(self, x_pixel, y_pixel):
        for i, pixel in enumerate(x_pixel):
            if abs(y_pixel[i] - pixel) > 50:
                return False
        return True

    # 计算距离
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

    def get_track(self, distance):
        """
        根据偏移量获取移动轨迹
        :param distance: 偏移量
        :return: 移动轨迹
        """
        # 移动轨迹
        track = []
        # 当前位移
        current = 0
        # 减速阈值
        mid = distance * 4 / 5
        # 计算间隔
        t = 0.2
        # 初速度
        v = 0

        while current < distance:
            if current < mid:
                # 加速度为正2
                a = 2
            else:
                # 加速度为负3
                a = -3
            # 初速度v0
            v0 = v
            # 当前速度v = v0 + at
            v = v0 + a * t
            # 移动距离x = v0t + 1/2 * a * t^2
            move = v0 * t + 1 / 2 * a * t * t
            # 当前位移
            current += move
            # 加入轨迹
            track.append(round(move))
        return track
    # 开始移动
    def start_move(self, distance):
        element = self.driver.find_element_by_xpath('//div[@class="gt_slider_knob gt_show"]')
        print(element.size.get('width'))
        distance -= element.size.get('width') / 2
        print(distance)
        distance += 15
        print(distance)
        track = self.get_track(distance)
        print(track)
        # self.move_to_gap(element, track)
        ActionChains(self.driver).click_and_hold(element).perform()
        for x in track:
            ActionChains(self.driver).move_by_offset(xoffset=x, yoffset=0).perform()
        time.sleep(0.5)
        ActionChains(self.driver).release().perform()
        # 这里就是根据移动进行调试，计算出来的位置不是百分百正确的，加上一点偏移
        #
        #
        #
        # # 按下鼠标左键
        #
        # ActionChains(self.driver).click_and_hold(element).perform()
        # time.sleep(0.5)
        # while distance > 0:
        #     if distance > 10:
        #         # 如果距离大于10，就让他移动快一点
        #         span = random.randint(40, 43)
        #     else:
        #         # 快到缺口了，就移动慢一点
        #         span = random.randint(2, 3)
        #     ActionChains(self.driver).move_by_offset(span, 0).perform()
        #     distance -= span
        #     time.sleep(random.randint(10, 50) / 100)
        #
        # ActionChains(self.driver).move_by_offset(distance, 1).perform()
        # ActionChains(self.driver).release(on_element=element).perform()

    def register(self):
        element = self.driver.find_element_by_xpath('//input[@id="sms_username"]')
        element.clear()
        element.send_keys("手机号")

        ele_captcha = self.driver.find_element_by_xpath('//span[@class="js-btn-captcha btn-captcha"]')
        ele_captcha.click()


if __name__ == "__main__":
    h = HuXiu()
    h.visit_index()
    h.driver.quit()
