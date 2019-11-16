import pickle
shop_list = ['apple', 'banana', 'flour', 'butter', 'berries', 'salmon', 'cheese', 'milk']
shop_list.sort()

with open('shopping_list.data', 'wb') as shop_file:
    pickle.dump(shop_list, shop_file)

del shop_list
with open('shopping_list.data', 'rb') as shop_file:
    storedlist = pickle.load(shop_file)
    print(storedlist)
