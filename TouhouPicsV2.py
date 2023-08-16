import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
url = 'https://img.paulzzh.com/touhou/random'
for i in range(1, 201):
    headers = {
        'Referer': 'https://img.paulzzh.com/touhou/random',
        'Host': 'img.paulzzh.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',}
    
    driver = webdriver.Safari()
    driver.get(url)
    a = driver.find_element(By.XPATH, "//body/img")
    href = a.get_attribute('src')
    print(href)
    myfile = requests.get(href)
    open((str(i)+'.png'), 'wb').write(myfile.content)
    driver.quit()
print('--end--')
