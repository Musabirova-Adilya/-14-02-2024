import csv

def promocode_generate(category, day, name):
    return category[:2].upper + day[:2] + name[-1].upper + name[-2].upper + day[4] + day[3]

with open('products.csv', 'r', encoding='utf-8') as file:
    data = list(csv.DictReader(file, delimiter=';'))
    for product in data:
        product['Promocode'] = promocode_generate(product['Category'], product['Date'], product['product'])
    
with open('product_promo.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['Category', 'product', 'Date', 'Price per unit', 'Count', 'Promocode'],\
    delimiter=';')
    writer.writeheader()
    writer.writerows(data)
    

    
