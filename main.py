from Wather import *
import sys



if __name__ == '__main__':
    try:
        my_file = sys.argv[1]
        my_watcher = Watcher(my_file)
        my_watcher.start_watch()
    except  Exception as e:
        print("[ Watcher Error ]:  "+str(e))
    