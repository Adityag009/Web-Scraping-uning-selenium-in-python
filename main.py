from selenium import webdriver
import time
import pandas as pd
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.keys import Keys
import re

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')


wd = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
url='https://www.wikipedia.org/'
wd.get(url)
#Assertion statment

assert "Wikipedia" in wd.title

# Print  the entire HTML
# print(wd.page_source)

#Fetching the element by ID
input_element=wd.find_element(by=By.ID,value="searchInput")

#sending keys
input_element.send_keys('ASD')
# Fetch search button through CSS Class name
search = wd.find_element(by=By.CLASS_NAME, value='pure-button')

#Click the search button

wd.execute_script("arguments[0].click();",search)

print(wd.page_source)

#Switching windows
window_after = wd.window_handles[0]
wd.switch_to.window(window_after)
#Assertion statement
assert "ASD - Wikipedia" in wd.title

# Printing the title
print("Successfully loaded the page",wd.title)

#Fetch search button through link text
link_text = wd.find_element(By.LINK_TEXT,"Adaptive software development")
#Clicking the link
wd.execute_script("arguments[0].click();", link_text)

#Switching window
window_after = wd.window_handles[0]
wd.switch_to.window(window_after)
#Assertion statment
assert "Adaptive software development - Wikipedia" in wd.title
#printing the title
print("Successful loaded the page",wd.title)

p_tags = wd.find_elements(by=By.TAG_NAME, value="p")

#printing the array with <p> tag element
print("Number of tags found:", len(p_tags))

text_lines= ""
for p_tag in p_tags:
    text_lines = text_lines + p_tag.text

print(text_lines)

pattern = r'[[0-9]\]'

new_string = re.sub(pattern,'',text_lines)
print(new_string)

elems=  wd.find_elements(by=By.CSS_SELECTOR,value='p>a')

#Creating Dictionary
links_dict={}
for elem in elems:
    links_dict[elem.text] = elem.get_attribute('href')
print(links_dict)
