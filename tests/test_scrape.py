from modules.scrape import extract_unit

def test_extract_unit_from_title():
    
    expected_result = 'This is an item', 1000.0
    assert extract_unit('This is an item 1KG') == expected_result

    expected_result = 'Parle Monaco Classic Regular', 150.0
    assert extract_unit('Parle Monaco Classic Regular 150g') == expected_result

    expected_result = 'Slurrp Farm Healthy Snacks for Kids | Mighty Puff Cheese & Herbs| Not Fried, No Maida',None
    assert extract_unit('Slurrp Farm Healthy Snacks for Kids | Mighty Puff Cheese & Herbs| Not Fried, No Maida') == expected_result

    expected_result = 'Sushi Nori (Kagawa) 10 Sheets,', 25.0
    assert extract_unit('Sushi Nori (Kagawa) 10 Sheets, 25g') == expected_result

    expected_result = 'Britannia/Marie Gold Biscuits/ (Pack of 12)', 50.0
    assert extract_unit('Britannia/Marie Gold Biscuits/50g (Pack of 12)') == expected_result



if __name__ == '__main__':
    print('Running unit extraction test')
    test_extract_unit_from_title()
