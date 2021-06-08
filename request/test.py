from selenium import webdriver
import datetime
import time
f = open("/root/python/request/log.txt", "a+")
options = webdriver.FirefoxOptions()
options.add_argument('--headless')
wd = webdriver.Firefox(
    executable_path="/root/python/geckodriver", options=options)
wd.get('https://stuhealth.jnu.edu.cn/#/login')
f.write(datetime.datetime.now()+"成功运行\n")

element = wd.find_element_by_id("zh")
element.clear()
time.sleep(1)
element.send_keys('2018053307')
time.sleep(1)

element = wd.find_element_by_id("passw")
element.clear()
time.sleep(1)
element.send_keys('JUST1990s')
time.sleep(1)

wd.find_element_by_xpath(
    "/html/body/app-root/app-login/div[2]/div[2]/form/div[4]/div/button").click()
wd.quit()
f.write(datetime.datetime.now()+"运行完成\n")
f.close()
