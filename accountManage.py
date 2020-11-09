
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
    LOGINPG = webdriver.Chrome(path)
    LOGINPG.get(url)
    driver.execute_script("window.open('','_blank');")
    time.sleep(3)
    LOGINPG.find_element_by_xpath("//input[@name='username']").send_keys(ID)
    LOGINPG.find_element_by_xpath("//input[@name='password']").send_keys(PASS)
    LOGINPG.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
    time.sleep(5)







#python accountManage.py
