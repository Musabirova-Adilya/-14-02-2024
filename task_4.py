import csv

def promocode_generate(category, day, name):
    '''Описание функции promocode_generate.
    Описание аргументов:
        category - категория товара 
        day - дата поступления
        name - название продукта 
    '''
    return category[:2] + day[:2] + name[-1] + name[-2] + day[4] + day[3]

with open('products.csv', 'r', encoding='utf-8-sig') as file:
    data = list(csv.DictReader(file, delimiter=';'))
    for product in data:
        product['Promocode'] = promocode_generate(product['Category'], product['Date'], product['product'])#создаем столбец 'Promocode' и вызываем фук-цию промокод
    
with open('product_promo.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['Category', 'product', 'Date', 'Price per unit', 'Count', 'Promocode'],\
    delimiter=';')
    writer.writeheader()
    writer.writerows(data)
    
