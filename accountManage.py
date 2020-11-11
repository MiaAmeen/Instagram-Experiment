
import webbrowser
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
import json
import time as Time
from datetime import *
import random
from selenium.webdriver.common.action_chains import ActionChains


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
#accounts= {"dembotf_nc":"dembotf_nc123", "repbotf_nc":"repbotf_nc123", "neutbot_nc":"neutbot_nc123"}
accounts= {"dembotf_nc":"dembotf_nc123"}

def newtab(ID,PASS):
    LOGINPG = webdriver.Chrome(path)
    LOGINPG.get(url)
    Time.sleep(1)
    LOGINPG.find_element_by_xpath("//input[@name='username']").send_keys(ID)
    LOGINPG.find_element_by_xpath("//input[@name='password']").send_keys(PASS)
    LOGINPG.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
    Time.sleep(4)
    LOGINPG.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
    LOGINPG.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()

    likeXpath= 'section.ltpMr.Slqrh > span.fr66n > button > div > span > svg[aria-label="Like"]'
    elements= LOGINPG.find_elements_by_css_selector(likeXpath)

    t1= datetime.today()
    m1= t1.minute
    m2= m1 + 58
    totlikes= 0

    for element in elements:
        if datetime.today().minute == m2:
            pass
        else:
            actions = ActionChains(LOGINPG)
            LOGINPG.execute_script('arguments[0].scrollIntoView({behavior: "smooth", block: "center", inline: "nearest"});', element)
            rand= random.randint(9,12)
            print("waiting for "+str(rand)+" seconds...")
            Time.sleep(rand)
            element.click()
            totlikes+= 1

    print("time's up!\n"+"total likes:"+str(totlikes))


for key,value in accounts.items():
    ID= key
    PASS= value
    newtab(ID,PASS)






#chdir Documents/IG/Instagram-Experiment
#python accountManage.py
