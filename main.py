'''
Created on 08.03.2016

@author: cypher9
'''
from src.info import Info
from src.functions import Functions
from src.xml_func import write_xml
from src.crypto import set_password,change_password
from os.path import isfile



if __name__ == '__main__':
    info = Info()
    info.start_text()
    function = Functions()
    if isfile('termine.enc'):
        function.xml_to_cal()
    else:
        set_password()
        write_xml("")
        
    
    
options = {1 : function.add_event,
           2 : info.submenu_search,
           3 : info.submenu_view,
           4 : info.submenu_delete,
           5 : function.print_calendar,
           6 : info.help,
           7 : change_password,
           0 : function.quit
}

suboptions_search = {1 : function.search_by_string,
                     2 : function.search_by_date,
                     0 : function.return_to_main
}

suboptions_view = {1 : function.show_calendars,
                   2 : function.show_events,
                   3 : function.show_next_event,
                   4 : function.show_timeframe,
                   0 : function.return_to_main,
}

suboptions_delete = {1 : function.delete_calendar,
                     2 : function.delete_event,
                     0 : function.return_to_main,
}  
        

while True:
    try:
        info.menu()            
        option=int(raw_input('Option: '))
        if option < 0 or option > 7:
            print ("\n...not a valid input...\n")
        else:
            if option == 2:
                sub_opt = options[option]()
                if sub_opt <  0 or sub_opt > 2:
                    print ("\n...not a valid input...\n")
                else:
                    suboptions_search[sub_opt]()   
            elif option == 3:
                sub_opt = options[option]()
                if sub_opt <  0 or sub_opt > 4:
                    print ("\n...not a valid input...\n")
                else:
                    suboptions_view[sub_opt]()
            elif option == 4:
                sub_opt = options[option]()
                if sub_opt <  0 or sub_opt > 2:
                    print ("\n...not a valid input...\n")
                else:
                    suboptions_delete[sub_opt]()
            elif option == 7:
                options[option]()
                function.save_cal_list()
            else:
                options[option]()
    except ValueError:
        print ("\n...not a valid input...\n")