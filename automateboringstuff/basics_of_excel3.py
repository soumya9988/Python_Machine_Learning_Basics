import openpyxl
from openpyxl.styles import Font

work_book = openpyxl.Workbook()
work_sheet = work_book.active

work_sheet['A1'] = 'Hello'
work_sheet['B1'] = 'Monkey'
work_sheet['C1'] = 10
work_sheet.append(['Apple', 'Pie', 9.3])
work_sheet.append(['Grapes', 'Float', 5.7])

work_sheet['A5'] = 'Total'
work_sheet['C5'] = '=SUM(C1:C3) * 2'

italic_font = Font(name = 'Times New Roman', italic=True, size=20, bold=True)
work_sheet['A5'].font = italic_font
font_1 = Font(name='Calibri', size=30, italic=True, shadow=True)
work_sheet['C5'].font = font_1

work_sheet.row_dimensions[5].height = 30
work_sheet.column_dimensions['A'].width = 30

work_sheet.merge_cells('A5:B5')
work_sheet.freeze_panes = 'C5'
work_book.save('font_check.xlsx')

