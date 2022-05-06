import os
from datetime import datetime
from Executer import *



class Watcher(object):
    def __init__(self,filename_arg):
        self.filename = filename_arg
        self._cached_stamp = 0
        self.count = 0
    def start_watch(self):
        print("[ My watch is start :) .. ] : "+datetime.now().strftime("%H:%M:%S"))
        while True:
            stamp = os.stat(self.filename).st_mtime
            if stamp != self._cached_stamp:
                self._cached_stamp = stamp
                self.count += 1
                # File has changed, so do something..
                if not self.count == 1:
                    print("[ file Update detected ] : "+datetime.now().strftime("%H:%M:%S"))
                    # ask user to run this file :
                    response = input("Rerun file ? (Y/N) ")
                    if response == 'Y':
                        print("run ........")
                        my_executer = Executer(self.filename.split('.')[1],self.filename)
                        my_executer.Run()
                    else:
                        print("don't run :) ")
        return
