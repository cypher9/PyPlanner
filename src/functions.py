'''
Created on 06.03.2016

@author: cypher9
'''

import sys #for saveEvent
import calendar

from datetime import datetime
from operator import attrgetter
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
    
    def query_yes_no(self, question, default="yes"):
        valid = {"yes":True, "y":True, "ye":True,
                 "no":False, "n":False}
        if default is None:
            prompt = "[y/n]"
        elif default == "yes":
            prompt = "[Y/n]"
        elif default == "no":
            prompt = "[y/N]"
        else:
            raise ValueError("invalid default answer:'%s'" % default)
        
        while True:
            print(question + prompt)
            choice = raw_input().lower()
            if default is not None and choice == "":
                return valid[default]
            elif choice in valid:
                return valid[choice]
            else:
                print("Plese respond with 'yes' or 'no' (or 'y' or'n').\n")
    
    def xml_to_cal(self):
        '''
        writes all calendars from xml to eventlist
        '''
        try:
            self.cal_list = []
            xml_root = get_root()
            for cal in xml_root.findall('calendar'):
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
            print "failed to read xml...\nYour password may be incorrect!\nRestart PyPlanner and try again!"
            self.quit()
            
    def save_cal_list(self):
        create_xml(self.cal_list)
            
    def add_cal_to_list(self, cal):
        self.cal_list.append(cal) 
        
    def sort_list(self, eventlist):
        return sorted(eventlist, key=attrgetter('event_start_datetime'))
        
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
                self.add_cal_to_list(make_cal(event_calendar, self.sort_list(eventlist)))
            else:
                cal.eventlist.append(new_event)
                self.sort_list(cal.eventlist)
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
    
        
    def show_calendars(self):
        print("\nAvailable Calendars:")   
        if len(self.cal_list) < 1:
            print("There are no calendars to show! \nGo on and create one.")
        else:
            for cal in self.cal_list:
                print cal.calendar_title
        print "\n\n"   
    

    def show_events(self):
        cal_name = str(raw_input("\nSelect calendar: "))
        cal = self.first(cal for cal in self.cal_list if cal.calendar_title == cal_name)
        if cal is not None:
            if len(cal.eventlist) < 1:
                print("There are no events in this calendar! \nGo on and create one.")
            else:
                for event in cal.eventlist:
                    self.print_event(event)
        else:
            print("\n...no calendar found...\n")
            
    def show_next_event(self):
        next_event = None
        tmp_first = None
        for cal in self.cal_list:
            for event in cal.eventlist:
                if tmp_first is None:
                    tmp_first = event.event_start_datetime
                tmp_event = event.event_start_datetime
                if tmp_event <= tmp_first and tmp_event > datetime.now():
                    tmp_first = tmp_event
                    next_event = event
        if next_event is not None:
            self.print_event(next_event)
        else:
            print"\n...no upcoming events...\n"
            
    def show_timeframe(self):
        print("Enter the timeframe...")
        wrong_input = True
        while wrong_input:
            try:    
                start_date_frame = datetime.strptime(str(raw_input("Start(YYYY-MM-DD): ")), '%Y-%m-%d')
                wrong_input = False
            except ValueError:
                print("\n...incorrect date value...\n")
        wrong_input = True
        while wrong_input:
            try:    
                end_date_frame = datetime.strptime(str(raw_input("End(YYYY-MM-DD): ")), '%Y-%m-%d')
                wrong_input = False
            except ValueError:
                print("\n...incorrect date value...\n")
                
        for cal in self.cal_list:
            for event in cal.eventlist:
                if event.event_start_datetime.date() >= start_date_frame.date() and event.event_end_datetime.date() <= end_date_frame.date():
                    self.print_event(event) 
    
    def delete_calendar(self):
        cal_name = str(raw_input("\nSelect calendar: "))
        if self.query_yes_no("Do you really want to delete this calendar?", "no"):
            cal = self.first(cal for cal in self.cal_list if cal.calendar_title == cal_name)
            if cal is None:
                print "\n...no matching calendar found...\n"
            else:
                self.cal_list.remove(cal)
                create_xml(self.cal_list) 
                print "\n...calendar deleted...\n" 
            
    def delete_event(self):
        found = False
        event_name = str(raw_input("\nSelect event: "))
        if self.query_yes_no("Do you really want to delete this event?", "no"):
            for cal in self.cal_list:
                for event in cal.eventlist:
                    if event.event_title == event_name:
                        cal.eventlist.remove(event)
                        create_xml(self.cal_list)
                        print "\n...event deleted...\n"
                        found = True
                        break
                if found:
                    break
            if not found:
                print "\n...no matching event found...\n"
            
     
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