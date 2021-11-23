import xml.etree.ElementTree as ET

tree = ET.parse("activity_7853524073.tcx")
root = tree.getroot()

print( root.tag)

# Using Namespaces
# https://docs.python.org/3/library/xml.etree.elementtree.html#parsing-xml-with-namespaces
ns =  { "ns":"http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2"}
for activities in root.findall("ns:Activities",ns):
    for act in activities:
        print( act.tag, act.attrib)

# Using XPath
# https://docs.python.org/3/library/xml.etree.elementtree.html#xpath-support
for lap in tree.findall("./ns:Activities/ns:Activity/ns:Lap",ns):
    print( lap.tag, lap.attrib)