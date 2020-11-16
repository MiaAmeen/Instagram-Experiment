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

url = 'https://www.instagram.com'
path = "/Users/destroyerofworlds/Documents/chromedriver"
accounts= {"dembotf_nc":"dembotf_nc123", "repbotf_nc":"repbotf_nc123", "neutbot_nc":"neutbot_nc123"}
data= {}
#noUseWords= ['for and nor but or yet so since although after because before when while whose that which whichever who whoever whom whomever what whatever a an the']
#postInfo= {"rank":no, "caption": caption}
ID= "repbotf_nc"
PASS= "repbotf_nc123"

LOGINPG = webdriver.Chrome(path)
LOGINPG.get(url)
LOGINPG.maximize_window()
Time.sleep(1)
LOGINPG.find_element_by_xpath("//input[@name='username']").send_keys(ID)
LOGINPG.find_element_by_xpath("//input[@name='password']").send_keys(PASS)
LOGINPG.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
Time.sleep(4)
LOGINPG.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
Time.sleep(2)
LOGINPG.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm').click()

likeXpath= 'section.ltpMr.Slqrh > span.fr66n > button > div > span > svg[aria-label="Like"]'
capPath = 'div.eo2As > div.EtaWk > div > div.Igw0E.IwRSH.eGOV_._4EzTm.pjcA_ > div > span._8Pl3R'
count= 0

while count!=5:
    count+=1
    caption= LOGINPG.execute_script('return document.querySelector("div.eo2As > div.EtaWk > div > div.Igw0E.IwRSH.eGOV_._4EzTm.pjcA_ > div > span._8Pl3R");')
    if 'more' in caption.text:
        caption.click()
        morePath= "div.eo2As > div.EtaWk > div > div.Igw0E.IwRSH.eGOV_._4EzTm.pjcA_ > div > span._8Pl3R > span._2UvmX > button"
        LOGINPG.find_element_by_css_selector(morePath).click()
    else:
        pass
    data[count]= caption.text
    Time.sleep(3)

print(data)
#for element in elements:
    #LOGINPG.execute_script("window.scrollTo(0, Y)")
    #react-root > section > main > section > div > div:nth-child(2) > div > article:nth-child(1)
    #height = LOGINPG.execute_script("var elm = document.getElementByClassName('._8Rm4L M9sTE.L_LMM SgTZ1.ePUX4'); return elm.scrollHeight;")
    #//*[@id="react-root"]/section/main/section/div/div[2]/div/article[2]
    #//*[@id="react-root"]/section/main/section/div/div[2]/div/article[1]
    #height = LOGINPG.execute_script("return .scrollHeight;"%element)
