'''
Created on 14.03.2016

@author: Matthias
'''

from data import event

class File(object):
    '''
    classdocs
    '''
    event = ""
    def __init__(self):
        '''
        Constructor
        '''
        print "ich bin jetzt initialisiert"
        self.event = event.make_event("test", "event_description", "event_start_datetime", "event_end_datetime")
     
    def irgendwas(self):
        print(self.event.event_title)   