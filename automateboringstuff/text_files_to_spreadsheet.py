import openpyxl

with open('madlibs_text.txt') as input_file:
    text = input_file.readlines()

new_wb = openpyxl.Workbook()
new_ws = new_wb.active
new_ws.title = 'Text from madlibs'

for line in text:
    new_ws.append([line.strip()])

new_ws.column_dimensions['A'].width = 100
new_wb.save('text_to_excel.xlsx')
