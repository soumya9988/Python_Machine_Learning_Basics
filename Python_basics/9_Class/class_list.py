class List_mod:
    def __init__(self):
        self.new_list = []

    def add_value(self, val):
        self.new_list.append(val)
        return self.new_list

    def delete_value(self, val):
        if val in self.new_list:
            self.new_list.remove(val)
        return self.new_list

    def display_value(self):
        print('The values in the list are:')
        for item in self.new_list:
            print(item)


if __name__ == '__main__':
    choice = 1
    list_obj = List_mod()
    while choice != 0:
        print('1. Add Value to a list')
        print('2. Delete value from list')
        print('3. Display the list')
        print('0: Exit')
        choice = int(input('Please enter your choice: '))
        if choice == 1:
            val = int(input('Enter the value to be added to the list:'))
            list_obj.add_value(val)
        elif choice == 2:
            val = int(input('Enter the value to be deleted from the list:'))
            list_obj.delete_value(val)
        elif choice == 3:
            list_obj.display_value()
        else:
            print('Exiting....')
            break
