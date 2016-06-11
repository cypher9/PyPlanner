'''
Created on 06.03.2016

@author: cypher9
'''

import sys #for saveEvent
import calendar

from datetime import datetime
from src.cal import make_event, make_cal
from src.xml_func import get_root, create_xml

class Functions(object):
    '''
    classdocs
    '''   
    cal_list = []
        
    def first(self, iterabel, default = None):
        for item in iterabel:
            return item
        return default
    
    def print_event(self, event):
        print("\n**************************")
        print("Title: " + event.event_title)
        print("Description: " + event.event_description)
        print("Start Datetime: " + str(event.event_start_datetime))
        print("End Datetime: " + str(event.event_end_datetime))
        print("**************************")
    
    def xml_to_cal(self):
        '''
        writes all calendars from xml to eventlist
        '''
        try:
            self.cal_list = []
            xml_root = get_root()
            for cal in xml_root.findall('cal'):
                if cal is None:
                    break
                else:
                    eventlist = []
                    xml_calname = cal.attrib['name']
                    for event in cal.findall('event'):
                        xml_event = event
                        if xml_event is None:
                            break
                        else:
                            title = event.attrib['title']
                            description= event.attrib['description']
                            startdatetime = datetime.strptime(str(event.attrib['startdatetime']), '%Y-%m-%d %H:%M:%S')
                            enddatetime = datetime.strptime(event.attrib['enddatetime'], '%Y-%m-%d %H:%M:%S')
                            eventlist.append(make_event(title, description, startdatetime, enddatetime))
                self.add_cal_to_list(make_cal(xml_calname, eventlist)) 
        except:
            print "failed to read xml...\nYour password may be incorrect!\nRestart Pyplanner and try again!"
            self.quit()
            
    def save_cal_list(self):
        create_xml(self.cal_list)
            
    def add_cal_to_list(self, cal):
        self.cal_list.append(cal) 
        
    def add_event(self):
        print("\nAdd your event details:\n")
        wrong_input = True
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
            
            while wrong_input:
                try:    
                    event_start_date = str(raw_input("Startdate(YYYY-MM-DD): "))
                    datetime.strptime(event_start_date, '%Y-%m-%d')
                    wrong_input = False
                except ValueError:
                    print("\n...incorrect date value...\n")
            
            wrong_input = True                
            while wrong_input:
                try:    
                    event_start_time = str(raw_input("Starttime(HH:MM)24h: "))
                    datetime.strptime(event_start_date + " " + event_start_time, '%Y-%m-%d %H:%M')
                    wrong_input = False
                except ValueError:
                    print("\n...incorrect time value...\n")
            
            wrong_input = True
            while wrong_input:
                try:    
                    event_end_date = str(raw_input("Enddate(YYYY-MM-DD): "))
                    datetime.strptime(event_end_date, '%Y-%m-%d')
                    wrong_input = False
                except ValueError:
                    print("\n...incorrect date value...\n")
                    
            wrong_input = True                
            while wrong_input:
                try:    
                    event_end_time = str(raw_input("Endtime(HH:MM)24h: "))
                    datetime.strptime(event_end_date + " " + event_end_time, '%Y-%m-%d %H:%M')
                    wrong_input = False
                except ValueError:
                    print("\n...incorrect time value...\n")
            
            
            event_start_datetime = datetime.strptime(event_start_date + ' ' + event_start_time, '%Y-%m-%d %H:%M')
            event_end_datetime = datetime.strptime(event_end_date + ' ' + event_end_time, '%Y-%m-%d %H:%M')
            event_calendar = str(raw_input("Select cal: "))
            new_event = make_event(event_title, event_description, event_start_datetime, event_end_datetime)
            
            cal = self.first(cal for cal in self.cal_list if cal.calendar_title == event_calendar)
            if cal is None:
                eventlist = []
                eventlist.append(new_event)
                self.add_cal_to_list(make_cal(event_calendar, eventlist))
            else:
                cal.eventlist.append(new_event)
            self.save_cal_list()
            
            print("\n...event saved...\n\n") 
            
        except ValueError:
            print "\nError generating event...\n" 
               
                    

    def search_by_string(self):
        search_str = str(raw_input("\nPlease enter search term: "))
        found = False
        print"\n"
        for cal in self.cal_list:
            if search_str in cal.calendar_title:
                print "Calendar: " + cal.calendar_title
                found = True
                
            for event in cal.eventlist:
                if (search_str in event.event_title) or (search_str in event.event_description) :
                    self.print_event(event)
                    found = True
        
        if not found:
            print "There are no matches for your search!" 
            
    def search_by_date(self):
        search_date = str(raw_input("\nPlease enter date(YYYY-MM-DD): "))
        found = False
        for cal in self.cal_list:
            for event in cal.eventlist:
                if search_date == str(event.event_start_datetime.date()):
                    self.print_event(event)
                    found = True                    
        
        if not found:
            print "There are no matches for your search!"               
    
        
    def view_calendars(self):
        print("\nAvailable Calendars:")
        for cal in self.cal_list:   
            if cal is None:
                print("There are no calendars to show! \n Go on and create one.")
            else:
                print cal.calendar_title
        print "\n\n"   
    

    def view_events(self):
        cal_name = str(raw_input("\nSelect cal: "))
        cal = self.first(cal for cal in self.cal_list if cal.calendar_title == cal_name)
        if cal is not None:
            for event in cal.eventlist:
                self.print_event(event)
        else:
            print("No cal found!\n\n")
            
    
    def delete_calendar(self):
        cal_name = str(raw_input("\nSelect cal: "))
        cal = self.first(cal for cal in self.cal_list if cal.calendar_title == cal_name)
        if cal is None:
            print "no matching cal found..."
        else:
            self.cal_list.remove(cal)
            create_xml(self.cal_list) 
            print "...cal deleted..." 
            
    def delete_event(self):
        found = False
        event_name = str(raw_input("\nSelect event: "))
        for cal in self.cal_list:
            for event in cal.eventlist:
                if event.event_title == event_name:
                    cal.eventlist.remove(event)
                    create_xml(self.cal_list)
                    print "...event deleted..."
                    found = True
                    break
            if found:
                break
        if not found:
            print "no matching event found..."
            
     
    def print_calendar(self):
        year = int(input('\nEnter year: '))
        month = int(raw_input('Enter month (optional): ') or 0)
        
        if month is 0:
            print(calendar.TextCalendar().formatyear(year))
        else:
            print(calendar.month(year,month))
            
        
    def return_to_main(self):
        return 0       
    def quit(self):
        sys.exit(0)