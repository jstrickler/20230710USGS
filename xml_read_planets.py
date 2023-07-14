import lxml.etree as et

doc = et.parse('DATA/solar.xml')

#  doc.find()  doc.findall()   doc.getroot.findall()
#  elem.find()   elem()

for planet in doc.findall('.//planet'):
    name = planet.get('planetname')
    print(name)
    for moon in planet.findall('moon'):
        print(f"    {moon.text}")

mercury = doc.find('.//planet[@planetname="Mercury"]')
print(f"mercury: {mercury}")
et.SubElement(mercury, "moon").text = "Python"

doc.write('newsolar.xml', pretty_print=True, 
          xml_declaration=True)

