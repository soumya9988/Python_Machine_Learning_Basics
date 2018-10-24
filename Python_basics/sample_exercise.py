password_list = []
alpha_lower = 'abcdefghijklmnopqrstuvwxyz'
alpha_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digit = '0123456789'
characters = '$#@'
password_io = input('Enter the passwords separated by comma: ').split(',')
for pw in password_io:
    if len(pw) < 6 or len(pw) > 12:
        continue
    low = set(alpha_lower).intersection(pw)
    upper = set(alpha_upper).intersection(pw)
    dig = set(digit).intersection(pw)
    chars = set(characters).intersection(pw)
    if len(low) > 0 and len(upper) > 0 and len(dig) > 0 and len(chars) > 0:
        password_list.append(pw)
print(password_list)














