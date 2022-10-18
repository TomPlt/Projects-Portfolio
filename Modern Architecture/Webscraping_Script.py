from selenium.webdriver import Chrome
from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument("headless")
driver = Chrome(executable_path='C:/Users/tompa/Downloads/chromedriver_win32/chromedriver', options=options)
page = 1
image_list = []
tags = []
while True:
    print(page, len(image_list))
    driver.get(f'https://www.archdaily.com/search/images/categories/residential-architecture?page={page}')
    time.sleep(5)
    test = driver.find_elements_by_xpath('//div[@class="image__container"]/img')
    for i in test:
        tags.append(i.get_property('alt'))
        image_list.append(i.get_property('src'))
    with open('imgs/Resid_Architecture_Urls.txt', 'a') as f:
        for line in image_list:
            f.write(f"{line}\n")
    with open('imgs/Resid_Architecture_Descr.txt', 'a', encoding='utf-8') as f:
        for line in tags:
            f.write(f"{line}\n")
    # driver.quit()
    page += 1