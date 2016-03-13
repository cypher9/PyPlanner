'''
Created on 06.03.2016

@author: cypher9
'''
from src.functions import Functions

class pyplanner_menu(object):
    '''
    menu of PyPlanner
    '''
    def add(self):
        self.functions.add_event()
 
    def view(self):
        self.functions.view_events()
    
    options = {1 : add,
               2 : view,                   
    }
    
    def __init__(self, option):
        '''
        Constructor
        '''
        self.functions = Functions()
        self.option = option
        self.menu_select(self.options)   
    

    def menu_select(self, options):  
        options[self.option](self)
        
    