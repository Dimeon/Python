import openpyxl
import xml.etree.ElementTree as ET
import json

filename = 'config.json'
with open(filename) as f:
    pop_data = json.load(f)
    print(pop_data)
for pop_dict in pop_data:
    path_name = pop_dict['Excel File']
    sheet_name = pop_dict['Excel Sheet']
    xml_sheet = pop_dict['XML File']
    print(path_name + '\n' + sheet_name)

wb = openpyxl.load_workbook(path_name)
sheet = wb[sheet_name]
excel_req_info = []  # [ (row_nr, req), (row_nr, req), .. ]

#here you iterate over the rows in the specific column
for row in range(9, sheet.max_row+1):
    for column in "A":  #Here you can add or reduce the columns
        cell_name = "{}{}".format(column, row)
        excel_req_info.append(
            (row, sheet[cell_name].value)
        )

def xml_path():
    filename = 'xml_config.json'
    with open(filename) as f:
        pop_data = json.load(f)
        print(pop_data)
        for key, v in pop_data.items():
            xml_path_str = []
            xml_path_str = xml_path_str.append(v)
            print(xml_path_str)

tree = ET.ElementTree(file=xml_sheet)
root = tree.getroot()

idents = [el.text for el in root.iterfind('.//testcase/ident')]
descs = [el.text for el in root.iterfind('.//testcase/description')]

d = {id_: desc for id_, desc in zip(idents, descs)}

print(d)
from typing import List

def find_trace(trace: str) -> List[str]:
    l = []
    for k, v in d.items():
        if trace in v:
            l.append(k)
            print(l)
    return l

for row_nr, req in excel_req_info:
    trace_id = find_trace(req)
    trace_id = str(trace_id)[2:-2]
    print(row_nr, req, trace_id)
    sheet.cell(row=row_nr, column=13).value = trace_id

wb.save('C:/Project/Python/ReqParser/output/new_big_file.xlsx')
