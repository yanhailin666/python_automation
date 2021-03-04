from page.login_element import login_element
from public.public_code import public
import time,unittest


class login_in(public):
    def login(self,gsmc,gstz,uear,pwd):
        self.open_browser()
        self.driver.implicitly_wait(10)
        self.location_element(login_element.gsdh).click()
        time.sleep(1)
        self.location_element(login_element.gsmc).send_keys(gsmc)
        time.sleep(1)
        self.location_element(login_element.gstz).send_keys(gstz)
        time.sleep(1)
        self.location_element(login_element.yhdl).click()
        time.sleep(1)
        self.location_element(login_element.zh).send_keys(uear)
        time.sleep(1)
        self.location_element(login_element.mm).send_keys(pwd)
        time.sleep(1)
        self.location_element(login_element.dl).click()














# from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
# from page.login_element import login_element
# import time,unittest
#
#
#
# class login_in(login_element):
#
#     def open_browser(self):
#         self.driver = webdriver.Chrome()
#         self.driver.maximize_window()
#         self.driver.get('http://vmes.gdshangji.com:8010/#/login?redirect=%2Fpms%2Fshenc%2FProMaterial')
#         time.sleep(10)
#     def location_element(seif, args):
#         try:
#             return WebDriverWait(seif.driver, 10).until(lambda x:x.find_element(*args))
#         except Exception:
#             print("元素定位失败：通过" + args[0] + "定位元素是:" + args[1])
#     def login(self,gsmc,gstz,uear,pwd):
#         self.driver.implicitly_wait(10)
#         self.location_element(login_element.gsdh).click()
#         time.sleep(1)
#         self.location_element(login_element.gsmc).send_keys(gsmc)
#         time.sleep(1)
#         self.location_element(login_element.gstz).send_keys(gstz)
#         time.sleep(1)
#         self.location_element(login_element.yhdl).click()
#         time.sleep(1)
#         self.location_element(login_element.zh).send_keys(uear)
#         time.sleep(1)
#         self.location_element(login_element.mm).send_keys(pwd)
#         time.sleep(1)
#         self.location_element(login_element.dl).click()
