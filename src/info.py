'''
Created on 06.03.2016

@author: cypher9
'''

class Info(object):
    '''
    Info of version and tool
    '''
    def start_text(self):
        print("PyPlanner v0.0.4-beta")
        print("--")
        print("PyPlanner is a simple commandline tool for keeping up with your appointments and events")
        print("PyPlanner encrypts your database with gpg to make your stuff really private ")
        print("\n")
        
    def help(self):
        print("help")
        
    def menu(self):
        print("\nSelect what you want to do")
        print("1 - Add an event")
        print("2 - Search")
        print("3 - View")
        print("4 - Delete")
        print("5 - Show calendar")
        print("0 - Quit")
        
    def submenu_view(self):
        print("\nSelect what you want to do")
        print("1 - View calendars")
        print("2 - View events")
        print("0 - Main Menu")
        
        return int(raw_input('Option: '))
        
    def submenu_delete(self):
        print("\nSelect what you want to do")
        print("1 - Delete calendar")
        print("2 - Delete event")
        print("0 - Main Menu")
        
        return int(raw_input('Option: '))
    
    def submenu_search(self):
        print("\nSelect what you want to do")
        print("1 - Search by string")
        print("2 - Search by date")
        print("0 - Main Menu")
        
        return int(raw_input('Option: '))
        