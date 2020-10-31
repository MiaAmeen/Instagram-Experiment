
import webbrowser
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome

accounts = {"dem":{"m18":{}, "m25":{}, "m34":{}, "f18":{}, "f25":{}, "f34":{}}, "rep":{"m18":{}, "m25":{}, "m34":{}, "f18":{}, "f25":{}, "f34":{}}, "neut":{"m18":{}, "m25":{}, "m34":{}, "f18":{}, "f25":{}, "f34":{}}}

for party in accounts:
    for demog in accounts[party]:
        print(demog.upper())
        id= str(party)+"bot"+demog+"_"+"nc"
        key= id + "123"
        accounts[party][demog] = {"Username":id, "Password":key}

url = 'https://www.instagram.com/'

'''if os.getcwd() != "/Users/destroyerofworlds/Applications":
    os.chdir("/Users/destroyerofworlds/Applications")
else:
    pass

chromepath= 'open -a /Applications/Google\ Chrome.app %s'
webbrowser.get(chromepath).open(url, new=1)'''

driver = webdriver.chrome()
driver.get(url)

#python accountManage.py
