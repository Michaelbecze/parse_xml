from lxml import etree as ET

stream = open('Sample.xml', 'r')

xml = ET.parse(stream)

root = xml.getroot()

for f in root:
    print(ET.tostring(f))
    print("")