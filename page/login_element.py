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
    #登录校验是否登录成功
    uesr = (By.XPATH, "//*[@id='app']/div/div[2]/div/div[1]/div[3]/span/span")
    #登录异常信息
    uesr_err=(By.XPATH,"//*[@id='app']/div/section/main/div[1]/div[2]/div/div/div/form/div[6]")