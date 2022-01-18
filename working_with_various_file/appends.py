from openpyxl import Workbook

book_obj = Workbook()
excel_sheet = book_obj.active
rows = (
    ('st_id', 'name', 'lastname', 'email', 'phone'),
    ('A', 'ali','yonghui','yonghui@gmail.com','1234312'),
    ('B','shim','yonghui','yhshim17@gmail.com','12314')
)

for values in rows:
    excel_sheet.append(values)
    print()
print('values are successfully appended')
book_obj.save('data.xlsx')