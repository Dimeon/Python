import xml.etree.ElementTree as ET

tree = ET.parse("I:/renamed ident xml testcases/Volvo_Smoke_Test_MOST.xml")
root = tree.getroot()

i = 1
curr_id = None
for item in root.iterfind(".//testcase"):
    print(item.get('ident'))
    curr_id = 'MOST_'+str(i).zfill(4)
    #print(curr_id)

    item.set("ident", curr_id)

    print(item.get("ident"))
    i += 1

tree.write("C:/Volvo_Smoke_Test_MOST.xml", xml_declaration=True, encoding='iso-8859-1', method='xml')