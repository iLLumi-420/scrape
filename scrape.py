import requests
import csv

def get_food_items():
    search_term = 'food'
    page = 1
    last_page = 20

    while True:
        url = f'https://www.daraz.com.np/catalog/?page={page}&q={search_term}&ajax=True'
        response = requests.get(url)
        
        if response.status_code != 200:
            print(f'Error while getting data for page {page}')
            return
        
        data = response.json()

        filter_items = data['mods']['filter']['filterItems']
        
        with open('output.csv', 'a', newline='') as file:
            writer = csv.writer(file)

            if page == 1:
                writer.writerow(['value', 'title','url','order', 'id', 'price'])

            for item in filter_items:
                options = item['options'] if 'options' in item else []
                for option in options:
                    value = option['value']
                    title = option['title']
                    order = option['order']
                    price = option['price'] if 'price' in option else ''
                    url = option['url'] if 'url' in option else ''
                    id_ = option['id']  if 'id' in option else ''
                    writer.writerow([value, title,url, order, id_, price])
        
        
        if page == last_page:
            break
        
        page += 1

get_food_items()
