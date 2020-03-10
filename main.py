from pybleno import *
import sys
import signal
from services import *

bleno = Bleno()

primaryService = HPS_Service();

def onStateChange(state):
   print('on -> stateChange: ' + state);

   if (state == 'poweredOn'):
       bleno.startAdvertising('HPService', [primaryService.uuid]);
   else:
     bleno.stopAdvertising();
bleno.on('stateChange', onStateChange)

def onAdvertisingStart(error):
    print('on -> advertisingStart: ' + ('error ' + error if error else 'success'));

    if not error:
        def on_setServiceError(error):
            print('setServices: %s'  % ('error ' + error if error else 'success'))
            
        bleno.setServices([
            primaryService
        ], on_setServiceError)
bleno.on('advertisingStart', onAdvertisingStart)

bleno.start()

print ('Hit <ENTER> to disconnect')


if (sys.version_info > (3, 0)):
    while True:
        pass
else:
    raw_input()

bleno.stopAdvertising()
bleno.disconnect()

print ('terminated.')
sys.exit(1)
