import xml.etree.ElementTree as ET
from pprint import pprint

tree = ET.ElementTree(file="Eng8_SW_Tests.xml")
root = tree.getroot()

print(root)

keys = []
reqs = []
# boroot = root.iter('ident')
# for child_of_root in boroot:
# print('Tag: %s Keys: %s Items: %s Text: %s' % (child_of_root.tag, child_of_root.keys(), child_of_root.items(), child_of_root.text))
# for item in root.iterfind('.//testcase/ident'):
#     ident = item.text
#     print('Testcase number: %s' % ident)
# for elem in root.iterfind('.//testcase/description'):
#     desc = elem.text
#     reqs.append([desc])
#     print('Requirement: %s' % desc)

idents = [el.text for el in root.iterfind('.//testcase/ident')]
descs = [el.text for el in root.iterfind('.//testcase/description')]

d = {id_: desc for id_, desc in zip(idents, descs)}

# print(d)
# pprint(d)
from typing import List


def find_trace(trace: str) -> List[str]:
    l = []
    for k, v in d.items():
        if trace in v:
            l.append(k)
    return l


trace_id = find_trace("CAS")
print(trace_id)

# print(keys)
# print(reqs)
