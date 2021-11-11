import pytest
import time
import requests
from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\\Selenium\\chromedriver.exe")
driver.get("https://web.qasir.id/sign-in")
driver.maximize_window()



driver.find_element_by_xpath("//input[@id='sign-in-phonenumber']").send_keys("87877996114")
driver.find_element_by_xpath("//input[@id='password']").send_keys("123456")
driver.find_element_by_xpath("//input[@id='submit-btn-signin']").click()
time.sleep(5)

newAdd = "https://web.qasir.id/sign-in"
# print('newAdd ' + newAdd)
newAdd = 'https://testqasir-603666.' + newAdd[12:21] + 'dashboard'
# print('addressbaru = ', newAdd)
driver.get(str(newAdd))


driver.find_element_by_xpath("//body/div[@id='appWebApp']/div[1]/div[1]/ul[1]/li[10]/a[1]").click()
driver.find_element_by_xpath("//body/div[@id='navbarInstance']/div[1]/div[1]/div[1]/ul[1]/li[1]/a[1]/div[1]/img[1]").click()
driver.find_element_by_xpath("//body/div[@id='navbarInstance']/div[1]/div[1]/div[1]/ul[1]/li[1]/ul[1]/li[3]/a[1]").click()

driver.find_element_by_xpath("//input[@id='user_image']").send_keys(r'C:\Users\Nursaputra\PycharmProjects\QasirTest\Qasir\qasir.png')
driver.find_element_by_xpath("//button[contains(text(),'Terapkan Foto')]").click()





