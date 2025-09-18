import time
import numpy as np

from rustypot import Scs0009PyController

#左右手
Side = 2 # 1=> 右手 right // 2=> 左手 leftt


#速度
MaxSpeed = 4
CloseSpeed = 3

#手指原点位置
#MiddlePos = [-12, 3, -5, 8, 0, 0, -8, 10] # 替换为实际的舵机校准值-右手
MiddlePos = [0, 0, 0, -5, 0, 0, 5, 5] # 替换为实际的舵机校准值-左手

c = Scs0009PyController(
        serial_port="COM9", #注意修改为实际端口
        baudrate=1000000,
        timeout=0.5,
    )



def main():
    for i in range(11, 18):
        try:
            c.write_torque_enable(i, 1)
            print(f"ID {i} 使能成功")
        except Exception as e:
            print(f"ID {i} 使能失败: {e}")
    
    #c.write_torque_enable(1, 1)  #1 = On / 2 = Off / 3 = Free

    t0 = time.time()

    while True:
        t = time.time() - t0

        OpenHand()
        time.sleep(0.5)

        CloseHand()
        time.sleep(3)

        OpenHand_Progressive()
        time.sleep(0.5)

        SpreadHand()
        time.sleep(0.6)
        ClenchHand()
        time.sleep(0.6)

        OpenHand()
        time.sleep(0.2)

        Index_Pointing()
        time.sleep(0.4)
        Nonono()
        time.sleep(0.5)
        
        OpenHand()
        time.sleep(0.3)

        Perfect()
        time.sleep(0.8)

        OpenHand()
        time.sleep(0.4)

        Victory()
        time.sleep(1)
        Scissors()
        time.sleep(0.5)

        OpenHand()
        time.sleep(0.4)

        Pinched()
        time.sleep(1)

        Fuck()
        time.sleep(0.8)


        #trials

        #c.sync_write_raw_goal_position([1,2], [50,50])
        #time.sleep(1)

        #a=c.read_present_position(1)
        #b=c.read_present_position(2)
        #a=np.rad2deg(a)
        #b=np.rad2deg(b)
        #print(f'{a} {b}')
        #time.sleep(0.001)



def OpenHand(): #张开
    Move_Index (-35,35, MaxSpeed)
    Move_Middle (-35,35, MaxSpeed)
    Move_Ring (-35,35, MaxSpeed)
    Move_Thumb (-35,35, MaxSpeed)

def CloseHand(): #关闭
    Move_Index (90,-90, CloseSpeed)
    Move_Middle (90,-90, CloseSpeed)
    Move_Ring (90,-90, CloseSpeed)
    Move_Thumb (90,-90, CloseSpeed+1)

def OpenHand_Progressive(): #依次张开
    Move_Index (-35,35, MaxSpeed-2)
    time.sleep(0.2)
    Move_Middle (-35,35, MaxSpeed-2)
    time.sleep(0.2)
    Move_Ring (-35,35, MaxSpeed-2)
    time.sleep(0.2)
    Move_Thumb (-35,35, MaxSpeed-2)

def SpreadHand(): #伸展
    if (Side==1): # Right 
        Move_Index (4, 90, MaxSpeed)
        Move_Middle (-32, 32, MaxSpeed)
        Move_Ring (-90, -4, MaxSpeed)
        Move_Thumb (-90, -4, MaxSpeed)  
  
    if (Side==2): # Left 
        Move_Index (-60, 0, MaxSpeed)
        Move_Middle (-35, 35, MaxSpeed)
        Move_Ring (-4, 90, MaxSpeed)
        Move_Thumb (-4, 90, MaxSpeed)  
  
def ClenchHand(): #握拳
    if (Side==1): # Right 
        Move_Index (-60, 0, MaxSpeed)
        Move_Middle (-35, 35, MaxSpeed)
        Move_Ring (0, 70, MaxSpeed)
        Move_Thumb (-4, 90, MaxSpeed)  
  
    if (Side==2): # Left 
        Move_Index (0, 60, MaxSpeed)
        Move_Middle (-35, 35, MaxSpeed)
        Move_Ring (-70, 0, MaxSpeed)
        Move_Thumb (-90, -4, MaxSpeed)
  
def Index_Pointing():  
    Move_Index (-40, 40, MaxSpeed)
    Move_Middle (90, -90, MaxSpeed)
    Move_Ring (90, -90, MaxSpeed)
    Move_Thumb (90, -90, MaxSpeed)
  
def Nonono(): 
  Index_Pointing()
  for i in range(3) :
        time.sleep(0.2)
        Move_Index (-10, 80, MaxSpeed)
        time.sleep(0.2)
        Move_Index (-80, 10, MaxSpeed)
  
  Move_Index (-35, 35, MaxSpeed)
  time.sleep(0.4)
  
