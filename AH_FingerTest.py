import time
import numpy as np
import serial

from rustypot import Scs0009PyController


ID_1 = 17 #更改为待校准的舵机ID 
ID_2 = 18 #更改为待校准的舵机ID 
MiddlePos_1 =5 #舵机ID_1的中间位置 
MiddlePos_2 =5 #舵机ID_2的中间位置



c = Scs0009PyController(
        serial_port="COM9", #注意修改为实际端口
        baudrate=1000000,
        timeout=0.5,
    )

def main():
    
    try:
        c.write_torque_enable(ID_1, 1)
        c.write_torque_enable(ID_2, 1)
    except Exception as e:
        print(f"使能扭矩失败: {e}")
        return    

    #c.write_torque_enable(1, 1) 
    #1 = On / 2 = Off / 3 = Free
    
    while True:
        

        CloseFinger()
        time.sleep(3)


        OpenFinger()
        time.sleep(1)

        #c.sync_write_raw_goal_position([1,2], [50,50])
        #time.sleep(1)

        #a=c.read_present_position(1)
        #b=c.read_present_position(2)
        #a=np.rad2deg(a)
        #b=np.rad2deg(b)
        #print(f'{a} {b}')
        #time.sleep(0.001)


def CloseFinger ():
    
    c.write_goal_speed(ID_1, 6) # 设定舵机ID_1的速度为6 => Max Speed
    c.write_goal_speed(ID_2, 6) # 设定舵机ID_2的速度为6 => Max Speed
    Pos_1 = np.deg2rad(MiddlePos_1+90)
    Pos_2 = np.deg2rad(MiddlePos_2-90)
    c.write_goal_position(ID_1, Pos_1)
    c.write_goal_position(ID_2, Pos_2)
    time.sleep(0.01)


def OpenFinger():
    c.write_goal_speed(ID_1, 6) # 设定舵机ID_1的速度为6 => Max Speed
    c.write_goal_speed(ID_2, 6) # 设定舵机ID_2的速度为6 => Max Speed
    Pos_1 = np.deg2rad(MiddlePos_1-30)
    Pos_2 = np.deg2rad(MiddlePos_2+30)
    c.write_goal_position(ID_1, Pos_1)
    c.write_goal_position(ID_2, Pos_2)
    time.sleep(0.01)






if __name__ == '__main__':
    main()


