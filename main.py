print('Задача 1')
with open('recipes.txt', 'rt', encoding='utf-8') as f:
    cook_book = {}
    for line in f:
        dish_name = line.strip()
        ingr_count = int(f.readline())
        ingredients = [] # создаем пустой список, который потом будет значением по ключу словаря
        for i in range(ingr_count):
            ingredient_line = f.readline().strip()
            ingredient_name, quantity, measure = ingredient_line.split(' | ')
            ingredients.append({'ingredient_name': ingredient_name,
                                'quantity': quantity,
                                'measure': measure
                                })
        f.readline()
        cook_book[dish_name] = ingredients
print(cook_book)

print('Задача №2')
def get_shop_list_by_dishes(dishes, person_count):
    """
    Функция на вход принимает список блюд из cook_book и количество персон для кого мы будем готовить
    и возварщает словарь с названием ингредиентов и его количества для блюда
    """
    ingredients_dict = {}
    quantity_measure = {}
    for elem in dishes:
        elem_count = len(cook_book[elem])
        for i in range(elem_count):
            ingr_name = cook_book[elem][i]['ingredient_name']
            if ingr_name in ingredients_dict.keys():
                quantity_measure['measure'] = cook_book[elem][i]['measure']
                quantity_measure['quantity'] = int(cook_book[elem][i]['quantity']) * person_count * 2
                ingredients_dict[ingr_name] = quantity_measure
            else:
                quantity_measure['measure'] = cook_book[elem][i]['measure']
                quantity_measure['quantity'] = int(cook_book[elem][i]['quantity']) * person_count
                ingredients_dict[ingr_name] = quantity_measure
    print(ingredients_dict)

get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2)