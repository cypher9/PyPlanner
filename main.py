'''
Created on 08.03.2016

@author: cypher9
'''
from src.info import Info
from src.functions import Functions


if __name__ == '__main__':
    info = Info()
    info.start_text()
    function = Functions()
    
    
options = {1 : function.add_event,
           2 : function.view_calendars,
           3 : function.view_events,
           4 : function.print_calendar,
           5 : function.quit
}
        
try:
    while True:
        info.menu()
        function.xml_to_cal()
        option=int(raw_input('Option: '))
        options[option]()
except ValueError:
    print "Not a valid option" 