'''
Created on 08.03.2016

@author: cypher9
'''
from info import Info
from menu import pyplanner_menu


if __name__ == '__main__':
    info = Info()
    info.start_text()
    info.menu()

    try:
        option=int(raw_input('Option: '))
    except ValueError:
        print "Not a valid option" 
        
    menu_option = pyplanner_menu(option)
    pass