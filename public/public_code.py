from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from page.login_element import login_element
import time



class public(login_element):

    def open_browser(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://vmes.gdshangji.com:8010/#/login?redirect=%2Fpms%2Fshenc%2FProMaterial')
        time.sleep(10)
    def location_element(seif, args):
        try:
            return WebDriverWait(seif.driver, 10).until(lambda x:x.find_element(*args))
        except Exception:
            print("元素定位失败：通过" + args[0] + "定位元素是:" + args[1])
