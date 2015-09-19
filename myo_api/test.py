from myo_api import *

info_obj = get_myo_info_object()

while True:
    time.sleep(.2)
    print(info_obj.get('roll'))