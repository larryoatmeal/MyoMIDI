import myo as libmyo
libmyo.init()
import threading
import copy
import thread
import time
import math

TIME_PER_UPDATE = 0.1 # seconds

# Poses
FIST = 0
REST = 1
DOUBLE_TAP = 2
WAVE_OUT = 3
WAVE_IN = 4
FINGERS_SPREAD = 5

'''
 Get-able Values:
    pose
    roll
    pitch
    yaw
    acceleration_x
    acceleration_y
    acceleration_z
    angular_velocity_x
    angular_velocity_y
    angular_velocity_z
'''



def get_myo_info_object():

    info_object = _Listener()
    _start_data_gathering_thread(info_object)

    return info_object

def _start_data_gathering_thread(info_object):

    hub = libmyo.Hub()
    hub.set_locking_policy(libmyo.locking_policy.none)
    hub.run(1000, info_object)

    def update_info(hub, info_object, TIME_PER_UPDATE):
        try:
            while hub.running:
                time.sleep(TIME_PER_UPDATE)
                if info_object.done:
                    break

        except KeyboardInterrupt:
            info_object.shutdown()

        finally:
            info_object.shutdown()
            hub.shutdown()

    try:
        thread.start_new_thread(
            update_info, (
                hub,
                info_object,
                TIME_PER_UPDATE
            )
        )

    except:
        # Unable to start thread
        info_object.shutdown()

class _Listener(libmyo.DeviceListener):

    def __init__(self):
        self._reset_values()
        self.done = False
        self.locks = {k: threading.Lock() for k in self.values}
        self.lastGesture = None
    def getLastGesture(self):
        gesture = self.lastGesture
        self.lastGesture = None
        return gesture
    def get(self, key):
        if key not in self.values.keys():
            raise InputError('Key does not exist')

        self.locks[key].acquire()
        value = self.values[key]
        self.locks[key].release()

        return value

    def shutdown(self):
        self.done = True

    def on_pose(self, myo, timestamp, pose):
        if pose == libmyo.pose.rest:
            self.values['pose'] = REST
        elif pose == libmyo.pose.fist:
            self.values['pose'] = FIST
            self.lastGesture = FIST
        elif pose == libmyo.pose.wave_in:
            self.values['pose'] = WAVE_IN
            self.lastGesture = WAVE_IN
        elif pose == libmyo.pose.wave_out:
            self.values['pose'] = WAVE_OUT
            self.lastGesture = WAVE_OUT
        elif pose == libmyo.pose.fingers_spread:
            self.values['pose'] = FINGERS_SPREAD
            self.lastGesture = FINGERS_SPREAD
        elif pose == libmyo.pose.double_tap:
            self.values['pose'] = DOUBLE_TAP
            self.lastGesture = DOUBLE_TAP

    def on_orientation_data(self, myo, timestamp, orientation):
        x = orientation.x
        y = orientation.y
        z = orientation.z
        w = orientation.w

        # Calculate and set values to be in range [0, 1]
        roll =  (math.atan2(2*y*w - 2*x*z, 1 - 2*y*y - 2*z*z)/math.pi+1)/2
        pitch = (math.atan2(2*x*w - 2*y*z, 1 - 2*x*x - 2*z*z)/math.pi+1)/2
        yaw =   (math.asin(2*x*y + 2*z*w)/(math.pi/2)+1)/2

        self.values['roll'] =  roll
        self.values['pitch'] = pitch
        self.values['yaw'] =   yaw

    def on_accelerometor_data(self, myo, timestamp, acceleration):
        self.values['acceleration_x'] = acceleration.x
        self.values['acceleration_y'] = acceleration.y
        self.values['acceleration_z'] = acceleration.z

    def on_gyroscope_data(self, myo, timestamp, gyroscope):
        pass
        # def fit_from_0_to_1(x):
        #     hopefully_good_val = math.log(abs(x))/7.0*math.copysign(1.0, x)+7.0
        #     if hopefully_good_val > 1:
        #         print "shit"
        #         return 1
        #     if hopefully_good_val < 0:
        #         return 0
        #     return hopefully_good_val
        # self.values['angular_velocity_x'] = fit_from_0_to_1(gyroscope.x)
        # self.values['angular_velocity_y'] = fit_from_0_to_1(gyroscope.y)
        # self.values['angular_velocity_z'] = fit_from_0_to_1(gyroscope.z)

    def _reset_values(self):
        self.values = {
            'pose':               REST,
            'roll':               0,
            'pitch':              0,
            'yaw':                0,
            'acceleration_x':     0,
            'acceleration_y':     0,
            'acceleration_z':     0,
            'angular_velocity_x': 0,
            'angular_velocity_y': 0,
            'angular_velocity_z': 0,
        }

    '''

    def on_event(self, kind, event):
        """
        Called before any of the event callbacks.
        """

    def on_event_finished(self, kind, event):
        """
        Called after the respective event callbacks have been
        invoked. This method is *always* triggered, even if one of
        the callbacks requested the stop of the Hub.
        """

    def on_pair(self, myo, timestamp, firmware_version):
        pass

    def on_unpair(self, myo, timestamp):
        pass

    def on_connect(self, myo, timestamp, firmware_version):
        pass

    def on_disconnect(self, myo, timestamp):
        pass

    def on_arm_sync(self, myo, timestamp, arm, x_direction, rotation,
                    warmup_state):
        pass

    def on_arm_unsync(self, myo, timestamp):
        pass

    def on_unlock(self, myo, timestamp):
        pass

    def on_lock(self, myo, timestamp):
        pass

    def on_rssi(self, myo, timestamp, rssi):
        pass

    def on_battery_level_received(self, myo, timestamp, level):
        pass

    def on_emg_data(self, myo, timestamp, emg):
        pass

    def on_warmup_completed(self, myo, timestamp, warmup_result):
        pass

    '''