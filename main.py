'''
Created on 08.03.2016

@author: cypher9
'''
from src.info import Info
from src import functions


if __name__ == '__main__':
    info = Info()
    info.start_text()
    info.menu()

    
options = {1 : functions.add_event,                   
}        
        
try:
    option=int(raw_input('Option: '))
    options[option]()
except ValueError:
    print "Not a valid option" 