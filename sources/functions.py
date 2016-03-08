'''
Created on 06.03.2016

@author: cypher9
'''
from datetime import datetime
from event import make_event

class Functions(object):
    '''
    functions for PyPlanner
    '''

    def __init__(self):
        '''
        Constructor
        '''
     
    def add_event(self):
        print("Add your event details:\n")
        try:
            event_title=str(raw_input('Title: '))
            event_description = ""
            stopword = ""
            while True:
                line = raw_input('Description: ')
                if line.strip() == stopword:
                    break
                event_description += "%s\n" % line
            event_start_date = str(raw_input("Startdate(YYYY-MM-DD: "))
            event_start_time = str(raw_input("Starttime(HH:MM)24h: "))
            event_end_date = str(raw_input("Startdate(YYYY-MM-DD: "))
            event_end_time = str(raw_input("Endtime(HH:MM)24h: "))
            event_start_datetime = datetime.strptime(event_start_date + ' ' + event_start_time, '%Y-%m-%d %H:%M')
            event_end_datetime = datetime.strptime(event_end_date + ' ' + event_end_time, '%Y-%m-%d %H:%M')
        except ValueError:
            print "Not a valid option" 
            
        try:
            make_event(event_title, event_description, event_start_datetime, event_end_datetime)
        except Exception:
            print "Error writing "