'''
Created on 06.03.2016

@author: cypher9
'''

import sys #for saveEvent

from datetime import datetime
from data.event import make_event
from xml.etree import ElementTree
from xml.dom import minidom
from xml.etree.ElementTree import Element, SubElement, Comment

class Functions(object):
    '''
    classdocs
    '''

    def prettify(self, elem):
        """
        Return a pretty-printed XML string for the Element.
        """
        rough_string = ElementTree.tostring(elem, 'utf-8')
        reparsed = minidom.parseString(rough_string)
        return reparsed.toprettyxml(indent="  ")

    
    def saveEvent(self, event):       
        try:   
            top = Element('event')
            
            child = SubElement(top, 'title')
            child.text = event.event_title
            
            child = SubElement(top, 'description')
            child.text = event.event_description.rstrip()
            
            child = SubElement(top, 'startdatetime')
            child.text = str(event.event_start_datetime)
            
            child = SubElement(top, 'enddatetime')
            child.text = str(event.event_end_datetime)
            
            xmlfile=open('termine.xml','a')
            xmlfile.write(self.prettify(top))
            xmlfile.write("\n")
            
            xmlfile.close
        except:
            print('Something went wrong! Can\'t tell what?')
            sys.exit(0) # quit Python
            
            
    def __init__(self, eventlist):
        self.eventlist = eventlist
        

    def add_event_to_list(self, event):
        self.eventlist.append(event)
    
    def view_events(self):
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
            self.saveEvent(make_event(event_title, event_description, event_start_datetime, event_end_datetime)) #make txt saveEvent
        except ValueError:
            print "Not a valid input..." 
               
        try:
            self.add_event_to_list(make_event(event_title, event_description, event_start_datetime, event_end_datetime))          
        except Exception:
            print "Error generating event..."