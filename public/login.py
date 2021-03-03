from selenium import webdriver
from page.login_element import login_element
import time

class login_in(login_element):
    def open_browser(self):  # 定义函数并传人传人参数
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
    def login(self,gsmc,gstz,uear,pwd):
        self.driver.get('http://vmes.gdshangji.com:8010/#/login?redirect=%2Fpms%2Fshenc%2FProMaterial')
        time.sleep(20)
        self.driver.find_element(*login_element.gsdh).click()
        time.sleep(1)
        self.driver.find_element(*login_element.gsmc).send_keys(gsmc)
        time.sleep(1)
        self.driver.find_element(*login_element.gstz).send_keys(gstz)
        time.sleep(1)
        self.driver.find_element(*login_element.yhdl).click()
        time.sleep(1)
        self.driver.find_element(*login_element.zh).send_keys(uear)
        time.sleep(1)
        self.driver.find_element(*login_element.mm).send_keys(pwd)
        time.sleep(1)
        self.driver.find_element(*login_element.dl).click()