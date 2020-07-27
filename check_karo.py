import time
import webbrowser

total_breaks = 10
break_count = 0

while(break_count < total_breaks):
    time.sleep(2100)
    webbrowser.open("https://www.youtube.com/watch?v=2We-WLbmMkc")
    break_count = break_count + 1


##import ctypes
##import time
##
##while True:
##    MessageBox = ctypes.windll.user32.MessageBoxA
##    MessageBox(None, '20 Minutes have passed, time to look away', 'Time to look away', 0)
##    time.sleep(10)
