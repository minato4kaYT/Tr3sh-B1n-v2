import os
from time import sleep as wait
import requests
import playsound
import webbrowser as wb
#^-- imports
while True:
    try:
        getsite = requests.get('https://google.com')#send request
    except requests.exceptions.ConnectionError:#if request bad
        print('Check wifi...')
        wait(10)
        pass
    else:#if request good
        for i in range(0,3):#play sound 3 times
            playsound.playsound('internet_true.mp3')
            wb.open_new_tab(getsite)
        break#end