'''
Created on 06.03.2016

@author: cypher9
'''
from datetime import datetime

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
                line = raw_input()
                if line.strip() == stopword:
                    break
                event_description += "%s\n" % line
            event_start_date = datetime.strptime(raw_input("Startdate(YYYY-MM-DD: "), '%Y-%m-%d')
            event_start_date = datetime.strptime(raw_input("Startdate(YYYY-MM-DD: "), '%Y-%m-%d')
        except ValueError:
            print "Not a valid option"   