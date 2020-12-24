
import webbrowser
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import Chrome
import json
import time as Time
from datetime import *
import random
import csv


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
accounts= {"repbotf_nc":"repbotf_nc123", "neutbot_nc":"neutbot_nc123"}
#noUseWords= ['for and nor but or yet so since although after because before when while whose that which whichever who whoever whom whomever what whatever a an the']
#postInfo= {"rank":no, "caption": caption}

def newtab(ID,PASS):
    LOGINPG = webdriver.Chrome(path)
    LOGINPG.get(url)
    LOGINPG.maximize_window()
    Time.sleep(1)
    LOGINPG.find_element_by_xpath("//input[@name='username']").send_keys(ID)
    LOGINPG.find_element_by_xpath("//input[@name='password']").send_keys(PASS)
    LOGINPG.find_element_by_xpath("//input[@name='password']").send_keys(Keys.ENTER)
    Time.sleep(4)
    LOGINPG.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
    Time.sleep(2)
    LOGINPG.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm').click()


    t1= datetime.today()
    m1= t1.minute
    time = 2 #timer set to specified no of minutes
    print("timer started.. " + str(time) + " min from "+ str(t1.hour)+ ":"+ str(m1))
    m2= int(m1) + time
    if m2>= 60:
        m2-= 60
    else:
        pass

    data= {}
    bool= True
    count=0
    ignored_exceptions= (NoSuchElementException,StaleElementReferenceException)
    some_timeout= 10

    def chg(count):
        #lpath = "article:nth-child("+str(count)+") > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button > div > span > svg[aria-label='Like']"
        hpath = "#react-root > section > main > section > div > div:nth-child(2) > div > article:nth-child("+str(count)+") > div.eo2As > div.k_Q0X.NnvRN > a"
        return [lpath, hpath]

    while bool:

        if datetime.today().minute == m2:
            bool=False
            break
        else:
            rand= random.randint(9,12)
            count+=1

            try:
                #lpath= chg(count)[0]
                lpath = 'section.ltpMr.Slqrh > span.fr66n > button > div > span > svg[aria-label="Like"]'
                hpath= chg(count)[1]
                error= "None"

                element= WebDriverWait(LOGINPG, some_timeout,ignored_exceptions=ignored_exceptions).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, lpath)))
                LOGINPG.execute_script('arguments[0].scrollIntoView({behavior: "smooth", block: "center", inline: "nearest"});', element)
                #height= LOGINPG.execute_script('return arguments[0].scrollHeight;', element)
                print("Waiting for " + str(rand) + " seconds...")
                Time.sleep(rand)
            except BaseException as msg:
                    print(msg)
                    error= "LIKE WRONG: "+str(msg)

            try:
                a = LOGINPG.find_element_by_css_selector(hpath)
                caption= a.get_attribute('href')
            except BaseException as msg:
                    print(msg)
                    caption= " CAP WRONG: "+str(msg)

            data[count]= [caption, error]
            element.click()


    print("time's up!\n"+"total likes:"+str(count))

    LOGINPG.get('https://www.instagram.com/explore/people/suggested/')
    Time.sleep(5)  #wait for follow suggestions to load!
    folPath= "div.Igw0E.rBNOH.YBx95.ybXk5._4EzTm.soMvl > button"
    totfols= 0

    bool= True
    while bool:
        follows= LOGINPG.find_elements_by_css_selector(folPath)
        for follow in follows:
            if totfols == 5:
                bool= False
                break
            else:
                LOGINPG.execute_script('arguments[0].scrollIntoView({behavior: "smooth", block: "center", inline: "nearest"});', follow)
                Time.sleep(random.randint(3,5))
                follow.click()
                totfols+= 1

    print("All finished! Total follows:"+ str(totfols))

    with open('data.csv', 'w') as f:
        for key in data.keys():
            f.write("%s,%s\n"%(key,data[key]))

    LOGINPG.quit()

def start():
    ID= sys.argv[1]
    PASS= sys.argv[2]
    newtab(ID,PASS)

start()


#chdir Documents/IG/Instagram-Experiment
#python accountManage.py
