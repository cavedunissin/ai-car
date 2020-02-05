#!/usr/bin/env python3

import time
import requests

event_name = "Raspberry"
webhook_key = "lBWnRdYFOWNsn6mUXgthSl9gV0dP4te7S0cMW4_NO4u"

value1 = "Hello."
value2 = "I am RaspberryPi."
value3 = "Nice to meet you"

def IFTTT_post( value1,value2,value3 ):
        url_post = "https://maker.ifttt.com/trigger/" + event_name 
        url_post += "/with/key/" + webhook_key + "?value1=" + value1
        url_post += "&value2=" + value2 + "&value3=" + value3

        r = requests.get(url_post, headers = {"Host" : "maker.ifttt.com"})

        data = r.content.split()[:15]
        print ("data1"+str(data))
        data = r.content.split()
        print ("data2"+str(data))
        
        if data[0] == b"Congratulations!":
                print ("傳送成功")       
        else:      
                print (data)
          
def main():
        while True:
                try:
                        IFTTT_post(value1,value2,value3)
                        time.sleep(5)

                except KeyboardInterrupt:
                        print('使用者中斷')
                        break

if __name__ == '__main__':
    main()