'''
Created on 07.03.2016

@author: cypher9
'''

class Event(object):
    '''
    classdocs
    '''
    event_title = ""
    event_description = ""
    event_start_datetime = ""
    event_end_datetime = ""

    def __init__(self, event_title, event_description, event_start_datetime, event_end_datetime):
        '''
        Constructor
        '''
        self.event_title = event_title
        self.event_description = event_description
        self.event_start_datetime = event_start_datetime
        self.event_end_datetime = event_end_datetime
        
class Calendar(object):
    calendar_title = ""
    
    def __init__(self, calendar_title, eventlist):
        self.calendar_title = calendar_title
        self.eventlist = eventlist
        
def make_event(event_title, event_description, event_start_datetime, event_end_datetime):
    event = Event(event_title, event_description, event_start_datetime, event_end_datetime)
    return event

def make_cal(calendar_title, eventlist):
    calendar = Calendar(calendar_title, eventlist)
    return calendar
