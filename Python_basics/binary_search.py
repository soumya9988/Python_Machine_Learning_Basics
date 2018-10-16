from random import sample
elements = [item for item in sample(range(1, 1000), 15)]
elements.sort()
print("Elements in the list are", elements)
choice = int(input('Enter the number to be searched: '))
while True:
    mid = int(len(elements) / 2)
    if choice == elements[mid]:
        print('Element found in the list')
        break
    elif choice > elements[mid]:
        elements = elements[mid::]
    else:
        elements = elements[0:mid:]
    if mid == 0:
        print('Sorry, element could not be found in the list!!')
        break
