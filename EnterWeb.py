#进入网页
from selenium import webdriver
import re,time

wait_time = 1
wait_time1 = 3
username = "2018000013"
password = "qw123456"

def login(username,password):
    global driver
    driver = webdriver.Chrome()
    driver.get("https://zjiet.cpdaily.com/portal/index.html")
    time.sleep(wait_time)
    driver.find_element_by_xpath("//div[@id='ampHasNoLogin']/span").click()
    time.sleep(wait_time)
    driver.find_element_by_xpath("//input[@type='text']").send_keys(username)
    driver.find_element_by_xpath("//input[@type='password']").click()
    driver.find_element_by_xpath("//input[@type='password']").clear()
    driver.find_element_by_xpath("//input[@type='password']").send_keys(password)
    time.sleep(wait_time1)
    driver.find_element_by_xpath("//div[@id='app']/div/div/div/div/div[2]/div/div[2]/div/div/div[4]/div/span").click()
    time.sleep(wait_time)
    driver.get("https://zjiet.cpdaily.com/wec-counselor-leave-apps/leaveadmin/pcAdmin/index.html#/list")
    time.sleep(wait_time1)

if __name__ == "__main__":
    login(username,password)
    go_to_qinjia_page()