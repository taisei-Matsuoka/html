#%%
from flask import Flask,render_template,request,url_for
import time
import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import requests
from bs4 import BeautifulSoup
import re
import glob,random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import json


app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/',methods=['POST'])
def getyoutubeid():
    keyword=request.form['keyword']
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.youtube.com/c/yoshinori-yamamoto/search?query='+keyword)
    # searchbtn = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-browse/div[3]/ytd-c4-tabbed-header-renderer/tp-yt-app-header-layout/div/tp-yt-app-header/div[2]/tp-yt-app-toolbar/div/div/tp-yt-paper-tabs/div/div/ytd-expandable-tab-renderer[7]/yt-icon-button/button')
    # searchbtn.click()
    # time.sleep(5)
    # search=driver.find_element_by_css_selector('#input-1 > input').send_keys(keyword)
    # searchbtn.send_keys(Keys.ENTER)
    # time.sleep(3)
 #------------------------1---------------
    base=driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer[1]/div[3]/ytd-video-renderer/div[1]/div/div[1]/div/h3/a')
    url=base.get_attribute('href')
    url1= url.replace('https://www.youtube.com/watch?v=','')
    base=driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer[2]/div[3]/ytd-video-renderer/div[1]/div/div[1]/div/h3/a')
    url=base.get_attribute('href')
    url2= url.replace('https://www.youtube.com/watch?v=','')
    base=driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer[3]/div[3]/ytd-video-renderer/div[1]/div/div[1]/div/h3/a')
    url=base.get_attribute('href')
    url3= url.replace('https://www.youtube.com/watch?v=','')
    base=driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer[4]/div[3]/ytd-video-renderer/div[1]/div/div[1]/div/h3/a')
    url=base.get_attribute('href')
    url4= url.replace('https://www.youtube.com/watch?v=','')
    base=driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer[5]/div[3]/ytd-video-renderer/div[1]/div/div[1]/div/h3/a')
    url=base.get_attribute('href')
    url5= url.replace('https://www.youtube.com/watch?v=','')
    base=driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer[6]/div[3]/ytd-video-renderer/div[1]/div/div[1]/div/h3/a')
    url=base.get_attribute('href')
    url6= url.replace('https://www.youtube.com/watch?v=','')

    return render_template('pass.html', url1=url1,url2=url2,url3=url3,url4=url4,url5=url5,url6=url6)

print()

if __name__ == "__main__":
    app.run()