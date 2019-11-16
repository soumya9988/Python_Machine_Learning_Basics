import random
tot_val = 0
more_items = True
item_list = {}

while more_items:
    item = input('Enter the item you want to purchase: ')
    if item in item_list:
        item_list[item] += 1
    else:
        item_list[item] = 1
    tot_val += random.randint(1, 10)
    more_items = input('Enter any key to continue purchasing. Press enter to quit...')


print('Your final bill is: ')
print('Item','\t\t','Price')
for itm in item_list:
    print(itm,'\t\t',item_list[itm])
print('Total value is: ', tot_val)




