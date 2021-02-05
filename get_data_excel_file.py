import openpyxl as excel

# Open an excle file
book = excel.load_workbook("../hello.xlsx")

# get the 1st worksheet
sheet = book.worksheets[0]

# get A1 cell value
cell = sheet["A1"]

print(cell.value)