import xml.etree.ElementTree as ET

tree = ET.parse('my_xml.xml')
root = tree.getroot()
new_tag =  ET.fromstring("<mobile><title>Mega</title><price>1$</price></mobile>")
root.append(new_tag)
for x in root:
    title = x.find('title')
    if title.text == 'Nokia':
        root.remove(x)

for x in root:
    print(x.find('title').text)


