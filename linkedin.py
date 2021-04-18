from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys



################################ webdriver for firefox


from webdriver_manager.firefox import GeckoDriverManager


browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())


#######################################################

query="python%20developer"

browser.get(f"https://www.linkedin.com/jobs/search/?geoId=102713980&keywords={query}&location=India")

n=0
time.sleep(10)
ele= browser.find_element_by_tag_name('body')
itertn=0
while n<40:
        ele.send_keys(Keys.PAGE_DOWN)
        time.sleep(3)
        n+=1
n=0
time.sleep(3)
while n<40:
    infi_btn=browser.find_elements_by_css_selector('button.infinite-scroller__show-more-button')
    infi_btn[0].send_keys(Keys.ENTER)
    if not infi_btn:
        break
    while itertn<10:
        ele.send_keys(Keys.PAGE_DOWN)
        time.sleep(3)
        itertn+=1
    n+=1
    itertn=0


import pandas as pd
import numpy as np

df = pd.DataFrame(columns = ['position', 'company', 'location'])

data=np.array(browser.find_elements_by_css_selector('li.job-result-card'))

for i in data:
    position=i.find_elements_by_css_selector('div.job-result-card__contents h3.job-result-card__title')[0]
    company=i.find_elements_by_css_selector('h4.job-result-card__subtitle')[0]
    location=i.find_elements_by_css_selector('div.job-result-card__meta span.job-result-card__location')[0]
    df=df.append({'position':position.text,'company':company.text,'location':location.text},ignore_index=True)

df.to_csv('datafile123.csv')
