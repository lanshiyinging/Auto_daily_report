import time

from pip._vendor.distlib.compat import raw_input
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import sys
import os

'''
chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options)
'''

#user_name = 'xxx'       #your username
#password = 'xxx'        #your password

user_name = sys.argv[1]
password = sys.argv[2]
try:
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get("https://ids.xmu.edu.cn/authserver/login?service=https://xmuxg.xmu.edu.cn/login/cas/xmu")
    time.sleep(1)

    user_name = driver.find_element_by_xpath("//input[@id='username']").send_keys(user_name)
    user_password = driver.find_element_by_xpath("//input[@id='password']").send_keys(password)
    login = driver.find_element_by_xpath("//button[@type='submit']").click()
    time.sleep(10)

    driver.get_screenshot_as_file("screen.png")

    daily_report_app = driver.find_element_by_xpath('//*[@id="mainPage-page"]/div[1]/div[3]/div[2]/div[2]/div[3]/div/div[1]/div[2]').click()
    time.sleep(10)

    handles = driver.window_handles
    driver.switch_to.window(handles[-1])

    my_form = driver.find_element_by_xpath('//div[@title="我的表单"]').click()
    time.sleep(1)

    select = driver.find_element_by_xpath('//*[@id="select_1582538939790"]/div/div').click()
    yes = driver.find_element_by_xpath("/html/body/div[8]/ul/div/div[3]/li/label").click()
    time.sleep(2)

    save = driver.find_element_by_xpath('//*[@id="mainM"]/div/div/div/div[2]/div[1]/div/div/span/span').click()
    time.sleep(1)
    confirm = driver.switch_to.alert
    confirm.accept()
    time.sleep(5)
    pagesource = driver.page_source
    if "修改了表单" in pagesource:
        print("Success")
        driver.quit()
        os._exit(0)
    else:
        os._exit(1)
    #with open('source.txt', 'w') as f:
    #    f.write(pagesource)

except:
    os._exit(1)

