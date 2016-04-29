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
        print("Select what you want to do")
        print("1 - Add an event")
        print("2 - View my events")
        print("3 - Quit")