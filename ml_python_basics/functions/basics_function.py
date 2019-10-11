def conversion(temp, mode):
    if mode == 1:
        c_to_f = (temp * 9/5) + 32
        return c_to_f
    else:
        f_to_c = (temp - 32) * 5 / 9
        return f_to_c


mode = int(input('Enter 1 to convert temperature from celsius to F and 2 to convert it from F to C: '))
temp = float(input('Enter the temperature for conversion: '))
converted_temp = conversion(temp, mode)
print('Converted temperature is: ', converted_temp)
