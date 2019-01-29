import traceback

try:
    raise Exception('This is a test exception raised')

except:
    with open('error_file.txt', 'w') as error_file:
        error_file.write(traceback.format_exc())
    print('Error info has been written in the error_file')

