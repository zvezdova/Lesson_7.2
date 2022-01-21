cook_book = {
  'Омлет': [
    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
  'Утка по-пекински': [
    {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
  'Запеченный картофель': [
    {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
    {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
  }

def get_shop_list_by_dishes(dishes, person_count):  
    
    shop_dict_keys = []
    shop_dict_values = []
 
    for dish in dishes:        
        if dish in list(cook_book.keys()): 
            for element in cook_book[dish]:
                new_element = {}
                shop_dict_keys.append(element['ingredient_name'])                                
                new_element['measure'] = element['measure'] 
                new_element['quantity'] = int(element['quantity']) * int(person_count)
                shop_dict_values.append(new_element)
    
    shop_dict = dict(zip(shop_dict_keys, shop_dict_values))
    print(shop_dict)         
        

get_shop_list_by_dishes(['Омлет'], 3)