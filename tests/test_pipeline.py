from modules.scrape import extract_products, transform_products
import os
import csv

def test_extract_products():
    search_term = 'foods'

    file_path = f'./csv-files/{search_term}.csv'
    if os.path.exists(file_path):
        extract = extract_products(search_term)
        expected_result = f'File for {search_term} already exists'

        assert extract == expected_result

    else:
        extract = extract_products(search_term)
        expected_result = f'Successfully created csv file for {search_term}'

        assert extract == expected_result


    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
                
        for row in reader:
            title = row['Title']
            price = row['Price']

            assert isinstance(title, str) , "Title is not a sting"
            assert len(title) > 0, "Empty string not valid"
            assert isinstance(price, str), "Invalid price"


def test_transform_products():
    search_term = 'foods'

    unit_file_path = f'./csv-files/unit_{search_term}.csv'

    if os.path.exists(unit_file_path):
        transform = transform_products(search_term)
        expected_result = f'Unit data for {search_term} has already been transformed and saved'

        assert transform == expected_result

    else:
        transform = transform_products(search_term)
        expected_result == f'Succesfully created unit file for {search_term}'

        assert transform == expected_result


    with open(unit_file_path, 'r') as file:
        reader = csv.DictReader(file)

        transformed_count = 0
        
        for row in reader:
            title = row['Title']
            unit = row['Unit(grams)']
            price = row['Price(NRs)']
            transformed_count += 1

            assert isinstance(title, str) , "Title is not a sting"
            assert len(title) > 0, "Empty string not valid"
            assert unit is None or isinstance(unit, str) , "Invalid unit"
            assert isinstance(price, str), "Invalid price"
        
        assert transformed_count > 0, "No data in unit file"
        
    file_path = f'./csv-files/{search_term}.csv'
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        extracted_count = sum(1 for row in reader)

        assert extracted_count > 0 , "No data in extracted file"

        extracted_count == transformed_count, "Mismatch in row between extracted and transformed data"
        
    
if __name__ == '__main__':
    test_extract_products()
    test_transform_products()


