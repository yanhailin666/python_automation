from selenium.webdriver.common.by import By

class login_element:
    #点击公司代号
    gsdh=(By.XPATH,"//*[@class='copyLogian']")
    #请输入公司名称
    gsmc=(By.XPATH,"//*[@class='el-input__inner'and @placeholder='请输入公司名称']")
    #输入公司代号
    gstz=(By.XPATH,"//*[@class='el-input__inner'and @placeholder='请输入公司代号']")
    #点击用户登录
    yhdl=(By.XPATH,"//*[@class='userLogian']")
    # 输入账号
    zh=(By.XPATH,"//*[@class='el-input__inner'and @placeholder='请输入账号']")
    # 输入密码
    mm = (By.XPATH,"//*[@class='el-input__inner'and @placeholder='请输入密码']")
    #点击立即登录
    dl = (By.XPATH, "//*[@class='el-button pan-btn green-btn el-button--primary el-button--medium']")