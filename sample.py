from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os
import urllib
import requests
import io
from PIL import Image
import time


chrome_options = Options()
# chrome_options.add_argument("--headless")  # Example capability

PATH = "C:\\Users\\abdur\\OneDrive\\Desktop\\scrape\\chromedriver.exe"

wd = webdriver.Chrome(service=Service(PATH), options = chrome_options)


url = "https://stock.adobe.com/in/search?filters%5Bcontent_type%3Aphoto%5D=1&filters%5Bcontent_type%3Aillustration%5D=1&filters%5Bcontent_type%3Azip_vector%5D=1&filters%5Bcontent_type%3Avideo%5D=1&filters%5Bcontent_type%3Atemplate%5D=1&filters%5Bcontent_type%3A3d%5D=1&filters%5Bcontent_type%3Aaudio%5D=0&filters%5Binclude_stock_enterprise%5D=0&filters%5Bis_editorial%5D=0&filters%5Bfree_collection%5D=0&filters%5Bcontent_type%3Aimage%5D=1&k=beautiful+mosque&order=relevance&safe_search=1&search_page=2&get_facets=0&search_type=pagination"
wd.get(url)
wd.execute_script("window.scrollTo(0,document.body.scrollHeight);")
time.sleep(5)

image_urls = []

for i in range(0, 50):

    xpath =f"""/html/body/div[1]/main/div/div/div[2]/div[2]/div[4]/div[3]/div/div/div[2]/div[{i}]/div[1]/a/picture/img"""
    img_results = wd.find_elements(By.XPATH, xpath)

    time.sleep(0.4)

    for img in img_results:
        image_urls.append(img.get_attribute('src'))

folder_path = 'images/' # change your destination path here

if not os.path.exists(folder_path):
    os.makedirs(folder_path)

counter = 0
for i in range(len(image_urls)):
    counter = i + 88
    urllib.request.urlretrieve(str(image_urls[i]), folder_path + "image_" + f"{counter}.jpg")


wd.quit()

