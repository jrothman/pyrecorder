import time
import pyautogui
import codecs
import datetime
import sys
import os
import ctypes
from win10toast import ToastNotifier

SLEEPTIME = 60

if __name__ == '__main__':
    i = 0
    toaster = ToastNotifier()
    today = datetime.datetime.now()
    toaster.show_toast("INFO", f"{today}: PyRecorder started... ", duration=10)
    print(f"{today}: PyRecorder started...")
    f = None
    path = os.environ['HOMEPATH'] + "\\Documents\\_pyrecordings\\"
    while True:
        today = datetime.datetime.now()
        try:
            fw = pyautogui.getActiveWindow()
            d = '{:02d}'.format(today.day)
            m = '{:02d}'.format(today.month)
            y = '{:02d}'.format(today.year)

            filename = path+y+'-'+m+'-pyrecorder.csv'

            with codecs.open(filename, 'a+', 'UTF-8') as f:
                f.write(str(today)+',|'+fw.title+'\n')
            f.close()
            time.sleep(SLEEPTIME)
        except IOError:
            type, value, traceback = sys.exc_info()
            filename = path+'pyrecorder-ERRORS.csv'
            f = open(filename, "a")
            f.write("{}: IO Error: {}".format(today,str(value)))
            f.close()
            # message_box = ctypes.windll.user32.MessageBoxW
            # message_box(None, 'Error:'+value.strerror, 'PyRecorder Error', 0)
            print(f"{today}: PyRecorder had an IO Error!")
            toaster.show_toast("ERROR", f"{today}: PyRecorder had an IO Error! ", duration=10)

            time.sleep(SLEEPTIME)
        except Exception as e:
            type, value, traceback = sys.exc_info()
            filename = path + 'pyrecorder-ERRORS.csv'
            f = open(filename, "a")
            f.write("{}: Exception: {}".format(today,str(value)))
            f.close()
            # message_box = ctypes.windll.user32.MessageBoxW
            # message_box(None, 'Error:'+value.strerror, 'PyRecorder Error', 0)
            toaster.show_toast("ERROR", f"{today}: PyRecorder had an Unknown Error!", duration=10)
            print(f"{today}: PyRecorder had an Unknown Error!")
            time.sleep(SLEEPTIME)
        finally:
            if f:
                f.close()
