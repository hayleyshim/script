import openpyxl

book_obj = openpyxl.load_workbook('database.xlsx')
excel_sheet = book_obj.active
cells = excel_sheet['A1':'E4']
for c1, c2, c3, c4, c5 in cells:
    print("{0:4}  {1:4}  {2:4}  {3:4}  {4:4}".format(c1.value, c2.value, c3.value, c4.value, c5.value))