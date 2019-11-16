my_shopping_list = ['butter', 'egg', 'milk', 'fish', 'potato']
dessert_list = ('ice cream', 'cookie', 'pineapple')


print('I have %d items to buy and they are: ' % (len(my_shopping_list)))
for item in my_shopping_list:
    print(item, end=' ')


my_shopping_list.sort()
print('After sorting, the list is: ', my_shopping_list)


my_shopping_list.append('Water melon')
print('Modified shopping list is: ', my_shopping_list)


del my_shopping_list[2]
print('After deletion the list is ', my_shopping_list)

my_shopping_list.insert(2, 'Ice cream')
print('Adding new value: ', my_shopping_list)


ind = my_shopping_list.index('egg')
print('Index of egg is: ', ind)

# Tuples.....

print('The dessert menu is', dessert_list)
food_menu = ('Pasta', 'meatballs', dessert_list)
print('Food menu is :')
for item in food_menu:
    print(item, end=' ')
print('Number of dessert items are: ', len(food_menu[2]))
print('Hope you like all the %d items!' % (len(food_menu) - 1 + len(food_menu[2])))









