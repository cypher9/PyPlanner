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

def set_calname(cal_name, xml_root):
    xml_calname = ET.SubElement(xml_root, 'calendar')
    xml_calname.set('name', cal_name)
    
    return xml_calname
   

def create_xml(cal_name, event = None):
    xml_root = None
    xml_calname = None
    try:
        if os.path.isfile("termine.xml"):
            xml_root = get_root()  
                
            for cal in xml_root.findall('calendar'):
                if cal.attrib['name'] == cal_name:
                    xml_calname = cal
                    break
    
            if xml_calname is None:
                xml_calname = set_calname(cal_name, xml_root)
                
        else:
            xml_root = ET.Element('planner')
            xml_calname = set_calname(cal_name, xml_root)
        
        xml_event = ET.SubElement(xml_calname, 'event')
        
        if event is not None:
            xml_event.set('title', event.event_title)
            xml_event.set('description', event.event_description)
            xml_event.set('startdatetime', str(event.event_start_datetime))
            xml_event.set('enddatetime', str(event.event_end_datetime))
    
        doc=tostring(xml_root)
        write_xml(doc)

    except:
        print("Error writing file!")
        
        
    