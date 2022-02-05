import xml.etree.ElementTree as ET

xml_string = '''
<mobiles>
<mobile name="iphone">
<title>iphone</title>
<price>2000$s</price>
</mobile>
<mobile name="samsung">
<title>samsung</title>
<price>200$s</price>
</mobile>
</mobiles>

'''

tree = ET.fromstring(xml_string)
for x in tree:
    print(x.find('title').text)
    print(x.find('price').text)

#updating

for x in tree:
    title = x.find('title')
    if title.text == "iphone":
        title.text = "Iphone"
        # title.set("updated", "yes")

for x in tree:
    print(x.find('title').text)
    print(x.find('price').text)

#writing to a file
tree.write('new.xml')

#iterating over specific tags in the root
for x in tree.iter("price"):
    print(x.text)
