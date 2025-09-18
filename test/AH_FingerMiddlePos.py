import time
import numpy as np

from rustypot import Scs0009PyController


ID_1 = 17 #更改为待校准的舵机ID 
ID_2 = 18 #更改为待校准的舵机ID 
MiddlePos_1 = 0 #舵机ID_1的中间位置 
MiddlePos_2 = 0 #舵机ID_2的中间位置


c = Scs0009PyController(
        serial_port="COM9",
        baudrate=1000000,
        timeout=0.5,
    )

def main():
    

    c.write_torque_enable(ID_1, 1) 
    c.write_torque_enable(ID_2, 1) 
    #1 = On / 2 = Off / 3 = Free
    
    while True:
    
        ServosInMiddle()
        time.sleep(3)




def ServosInMiddle ():
    
    c.write_goal_speed(ID_1, 6) # 设定舵机ID_1的速度为6 => Max Speed
    c.write_goal_speed(ID_2, 6) # 设定舵机ID_2的速度为6 => Max Speed
    Pos_1 = np.deg2rad(MiddlePos_1)
    Pos_2 = np.deg2rad(MiddlePos_2)
    c.write_goal_position(ID_1, Pos_1)
    c.write_goal_position(ID_2, Pos_2)
    time.sleep(0.01)



if __name__ == '__main__':
    main()


