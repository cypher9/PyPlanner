'''
Created on 06.03.2016

@author: cypher9
'''

import sys #for saveEvent

from datetime import datetime
from data.event import make_event
from xml.etree import ElementTree
from xml.dom import minidom
from xml.etree.ElementTree import Element, SubElement
import xml.etree.ElementTree as ET
from _elementtree import tostring

class Functions(object):
    '''
    classdocs
    '''
    def xml_to_event(self):
        '''
        writes all events from the xml file in the eventlist
        '''
        try:
            tree = ET.parse('termine.xml')
            root = tree.getroot()
            #print(str(root))
            for event in root.findall('event'):
                title = event.find('title').text
                description= event.find('description').text
                startdatetime = event.find('startdatetime').text
                enddatetime = event.find('enddatetime').text
                self.add_event_to_list(make_event(title, description, startdatetime, enddatetime))
                
            
        except:
            print "mistake while reading xml"    
    def prettify(self, elem):
        """
        Return a pretty-printed XML string for the Element.
        """
        rough_string = ElementTree.tostring(elem, 'utf-8')
        reparsed = minidom.parseString(rough_string)
        return reparsed.toprettyxml(indent="  ")
    
    def xmlappend(self,event):
        '''
        event to xml format 
        '''
        try:
            tree = ET.parse('termine.xml')
            root = tree.getroot()

            b = ET.SubElement(root, 'event')
            
            child = ET.SubElement(b, 'title')
            child.text= event.event_title
        
            child = ET.SubElement(b, 'description')
            child.text= event.event_description.rstrip()
        
            child = ET.SubElement(b, 'startdatetime')
            child.text= str(event.event_start_datetime)
        
            child = ET.SubElement(b, 'enddatetime')
            child.text= str(event.event_end_datetime)
        
        
            xmlfile=open('termine.xml','w')
            l=tostring(root)
            xmlfile.write(l)     
            xmlfile.close
        except: 
            #if there is no xml file...
            self.makeXML(event)
        
    def makeXML(self, event):     
        '''
        create new, empty xml file and writes the first event 
        '''  
        try:   
            root = Element('planner')
            
            top = SubElement(root, 'event')
            
            child = SubElement(top, 'title')
            child.text = event.event_title
            
            child = SubElement(top, 'description')
            child.text = event.event_description.rstrip()
            
            child = SubElement(top, 'startdatetime')
            child.text = str(event.event_start_datetime)
            
            child = SubElement(top, 'enddatetime')
            child.text = str(event.event_end_datetime)
            
            xmlfile=open('termine.xml','a')
            l=tostring(root)
            xmlfile.write(l)
            
            
            xmlfile.close
        except:
            print('Something went wrong! Can\'t tell what?')
            sys.exit(0) # quit Python
            
            
    def __init__(self, eventlist):
        self.eventlist = eventlist
        

    def add_event_to_list(self, event):
        self.eventlist.append(event)
    
    def view_events(self):
        self.xml_to_event()
        for event in self.eventlist:
            print("\nTitle: " + event.event_title + "\n")
            print("Description: " + event.event_description)
            print("Start Datetime: " + str(event.event_start_datetime))
            print("End Datetime: " + str(event.event_end_datetime) + "\n") 
            
    def add_event(self):
        print("Add your event details:\n")
        try:
            event_title=str(raw_input('Title: '))
            event_description = ""
            stopword = ""
            first = True
            while True:
                if first:
                    line = raw_input('Description: ')
                    first = False
                else:
                    line = raw_input()
                if line.strip() == stopword:
                    break
                event_description += "%s\n" % line
            event_start_date = str(raw_input("Startdate(YYYY-MM-DD): "))
            event_start_time = str(raw_input("Starttime(HH:MM)24h: "))
            event_end_date = str(raw_input("Enddate(YYYY-MM-DD): "))
            event_end_time = str(raw_input("Endtime(HH:MM)24h: "))
            event_start_datetime = datetime.strptime(event_start_date + ' ' + event_start_time, '%Y-%m-%d %H:%M')
            event_end_datetime = datetime.strptime(event_end_date + ' ' + event_end_time, '%Y-%m-%d %H:%M')
            self.xmlappend(make_event(event_title, event_description, event_start_datetime, event_end_datetime))
            #self.makeXML(make_event(event_title, event_description, event_start_datetime, event_end_datetime)) #make txt saveEvent
        except ValueError:
            print "Not a valid input..." 
               
        try:
            self.add_event_to_list(make_event(event_title, event_description, event_start_datetime, event_end_datetime))          
        except Exception:
            print "Error generating event..."
            
            
    def quit(self):
        sys.exit()