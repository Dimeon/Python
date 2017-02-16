from openpyxl import load_workbook

filename = 'C:/Project/ReqParser/Implementation_Planing_v15.xlsx'
wb = load_workbook(filename)

sheet = wb['SWRS-AUDGenIV-V24']
cell_range = sheet['A9':'A47']

print(cell_range.value)

#wb.save('ready_document.xlsx')