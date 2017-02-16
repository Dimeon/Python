import xml.etree.ElementTree as ET

tree = ET.parse('Eng8_SW_Tests.xml')
root = tree.getroot()

#for child in root:
 #   print(child.tag, child.attrib)

#print(root[0][0][0][0].text)

for preparation in root.findall('preparation'):
    teststep = preparation.find('teststep').text
    print(teststep)

findable = root.find('preparation')
for data in findable:
    print(data)