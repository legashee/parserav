import json
from turtle import title
from unicodedata import category
from selenium import webdriver
import selenium.common.exceptions as exc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium_stealth import stealth
import time

# categories
phones = "телефоны"

print("Выберите категорию")
category = input()
print("Введите название товара")
item = input()

a = 1
b = 1


data = {

}
data2 = {

}

options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors")
options.add_argument("--ignore-ssl-errors")
options.add_argument("start-maximized")

# options.add_argument("--headless")

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options)
driver.set_page_load_timeout(2000)

stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

url = "https://www.avito.ru/tyumen?q=" + item + "&s=104"
# categories

if category == phones:
    url = "https://www.avito.ru/tyumen/telefony?q=" + item + "&s=104"
elif len(item) == 0:
    url = "https://www.avito.ru/tyumen/telefony?" + "s=104"

with open('result2.json', 'w', encoding="utf-8") as f:
    pass

driver.get(url)
driver.quit()
driver.get(url)
while True:

    blocks = driver.find_element(By.CLASS_NAME, "index-content-_KxNP")
    posts = blocks.find_elements(By.CLASS_NAME, "iva-item-body-KLUuy")

    for post in posts:
        product_link = post.find_element(
            By.TAG_NAME, "a").get_attribute("href")
        title = post.find_element(By.TAG_NAME, "h3").text
        price = post.find_element(By.CLASS_NAME, "price-text-_YGDY").text

        data[a] = {
            "url": product_link,
            "title": title,
            "price": price
        }
        a += 1
    with open("result.json", "w", encoding="utf-8") as f1:
        json.dump(data, f1, indent=4, ensure_ascii=False)

    if len(data2) == 0:
        pass
    else:
        with open('result.json', 'r', encoding="utf-8") as json_file:
            data1 = json.load(json_file)
        with open('result2.json', 'r', encoding="utf-8") as json_file2:
            data2 = json.load(json_file2)
        if data2["1"]["url2"] == data1["1"]["url"]:
            print("нового нет")
        elif data2["1"]["url2"] == data1["2"]["url"]:
            print(data1["1"]["title"] + " / " + data2["1"]["price"] + " / " + data2["1"]["url"])
        elif data2["1"]["url2"] == data1["3"]["url"]:
            print(data1["1"]["title"] + " / " + data2["1"]["price"] + " / " + data2["1"]["url"])
            print(data1["2"]["title"] + " / " + data2["2"]["price"] + " / " + data2["2"]["url"])
        elif data2["1"]["url2"] == data1["4"]["url"]:
            print(data1["1"]["title"] + " / " + data2["1"]["price"] + " / " + data2["1"]["url"])
            print(data1["2"]["title"] + " / " + data2["2"]["price"] + " / " + data2["2"]["url"])
            print(data1["3"]["title"] + " / " + data2["3"]["price"] + " / " + data2["3"]["url"])

    print("Товары внесены в список!")
    time.sleep(2)


    blocks2 = driver.find_element(By.CLASS_NAME, "index-content-_KxNP")
    posts2 = blocks2.find_elements(By.CLASS_NAME, "iva-item-body-KLUuy")

    for post2 in posts2:
        product_link2 = post2.find_element(
            By.TAG_NAME, "a").get_attribute("href")
        title2 = post2.find_element(By.TAG_NAME, "h3").text
        price2 = post2.find_element(By.CLASS_NAME, "price-text-_YGDY").text

        data2[b] = {
            "url2": product_link2,
            "title2": title2,
            "price2": price2
        }
        b += 1

    with open("result2.json", "w", encoding="utf-8") as f2:
        json.dump(data2, f2, indent=4, ensure_ascii=False)
    print("Товары внесены в список!")

    with open('result.json', 'r', encoding="utf-8") as json_file:
        data1 = json.load(json_file)
    with open('result2.json', 'r', encoding="utf-8") as json_file2:
        data2 = json.load(json_file2)

    if data1["1"]["url"] == data2["1"]["url2"]:
        print("нового нет")
    elif data1["1"]["url"] == data2["2"]["url2"]:
        print(data2["1"]["title2"] + " / " + data2["1"]["price2"] + " / " + data2["1"]["url2"])
    elif data1["1"]["url"] == data2["3"]["url2"]:
        print(data2["1"]["title2"] + " / " + data2["1"]["price2"] + " / " + data2["1"]["url2"])
        print(data2["2"]["title2"] + " / " + data2["2"]["price2"] + " / " + data2["2"]["url2"])
    elif data1["1"]["url"] == data2["4"]["url2"]:
        print(data2["1"]["title2"] + " / " + data2["1"]["price2"] + " / " + data2["1"]["url2"])
        print(data2["2"]["title2"] + " / " + data2["2"]["price2"] + " / " + data2["2"]["url2"])
        print(data2["3"]["title2"] + " / " + data2["3"]["price2"] + " / " + data2["3"]["url2"])

    time.sleep(2)
    driver.refresh()
