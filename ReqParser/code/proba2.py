import xml.etree.ElementTree as ET

context = ET.iterparse("Eng8_SW_Tests.xml", events=("start", "end"))

path = []
reqs = {}
ident_value = ''
desc_value = ''
on_testcase_tag = False
for event, elem in context:
    tag = elem.tag
    value = elem.text
    testcase_tag = tag == 'testcase'
    ident = tag == 'ident'
    description = tag == 'description'
    if event == 'start':
        if value:
            if testcase_tag:
                if ident:
                    ident_value = value
                    print(ident_value.text)
                if description:
                    desc_value = value
                    print(desc_value)
