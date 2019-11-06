import xml.etree.ElementTree as ET


data = """  <stuff>
            <office>
                <person x="1">
                    <name>Chuck</name>
                    <phone type = "intl">+1 549 877 2054</phone>
                    <email hide = "yes" />
                </person>
                <person x= "2">
                    <name>Dan</name>
                    <phone type = "intl">+1 312 678 5792</phone>
                    <email hide = "yes" />
                </person>
            </office>
            </stuff>
            """

tree = ET.fromstring(data)
list_person = tree.findall('office/person')
print(len(list_person))

for person in list_person:
    print(person.find("name").text, person.find("phone").get("type"), person.find("phone").text)