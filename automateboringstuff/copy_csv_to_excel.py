from openpyxl import Workbook
import csv

csv_file = open('example.csv')
csv_reader = csv.reader(csv_file)
csv_list = list(csv_reader)
print(csv_list)

work_book = Workbook()
work_sheet = work_book.active
work_sheet.title = 'Copy of example.csv'
for row in csv_list:
    work_sheet.append(row)

work_book.save('example.xlsx')