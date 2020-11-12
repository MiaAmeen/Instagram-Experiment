
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
accounts= {"repbotf_nc":"repbotf_nc123"}
#noUseWords= ['for and nor but or yet so since although after because before when while whose that which whichever who whoever whom whomever what whatever a an the']
#postInfo= {"rank":no, "caption": caption}

def newtab(ID,PASS):
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

#div > span._8Pl3R > span._2UvmX > button
#div > span._8Pl3R > span._2UvmX > button
    t1= datetime.today()
    m1= t1.minute
    print("timer started.. 58 min from"+ str(t1.hour)+ ":"+ str(m1))
    m2= int(m1) + 58 #timer set to 58 minutes
    if m2>= 60:
        m2-= 60
    else:
        pass

    totlikes= 0
    data= {}
    poopy= True

    while poopy:

        elements= LOGINPG.find_elements_by_css_selector(likeXpath)
        captions= LOGINPG.find_elements_by_css_selector(capPath)

        for element in elements:
            if datetime.today().minute == m2:
                poopy=False
                break
            else:
                LOGINPG.execute_script('arguments[0].scrollIntoView({behavior: "smooth", block: "center", inline: "nearest"});', element)
                #height= LOGINPG.execute_script('return arguments[0].scrollHeight;', element)
                #print(height)
                rand= random.randint(9,12)
                print("waiting for "+str(rand)+" seconds...")
                Time.sleep(rand)
                index= elements.index(element)
                if 'more' in captions[index].text:
                    try:
                        LOGINPG.find_element_by_css_selector('div > span._8Pl3R > span._2UvmX > button').click()
                    except BaseException as msg:
                        print(msg)
                else:
                    pass
                data[str(index)]= captions[index].text
                element.click()
                totlikes+= 1

    print("time's up!\n"+"total likes:"+str(totlikes))
    print(data)
    time.sleep(1)

    LOGINPG.get('https://www.instagram.com/explore/people/suggested/')
    Time.sleep(5)  #wait for follow suggestions to load!
    folPath= "div.Igw0E.rBNOH.YBx95.ybXk5._4EzTm.soMvl > button"
    totfols= 0
    while True:
        follows= LOGINPG.find_elements_by_css_selector(folPath)
        for follow in follows:
            if totfols == 50:
                break
            else:
                LOGINPG.execute_script('arguments[0].scrollIntoView({behavior: "smooth", block: "center", inline: "nearest"});', follow)
                Time.sleep((random.randint(5,8)
                follow.click()
                totfols+= 1

    print("All finished! Total follows:"+ str(totfol))

for key,value in accounts.items():
    ID= key
    PASS= value
    newtab(ID,PASS)






#chdir Documents/IG/Instagram-Experiment
#python accountManage.py
