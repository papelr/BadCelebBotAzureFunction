#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 18:36:02 2021

@author: robertpapel
"""

import base64
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# test image for scrape
# testing = "Barack Obama"

# Function to scrape picture of celeb ----
def pic_scrape(plain_name):


    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument('--disable-dev-shm-usage')

    # driver set up ()
    driver = webdriver.Chrome("/usr/local/bin/chromedriver", options = chrome_options)
    driver.get('https://www.google.com/imghp?hl=en&authuser=0&ogbl')
    search_box = driver.find_element_by_xpath("//input[@name='q']")
    search_box.send_keys(str(plain_name), Keys.ENTER)

    # find selenium elements
    elements = driver.find_element_by_class_name('rg_i')
    elements.click()
    element = driver.find_element_by_class_name('v4dQwb')

    # useless count variable, but lets me use the if statement, lol
    count = 0
    if count == 0:
        celeb_pic = element.find_element_by_class_name('n3VNCb')
    else:
        celeb_pic = element.find_element_by_class_name('n3VNCb')
    pic_url = celeb_pic.get_attribute("src")
    driver.close()

    # decode image and save
    imgdata = base64.b64decode(pic_url.split(",")[1])
    pic_file = plain_name + '.jpg'
    with open(pic_file, 'wb') as f:
        f.write(imgdata)

    return pic_file

# Main function ----
if __name__ == '__main__':
    pic_scrape()