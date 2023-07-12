from modules.scrape import scrape
import os
import csv

def test_scrape():
    search_term = 'foods'

    scrape(search_term)

    input_file = f'./csv-files/{search_term}.csv'
    unit_file = f'./csv-files/unit_{search_term}.csv'


    with open(input_file, 'r') as file:
        reader = csv.DictReader(file)

        input_count = 0 
        for row in reader:
            title = row['Title']
            price = row['Price']

            assert isinstance(title, str) , "Title is not a sting"
            assert len(title) > 0, "Empty string not valid"
            assert isinstance(price, str), "Invalid price"
            
            input_count += 1
        

    with open(unit_file, 'r') as file:
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

    
    assert input_count == transformed_count, "Mismatch in row between extracted and transformed data"
        




        
        
    
if __name__ == '__main__':
    search_term = 'foods'
    test_scrape(search_term)


