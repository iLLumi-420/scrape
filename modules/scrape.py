import requests
import csv
import re
import os


def convert_unit(unit):
    unit = unit.strip().lower()
    match = re.search(r'\d+', unit)

    if not match:
        return None
    number = match.group()

    if 'kg' in unit:
        converted_number = float(number) * 1000
        return converted_number
    
    if 'gm' in unit or 'g' in unit or 'gram' in unit or 'gms' in unit or 'grams' in unit:
        return float(number)
    else:
        return None
    
    
def extract_unit(title):
    pattern = r'(\d+\s*[A-za-z]+)'
    matches = re.findall(pattern, title)
    if matches:
        unit = matches[-1]
        title_without_unit = title.replace(unit, '').strip()
        return title_without_unit, convert_unit(unit.strip())
    else:
        return title.strip(), None


items = {}

def extract_products(search_term):

    page = 1
    last_page = 20

    file_path = f'./csv-files/{search_term}.csv'

    if os.path.exists(file_path):
        return f'File for {search_term} already exists'
        
    else:

        with open(file_path, 'a+') as file:
            writer = csv.DictWriter(file, fieldnames=['Title', 'Price'])
            if file.tell() == 0:
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
        
        return f'Successfully created csv file for {search_term}'

            

def load_raw_products(search_term):

    input_file = f'./csv-files/{search_term}.csv'
    if not os.path.exists(input_file):
        print('Data for search term {search_term} does not exist')
        return []
    
    product_list = []
    with open(input_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            product_list.append(row)
    return product_list



def transform_products(search_term):

    product_list = load_raw_products(search_term)

    output_file = f'./csv-files/unit_{search_term}.csv'
    if os.path.exists(output_file):
        return f'Unit data for {search_term} has already been transformed and saved'
    else:
        with open(output_file, 'w') as file:
            writer = csv.DictWriter(file, fieldnames=['Title', 'Unit(grams)', 'Price(NRs)'])
            writer.writeheader()
            for product in product_list:
                title = product['Title']
                price = product['Price']
                title_without_unit, unit = extract_unit(title)
                writer.writerow({'Title': title_without_unit, 'Unit(grams)': unit, 'Price(NRs)': price})
        
        return f'Succesfully created unit file for {search_term}'

    


if __name__ == '__main__':
    search_term = 'electronics'
    extract_products(search_term)
    transform_products(search_term)
