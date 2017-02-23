import openpyxl
import xml.etree.ElementTree as ET
import json



'''filename = 'xml_config.json'
with open(filename) as f:
    pop_data = json.load(f)
    print(pop_data)
    for key, v in pop_data.items():
        print(v)'''


def xml_path():
    filename = 'xml_config.json'
    xml_path_str = []
    with open(filename) as f:
        pop_data = json.load(f)
        for key, v in pop_data.items():
            xml_path_str.append(v)
    return xml_path_str

ttt = xml_path()
print(ttt)

for ppp in ttt:
    print(ppp)