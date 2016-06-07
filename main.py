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
           2 : info.submenu_search,
           3 : info.submenu_view,
           4 : info.submenu_delete,
           5 : function.print_calendar,
           6 : info.help,
           0 : function.quit
}

suboptions_search = {1 : function.search_by_string,
                     2 : function.search_by_date,
                     0 : function.return_to_main
}

suboptions_view = {1 : function.view_calendars,
                   2 : function.view_events,
                   0 : function.return_to_main,
}

suboptions_delete = {1 : function.delete_calendar,
                     2 : function.delete_event,
                     0 : function.return_to_main,
}  
        
try:
    while True:
        info.menu()
        function.xml_to_cal()
        option=int(raw_input('Option: '))
        if option < 0 or option > 6:
            print("\n...wrong input...\n")
        else:
            if option == 2:
                sub_opt = options[option]()
                if sub_opt <  0 or sub_opt > 2:
                    print("\n...wrong input...\n")
                else:
                    suboptions_search[sub_opt]()
                
            elif option == 3:
                sub_opt = options[option]()
                if sub_opt <  0 or sub_opt > 2:
                    print("\n...wrong input...\n")
                else:
                    suboptions_view[sub_opt]()
            elif option == 4:
                sub_opt = options[option]()
                if sub_opt <  0 or sub_opt > 2:
                    print("\n...wrong input...\n")
                else:
                    suboptions_delete[sub_opt]()
            else:
                options[option]()
except ValueError:
    print "Not a valid option" 