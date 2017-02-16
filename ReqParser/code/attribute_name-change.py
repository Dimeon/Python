import xml.etree.ElementTree as ET

ET.register_namespace('', "zzz")
tree = ET.parse("C:/Project/ReqParser/Reports/Eng8_SW_Tests_undertest.xml")
root = tree.getroot()

i = 1
curr_id = None
for item in root.iterfind(".//testcase"):
    print(item.get('ident'))
    curr_id = 'ENG_'+str(i).zfill(4)
    #print(curr_id)

    item.set("ident", curr_id)

    print(item.get("ident"))
    i += 1

tree.write("C:/Project/ReqParser/output/new_xml.xml", xml_declaration=True, encoding='iso-8859-1', method='xml')