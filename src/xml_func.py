'''
Created on 29.04.2016

@author: cypher9
'''
import os.path

import xml.etree.ElementTree as ET
from _elementtree import tostring
 
def write_xml(xml_doc):
    xmlfile=open('termine.xml','w')
    xmlfile.write(xml_doc)     
    xmlfile.close
        
        

def get_root():
    return ET.parse('termine.xml').getroot()

def create_xml(cal_name, event = None):
    xml_root = None
    xml_event = None
    try:
        if os.path.isfile("termine.xml"):
            xml_root = get_root()
            xml_calname = ET.Element.find(xml_root, cal_name)
            if xml_calname is None:
                xml_calname = ET.SubElement(xml_root, cal_name)
            xml_event = ET.SubElement(xml_calname, 'event')
        else:
            xml_root = ET.Element('planner')
            xml_calname = ET.SubElement(xml_root, cal_name)
            xml_event = ET.SubElement(xml_calname, 'event')
        if event is not None:
            child = ET.SubElement(xml_event, 'title')
            child.text= event.event_title
        
            child = ET.SubElement(xml_event, 'description')
            child.text= event.event_description.rstrip()
        
            child = ET.SubElement(xml_event, 'startdatetime')
            child.text= str(event.event_start_datetime)
        
            child = ET.SubElement(xml_event, 'enddatetime')
            child.text= str(event.event_end_datetime)
    
        doc=tostring(xml_root)
        write_xml(doc)

    except:
        print("Error writing file!")
        
        
    