def Perfect(): #比心
  if (Side==1): #Right 
        Move_Index (50, -50, MaxSpeed)
        Move_Middle (0, -0, MaxSpeed)
        Move_Ring (-20, 20, MaxSpeed)
        Move_Thumb (65, 12, MaxSpeed)

  
  if (Side==2): #Left 
        Move_Index (50, -50, MaxSpeed)
        Move_Middle (0, -0, MaxSpeed)
        Move_Ring (-20, 20, MaxSpeed)
        Move_Thumb (-12, -65, MaxSpeed)
  
def Victory():  #胜利
  if (Side==1): #Right  
        Move_Index (-15, 65, MaxSpeed)
        Move_Middle (-65, 15, MaxSpeed)
        Move_Ring (90, -90, MaxSpeed)
        Move_Thumb (90, -90, MaxSpeed)

  
  if (Side==2): #Left 
        Move_Index (-65, 15, MaxSpeed)
        Move_Middle (-15, 65, MaxSpeed)
        Move_Ring (90, -90, MaxSpeed)
        Move_Thumb (90, -90, MaxSpeed)
  
def Pinched(): #捏拳
  if (Side==1): #Right 
        Move_Index (90, -90, MaxSpeed)
        Move_Middle (90, -90, MaxSpeed)
        Move_Ring (90, -90, MaxSpeed)
        Move_Thumb (0, -75, MaxSpeed)

  if (Side==2): #Left 
        Move_Index (90, -90, MaxSpeed)
        Move_Middle (90, -90, MaxSpeed)
        Move_Ring (90, -90, MaxSpeed)
        Move_Thumb (75, 5, MaxSpeed)

def Scissors(): #剪刀
  Victory();
  if (Side==1): #Right 
        for i in range(3):  
            time.sleep(0.2)
            Move_Index (-50, 20, MaxSpeed)
            Move_Middle (-20, 50, MaxSpeed)
            
            time.sleep(0.2)
            Move_Index (-15, 65, MaxSpeed)
            Move_Middle (-65, 15, MaxSpeed)
    

  if (Side==2): #Left 
        for i in range(3):
            time.sleep(0.2)
            Move_Index (-20, 50, MaxSpeed)
            Move_Middle (-50, 20, MaxSpeed)
            
            time.sleep(0.2)
            Move_Index (-65, 15, MaxSpeed)
            Move_Middle (-15, 65, MaxSpeed)

def Fuck():

  if (Side==1): #Right 
        Move_Index (90, -90, MaxSpeed)
        Move_Middle (-35, 35, MaxSpeed)
        Move_Ring (90, -90, MaxSpeed)
        Move_Thumb (0, -75, MaxSpeed)

  if (Side==2): #Left 
        Move_Index (90, -90, MaxSpeed)
        Move_Middle (-35, 35, MaxSpeed)
        Move_Ring (90, -90, MaxSpeed)
        Move_Thumb (75, 0, MaxSpeed)
  
def Move_Index (Angle_1,Angle_2,Speed): #移动食指
    
    c.write_goal_speed(1, Speed)
    time.sleep(0.0002)
    c.write_goal_speed(2, Speed)
    time.sleep(0.0002)
    Pos_1 = np.deg2rad(MiddlePos[0]+Angle_1)
    Pos_2 = np.deg2rad(MiddlePos[1]+Angle_2)
    c.write_goal_position(1, Pos_1)
    c.write_goal_position(2, Pos_2)
    time.sleep(0.005)

def Move_Middle(Angle_1,Angle_2,Speed):    #移动中指
    c.write_goal_speed(3, Speed)
    time.sleep(0.0002)
    c.write_goal_speed(4, Speed)
    time.sleep(0.0002)
    Pos_1 = np.deg2rad(MiddlePos[2]+Angle_1)
    Pos_2 = np.deg2rad(MiddlePos[3]+Angle_2)
    c.write_goal_position(3, Pos_1)
    c.write_goal_position(4, Pos_2)
    time.sleep(0.005)

def Move_Ring(Angle_1,Angle_2,Speed):    #移动无名指
    c.write_goal_speed(5, Speed)
    time.sleep(0.0002)
    c.write_goal_speed(6, Speed)
    time.sleep(0.0002)
    Pos_1 = np.deg2rad(MiddlePos[4]+Angle_1)
    Pos_2 = np.deg2rad(MiddlePos[5]+Angle_2)
    c.write_goal_position(5, Pos_1)
    c.write_goal_position(6, Pos_2)
    time.sleep(0.005)

def Move_Thumb(Angle_1,Angle_2,Speed):    #移动拇指
    c.write_goal_speed(7, Speed)
    time.sleep(0.0002)
    c.write_goal_speed(8, Speed)
    time.sleep(0.0002)
    Pos_1 = np.deg2rad(MiddlePos[6]+Angle_1)
    Pos_2 = np.deg2rad(MiddlePos[7]+Angle_2)
    c.write_goal_position(7, Pos_1)
    c.write_goal_position(8, Pos_2)
    time.sleep(0.005)


if __name__ == '__main__':
    main()



