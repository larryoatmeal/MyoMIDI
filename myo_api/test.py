from myo_api import *
import math

info_obj = get_myo_info_object()

while True:
    time.sleep(.2)
    print "angular_velocity_x", info_obj.get('angular_velocity_x')
    print "angular_velocity_y", info_obj.get('angular_velocity_y')
    print "angular_velocity_z", info_obj.get('angular_velocity_z')