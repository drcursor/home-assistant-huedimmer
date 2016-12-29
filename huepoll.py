import time
from requests import get
import homeassistant.remote as remote

######## CONFIG ########
host = 'homeassistant.test'
urlhuebase = "http://HUEBRIDGEIP/api/USERNAME"
port = 8123
use_ssl = True
sensorid = '2'
pollingtime = 0.5
########################

def SensorState( SensorName ):
  tofind = "buttonevent\":"
  urlhue = urlhuebase + "/sensors/" + SensorName
  hueresponse = get(urlhue).text
  b = hueresponse.find(tofind) + len(tofind)
  e = hueresponse.find(",",b)
  state = hueresponse[b:e]
  return state

while 1 == 1:
  lastState = SensorState(sensorid)
  while (SensorState (sensorid) == lastState):
    time.sleep(pollingtime)
  state = SensorState(sensorid)
  button = state[0:1]
  print (button)
  action = None
#  if button == '1':
#    domain = 'scene'
#    switch_name = 'scene.watch_tv'
#    action = 'turn_on'
  if button == '2':
    domain = 'scene'
    switch_name = 'scene.dinner_time'
    action = 'turn_on'
  if button == '3':
    domain = 'scene'
    switch_name = 'scene.bed_time'
    action = 'turn_on'
#   if button == '4':
#    domain = 'light'
#    switch_name = 'light.light7'
#    action = 'turn_on'
  if action is not None:
    print(action)
    api = remote.API(host, port = port, use_ssl = use_ssl)
    remote.call_service(api, domain, action, {'entity_id': '{}'.format(switch_name)})
