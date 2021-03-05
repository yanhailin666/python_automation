from page.login_element import login_element
from public.public_code import public
import time,unittest


class login_in(public):
    def login(self,gsmc,gstz,uear,pwd):
        self.open_browser()
        self.driver.implicitly_wait(10)
        self.location_element(login_element.gsdh).click()
        self.location_element(login_element.gsmc).send_keys(gsmc)
        self.location_element(login_element.gstz).send_keys(gstz)
        self.location_element(login_element.yhdl).click()
        self.location_element(login_element.zh).send_keys(uear)
        self.location_element(login_element.mm).send_keys(pwd)
        try:
            self.location_element(login_element.dl).click()
            time.sleep(3)
            dl_uear=self.location_element(login_element.uesr)
            print("登录账号："+dl_uear.text)
        except:
            time.sleep(3)
            er_code=self.location_element(login_element.uesr_err)
            print("错误信息："+er_code.text)
        self.browser_quit()
