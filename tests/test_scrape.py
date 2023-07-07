from modules.scrape import extract_unit_from_title

def test_extract_unit_from_title():
    
    expected_result = 'This is an item', '1KG'
    assert extract_unit_from_title('This is an item 1KG') == expected_result

if __name__ == '__main__':
    print('Running title extraction test')
    test_extract_unit_from_title()
