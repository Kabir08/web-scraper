from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import csv

options = Options()
options.add_argument("--headless")

driver = webdriver.Chrome(options=options)

filecsv = open('file.csv', 'w', encoding='utf8', newline='')
csv_columns = ['name', 'price', 'img', 'link']
writer = csv.DictWriter(filecsv, fieldnames=csv_columns)
writer.writeheader()

driver.get("https://www.scrapingcourse.com/ecommerce/")
products = driver.find_elements(By.XPATH, "//*[@id='main']/ul/li")

for product in products:
    name = product.find_element(By.XPATH, ".//h2").text
    price = product.find_element(By.XPATH, ".//span").text
    img = product.find_element(By.XPATH, ".//img").get_attribute("src")
    link = product.find_element(By.XPATH, ".//a").get_attribute("href")

    writer.writerow({'name': name, 'price': price, 'img': img, 'link': link})

filecsv.close()
driver.close()
