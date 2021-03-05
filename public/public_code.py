from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from page.login_element import login_element
import time



class public(login_element):
    dr = webdriver.Chrome()  # 定义全局的dr，不在setUp函数里，实现了只启动一次firefox
    def open_browser(self,driver=dr):#初始化数据中，将全局变量dr赋值给self.driver,这样每次测试开始都只会锁定dr，而不是新创建一个
        self.driver=driver
        self.driver.maximize_window()
        self.driver.get('http://vmes.gdshangji.com:8010/#/login?redirect=%2Fpms%2Fshenc%2FProMaterial')
        time.sleep(10)
    def location_element(seif, args):
        try:
            return WebDriverWait(seif.driver, 10).until(lambda x:x.find_element(*args))
        except Exception:
            print("元素定位失败：通过" + args[0] + "定位元素是:" + args[1])

    def browser_quit(self):#最后一个测试用例，实现了只进行一次退出浏览器
        self.driver.quit()
