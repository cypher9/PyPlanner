'''
Created on 06.03.2016

@author: cypher9
'''

import sys #for saveEvent
import calendar

from datetime import datetime
from data.event import make_event
from src.xml_func import get_root, create_xml

class Functions(object):
    '''
    classdocs
    '''   
    
    def __init__(self, eventlist):
        self.eventlist = eventlist
    
    def xml_to_event(self, cal_name):
        '''
        writes all events from the xml file in the eventlist
        '''
        try:
            root = get_root()
            cal = root.find(cal_name)
            if cal is None:
                print ("No calendar found!")
            else:
                for event in cal.findall('event'):
                    title = event.find('title').text
                    description= event.find('description').text
                    startdatetime = event.find('startdatetime').text
                    enddatetime = event.find('enddatetime').text
                    self.add_event_to_list(make_event(cal, title, description, startdatetime, enddatetime))   
        except:
            print "mistake while reading xml"    
        
        
    def view_calendars(self):
        print("Available Calendars:\n")
    
    def add_event_to_list(self, event):
        self.eventlist.append(event)
    
    def view_events(self):
        cal_name = str(raw_input("Select calendar: "))
        self.xml_to_event(cal_name)
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
            event_calendar = str(raw_input("Select calendar: "))
            new_event = make_event(event_calendar, event_title, event_description, event_start_datetime, event_end_datetime)
            create_xml(event_calendar, new_event)
            
        except ValueError:
            print "Not a valid input..." 
               
        try:
            self.add_event_to_list(new_event)          
        except Exception:
            print "Error generating event..."
            
     
    def print_calendar(self):
        year = int(input('Enter year: '))
        month = int(raw_input('Enter month (optional): ') or 0)
        
        if month is 0:
            print(calendar.TextCalendar().formatyear(year))
        else:
            print(calendar.month(year,month))
            
        
            
    def quit(self):
        sys.exit(0)