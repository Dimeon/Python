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
        print(pop_data)
        for key, v in pop_data.items():
            print(v)
            xml_path_str.append(v)
    print(xml_path_str)
    return xml_path_str

