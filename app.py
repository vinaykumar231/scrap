import json
from bs4 import BeautifulSoup

# Read index.html file
with open('page5.html', 'r', encoding='utf-8') as file:
    content = file.read()

# Parse HTML content with Beautiful Soup
soup = BeautifulSoup(content, 'html.parser')

# Find all divs with the specified class
divs = soup.find_all('div', class_='sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 AdHolder sg-col s-widget-spacing-small sg-col-12-of-16')

data = []

# Process each div
for div in divs:
    img = div.find('img', class_='s-image')
    product_url = img['src'] if img else ''
    
    title_span = div.find('span', class_='a-size-medium a-color-base a-text-normal')
    product_name = title_span.text if title_span else ''
    
    rating_span = div.find('span', class_='a-icon-alt')
    rating = rating_span.text if rating_span else ''
    
    price_span = div.find('span', class_='a-price-whole')
    product_price = price_span.text if price_span else ''
    
    data.append({
        'Product URL': product_url,
        'Product Name': product_name,
        'rating': rating,
        'Product price': product_price
    })

# Write data to data.json
with open('data5.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

print('Data has been extracted and saved to data.json')
