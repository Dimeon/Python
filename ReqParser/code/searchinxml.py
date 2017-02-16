import xml.etree.ElementTree as ET
tree = ET.parse('country_data.xml')
root = tree.getroot()

for child in root:
    print(child.tag, child.attrib)

print(root[1][0].text)

for neighbor in root.iter('neighbor'):
    print(neighbor.attrib)

for country in root.findall('country'):
    rank = country.find('rank').text
    name = country.get('name')
    print(name, rank)