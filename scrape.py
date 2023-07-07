import requests
import csv
import re
from collections import Counter



def output_title_and_price():

    search_term = 'food'
    page = 1
    last_page = 20
  
    with open('title_price.csv', 'w') as file:
        writer = csv.DictWriter(file, fieldnames=['Title', 'Price'])
        writer.writeheader()

        while page <= last_page:
            url = f'https://www.daraz.com.np/catalog/?page={page}&q={search_term}&ajax=True'
            response = requests.get(url)

            if response.status_code != 200:
                print(f'Error while getting data for page {page}')
                return

            data = response.json()

            if 'mods' in data and 'listItems' in data['mods']:
                products = data['mods']['listItems']

                for product in products:
                    title = product['name']
                    price = product['price']
                    try:
                        writer.writerow({'Title': title, 'Price': price})
                    except:
                        print('Error..')

            page += 1

            

def get_titles():
    titles = []
    with open('title_price.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            titles.append(row['Title'])
    print(titles)
    return titles

def extract_unit_from_title(title):
    pattern = r'(\d+\s*\w+)'
    match = re.search(pattern, title)
    if match:
        unit = match.group(1)
        title_without_unit = title.replace(unit, '').strip()
        return title_without_unit, unit.strip(), 
    else:
        return None, title.strip()


def output_with_unit():
    titles = get_titles()
    with open('unit.csv', 'w') as file:
        writer = csv.DictWriter(file, fieldnames=['Title', 'Unit'])
        writer.writeheader()
        for item in titles:
            title, unit = extract_unit_from_title(item)
            writer.writerow({'Title': title, 'Unit': unit})

    



output_title_and_price()
output_with_unit()




