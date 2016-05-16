'''
Created on 29.04.2016

@author: cypher9
'''
import os.path

from xml.etree.ElementTree import Element, SubElement
import xml.etree.ElementTree as ET
from _elementtree import tostring
 
def write_xml(xml_doc):
    xmlfile=open('termine.xml','w')
    xmlfile.write(xml_doc)     
    xmlfile.close

def get_root():
    return ET.parse('termine.xml').getroot()

def create_xml(event):
    xml_root = None
    xml_top = None
    try:
        if os.path.isfile("termine.xml"):
            xml_root = get_root()
            xml_top = ET.SubElement(xml_root, 'event')
        else:
            xml_root = Element('planner')
            xml_top = SubElement(xml_root, 'event')
        
        child = ET.SubElement(xml_top, 'title')
        child.text= event.event_title
    
        child = ET.SubElement(xml_top, 'description')
        child.text= event.event_description.rstrip()
    
        child = ET.SubElement(xml_top, 'startdatetime')
        child.text= str(event.event_start_datetime)
    
        child = ET.SubElement(xml_top, 'enddatetime')
        child.text= str(event.event_end_datetime)
    
        doc=tostring(xml_root)
        write_xml(doc)

    except:
        print("Error writing file!")
        
        
    