from openpyxl import Workbook

book_obj = Workbook()
excel_sheet = book_obj.active
excel_sheet['A1'] = 'st_id'
excel_sheet['A2'] = 'A'
excel_sheet['A3'] = 'B'
excel_sheet['B1'] = 'name'
excel_sheet['B2'] = 'ali'
excel_sheet['B3'] = 'yonghui'

excel_sheet['C1'] = 'lastname'
excel_sheet['C2'] = 'shim'
excel_sheet['C3'] = 'hayley'

book_obj.save('testt.xlsx')
print('Excel file created successfully')


