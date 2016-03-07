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
    event_start_date = ""
    event_end_date = ""
    event_start_time = ""
    event_end_time = ""

    def __init__(self, event_title, event_description, event_start_date, event_end_date,
                  event_start_time, event_end_time):
        '''
        Constructor
        '''
        self.event_title = event_title
        self.event_description = event_description
        self.event_start_date = event_start_date
        self.event_end_date = event_end_date
        self.event_start_time = event_start_time
        self.event_end_time = event_end_time
        
def make_event(event_title, event_description, event_start_date, event_end_date,
                  event_start_time, event_end_time):
    event = Event(event_title, event_description, event_start_date, event_end_date,
                  event_start_time, event_end_time)
    return event
