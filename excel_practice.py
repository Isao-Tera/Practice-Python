import openpyxl as excel

# make a new workbook
book = excel.Workbook()

# get an active worksheet
sheet = book.active

# insert a word to A1 cell
sheet['A1'] = "Hello excel"

# save the excel file
book.save("hello.xlsx")