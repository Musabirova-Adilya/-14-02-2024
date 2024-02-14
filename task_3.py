import csv

with open('products.csv', 'r', encoding='utf-8') as file:
    data = list(csv.DictReader(file, delimiter=';'))

    category = input()
    while category != 'молоко':
        member_product = ''
        
        for product in data:
            if product['Category'] == category:
                print(member_product)
                min_count = 1000
                for count in data:
                    if float(count['Count']) > min_count: 
                        member_product = count['product']
                
                print(f'В категории: {category} товар: {member_product} был куплен {min_count} раз')
                break
        else:
            print('Такой категории не существует в нашей БД')
        category = input()
                    
                    
                
                


                



        