import conf, json, time
from boltiot import Sms, Bolt
import json, time


mybolt = Bolt(conf.API_KEY, conf.DEVICE_ID)
sms = Sms(conf.SID, conf.AUTH_TOKEN, conf.TO_NUMBER, conf.FROM_NUMBER)


while True: 
    print ("Reading sensor value")
    response = mybolt.digitalRead('0') 
    data = json.loads(response) 
    response = sms.send_sms(" there is emergency in industry ")
