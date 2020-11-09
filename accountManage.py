
import webbrowser
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
import json
import time

def updateString():
    accounts = {"dem":{"m18":{}, "m25":{}, "m34":{}, "f18":{}, "f25":{}, "f34":{}}, "rep":{"m18":{}, "m25":{}, "m34":{}, "f18":{}, "f25":{}, "f34":{}}, "neut":{"m18":{}, "m25":{}, "m34":{}, "f18":{}, "f25":{}, "f34":{}}}

    for party in accounts:
        for demog in accounts[party]:
            id= str(party)+"bot"+demog+"_"+"nc"
            key= id + "123"
            accounts[party][demog] = {"Username":id, "Password":key}

    f = open("IGaccounts.txt", "r")
    strAcc= json.dumps(accounts, indent=0)
    f.write(string)
    f.write(strAcc)
    f.close()


url = 'https://www.instagram.com'
path = "/Users/destroyerofworlds/Documents/chromedriver"
accounts= {"dembotf_nc":"dembotf_nc123", "repbotf_nc":"repbotf_nc123", "neutbot_nc":"neutbot_nc123"}

for key,value in accounts.items():
    ID= key
    PASS= value
    driver = webdriver.Chrome(path)
    driver.get(url)
    time.sleep(3)
    frame = password = driver.find_element_by_xpath('/html/body')
    frame.send_keys(Keys.ENTER)
    #username = driver.find_element_by_name('username')
    username = driver.find_element_by_xpath("/html/body//*[@name='username']")
    username.send_keys(str(ID))
    username.send_keys(Keys.ENTER)
    #password = driver.find_element_by_name('password')
    password = driver.find_element_by_xpath("/html/body//*[@name='password']")
    password.send_keys(str(PASS))
    password.send_keys(Keys.ENTER)

    time.sleep(5)









#python accountManage.py
