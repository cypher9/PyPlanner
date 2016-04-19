'''
Created on 08.03.2016

@author: cypher9
'''
from src.info import Info
from src.functions import Functions


if __name__ == '__main__':
    info = Info()
    info.start_text()
    info.menu()
    eventlist = []
    function = Functions(eventlist)

    
options = {1 : function.add_event,
           2 : function.view_events
}        
        
try:
    option=int(raw_input('Option: '))
    options[option]()
except ValueError:
    print "Not a valid option" 