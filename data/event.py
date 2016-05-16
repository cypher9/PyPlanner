'''
Created on 07.03.2016

@author: cypher9
'''

class Event(object):
    '''
    classdocs
    '''
    event_calendar = ""
    event_title = ""
    event_description = ""
    event_start_datetime = ""
    event_end_datetime = ""

    def __init__(self, event_calendar, event_title, event_description, event_start_datetime, event_end_datetime):
        '''
        Constructor
        '''
        self.event_calendar = event_calendar
        self.event_title = event_title
        self.event_description = event_description
        self.event_start_datetime = event_start_datetime
        self.event_end_datetime = event_end_datetime
        
def make_event(event_calendar, event_title, event_description, event_start_datetime, event_end_datetime):
    event = Event(event_calendar, event_title, event_description, event_start_datetime, event_end_datetime)
    return event
