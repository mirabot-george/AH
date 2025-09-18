import numpy as np
import pyarrow as pa
from dora import Node
import mediapipe as mp
from scipy.spatial.transform import Rotation
import time

def main():

    node = Node()


    pa.array([])  # initialize pyarrow array


    t0=time.time()
    for event in node:

        event_type = event["type"]

        if event_type == "INPUT":
            event_id = event["id"]

            if event_id == "tick":
                elapsed=time.time()-t0
                s1_pitch=np.sin(2.0*np.pi*1.0*elapsed)*np.radians(10.0)+np.radians(10.0)
                s1_roll=np.cos(2.0*np.pi*1.0*elapsed)*np.radians(10.0)

                s2_pitch=np.sin(2.0*np.pi*1.0*elapsed)*np.radians(140.0/2.0)+np.radians(140.0/2.0)
                s4_pitch=np.sin(2.0*np.pi*1.0*elapsed)*np.radians((90.0+53.0)/2.0)+np.radians((90.0-53.0)/2.0)

                #舵机 0° => ~121.9° pitch 远端指节参照于手指轴
                #屈伸范围 (远端指节) [0°, 140°]
                #摆动范围 [-20°, 20°]

                tip1=Rotation.from_euler('XYZ',[s1_roll,s1_pitch,0.0])
                tip1=tip1.as_quat(scalar_first=True)


                # tip2=Rotation.from_euler('XYZ',[np.radians(10.0),np.radians(140.0),0.0]) #finger2 has a 10° roll offset
                tip2=Rotation.from_euler('XYZ',[np.radians(10.0),s2_pitch,0.0]) #finger2 has a 10° roll offset
                tip2=tip2.as_quat(scalar_first=True)



                # tip3=Rotation.from_euler('XYZ',[np.radians(20.0),np.radians(140.0),0.0]) #finger3 has a 20° roll offset
                tip3=Rotation.from_euler('XYZ',[np.radians(20.0),s2_pitch,0.0]) #finger3 has a 20° roll offset
                tip3=tip3.as_quat(scalar_first=True)


                # tip4=Rotation.from_euler('XYZ',[0.0,-np.pi/2.0,np.radians(20.0)]) #finger4 has a 20° yaw offset
                tip4=Rotation.from_euler('xyz',[0.0,-s4_pitch,np.radians(20.0)]) #finger4 has a 20° yaw offset

                tip4=tip4.as_quat(scalar_first=True)


                # tip2=[1,0,0,0]
                # tip3=[1,0,0,0]
                # tip4=[1,0,0,0]
                angles=[{'r_tip1': tip1,'r_tip2': tip2,'r_tip3': tip3,'r_tip4': tip4}]
                node.send_output('hand_quat',pa.array(angles))



        elif event_type == "ERROR":
            raise RuntimeError(event["error"])


if __name__ == "__main__":
    main()
