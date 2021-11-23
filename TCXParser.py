#
# Notes:
#    2021.11.23: Export [ time, distance, heart_rate, speed, cadence]
#

import xml.etree.ElementTree as ET

tree = ET.parse("activity_7853524073.tcx")
root = tree.getroot()

#print( root.tag)

# Using Namespaces
# https://docs.python.org/3/library/xml.etree.elementtree.html#parsing-xml-with-namespaces
ns =  { "ns": "http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2",
        "ns3":"http://www.garmin.com/xmlschemas/ActivityExtension/v2"}
for activities in root.findall("ns:Activities",ns):
    for act in activities:
        #print( act.tag, act.attrib)
        pass

# Using XPath
# https://docs.python.org/3/library/xml.etree.elementtree.html#xpath-support
for lap in tree.findall("./ns:Activities/ns:Activity/ns:Lap",ns):
    for track in lap.findall("ns:Track", ns):
        #print( track.tag)
        for tp in track.findall("ns:Trackpoint",ns):

            tp_time= tp.find("ns:Time", ns)

            tp_distance= tp.find("ns:DistanceMeters", ns)            

            tp_hrt= tp.find("ns:HeartRateBpm/ns:Value", ns)

            tp_speed= tp.find("ns:Extensions/ns3:TPX/ns3:Speed", ns)

            tp_cadence= tp.find("ns:Extensions/ns3:TPX/ns3:RunCadence", ns)

            print( "{0},{1},{2},{3},{4}".format(tp_time.text,tp_distance.text,tp_hrt.text,tp_speed.text,tp_cadence.text))