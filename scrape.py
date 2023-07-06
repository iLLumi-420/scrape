import requests
import csv
import re
from collections import Counter

def generate_ngrams(text, n):
    words = [word for word in re.split(r"\s+", text.strip())]
    temp = zip(*[words[i:] for i in range(0, n)])
    ans = [' '.join(ngram) for ngram in temp]
    return ans

def get_all_ngrams(array):
    return [item for list in array for item in list]

def extract_unit_from_title(title):
    pattern = r'(\d+\s*\w+)'
    match = re.search(pattern, title)
    if match:
        unit = match.group(1)
        title_without_unit = title.replace(unit, '').strip()
        return unit.strip(), title_without_unit
    else:
        return None, title.strip()


def get_food_item_title():

    search_term = 'food'
    page = 1
    last_page = 20

    titles = []
    
    with open('output.csv', 'w') as file:
        writer = csv.DictWriter(file, fieldnames=['Title', 'Unit'])
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
                    titles.append(title)
                    unit, title_without_unit = extract_unit_from_title(title)

                    writer.writerow({'Title': title_without_unit, 'Unit': unit})

            page += 1

    return titles



get_food_item_title()

# unigrams = [generate_ngrams(title, 1) for title in titles ]
# all_unigrams = get_all_ngrams(unigrams)

# count_all_unigrams = Counter(all_unigrams)
# most_frequent_unigram = [ngram for ngram, count in count_all_unigrams.most_common(30)]
# print(most_frequent_unigram)





# def check_for_units(title):
#     for item in most_frequent_unigram:
#         if item in title:
#             print(item)
    

# for title in titles:
#     check_for_units(title)


