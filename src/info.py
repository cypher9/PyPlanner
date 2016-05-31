'''
Created on 06.03.2016

@author: cypher9
'''

class Info(object):
    '''
    Info of version and tool
    '''
    def start_text(self):
        print("PyPlanner v0.0.2-beta")
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
        print("3 - View calendars")
        print("4 - View my events")
        print("5 - Delete calendar")
        print("6 - Delete event")
        print("7 - Show calendar")
        print("0 - Quit")