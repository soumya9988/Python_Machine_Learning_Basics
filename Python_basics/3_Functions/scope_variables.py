x = 50
y = 100


def change_scope_numb():
    global x
    x = 20
    y = 30
    print('Value of x inside function is %d' % (x))
    print('Value of y inside the function is %d' % (y))


def print_text(text_str, times=2):
    print(text_str * times)


change_scope_numb()
print('Value of x outside the function is %d' % (x))
print('Value of y outside the function is %d' % (y))

print_text("Hello")
print_text("More Hello! ", 5)

