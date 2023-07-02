from selenium import webdriver
import os
import csv
import time
from bs4 import BeautifulSoup

os.environ['PATH'] += r"D:\Drivers\chromedriver.exe"

driver = webdriver.Chrome()

driver.get('https://www.daraz.com.np/catalog/?q=food')

time.sleep(3)

html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')

items = soup.find_all('div', {'class':'box--pRqdD'})

food_data = {}
for item in items:
    name = item.find('div', {'class':'title--wFj93'}).text.strip()
    price = item.find('span', {'class':'currency--GVKjl'}).text.strip()
    discount_element = item.find('span', {'class':'discount--HADrg'})

    
    if discount_element is not None:
        discount = discount_element.text.strip()
    else:
        discount = 'None'

    food_data[name] = {'price': price, 'discount': discount}


with open('output.csv', 'w') as file:
    writer = csv.DictWriter(file, fieldnames=['Name', 'Price', 'Discount'])
    writer.writeheader()
    for name, data in food_data.items():
        writer.writerow({'Name': name , 'Price': data['price'], 'Discount': data['discount']})


driver.quit()










# import requests
# from bs4 import BeautifulSoup

# def get_foot_items():
#     search_term = 'food'
#     url = f'https://www.daraz.com.np/catalog/?q={search_term}'

#     response = requests.get(url)
    
#     if response.status_code != 200:
#         print('Error while getting data')
#         return
    
#     soup = BeautifulSoup(response.content, 'html.parser')
#     print(soup)
#     food_items = soup.find_all('div', {'class':'box--pRqdD'})

#     print(food_items)


# get_foot_items()