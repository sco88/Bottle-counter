# This is m first attenpt at using a imported file to do srtup for my program. Hoe it works. :)
'''
Working version
This program is Lunas Brain. Luna is a smart Treat Dispencer/Game created to challange
my skills in 3d printing, programming and dog training :).
Author Scott Cantwell

Copy of Lunas_brain_v0.2.1
VERSION = "Software V0.3.0" Program re wirte to improve speed of buttons and over all  operation.



'''

import time # time module
import RPi.GPIO as GPIO #Pin interface module
from pygame import mixer # sound module
import pygame # sound module
import driver
#pygame.init()
#pygame.display.set_mode()
mylcd = driver.lcd()
mylcd.lcd_clear()

# pin definitions
CenterPedal = 26
blue_button = 17
green_button = 16
yellow_button = 12 
red_button = 13
m1 = 25 # motor 1
m2 = 18 # motor 2
WindowLED = 20 # Trigger for Relay
GateLED = 21 # Trigger for Relay
GPIO_TRIGGER = 24    # Sonar Out
GPIO_ECHO = 23     # Sonar IN

#set up pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#switch setup
GPIO.setup(CenterPedal, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(blue_button, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(green_button, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(red_button, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(yellow_button, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(green_button, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(m1,GPIO.OUT)
GPIO.setup(m2,GPIO.OUT)
GPIO.setup(WindowLED,GPIO.OUT)
GPIO.setup(GateLED,GPIO.OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

# Set start state for PINs
GPIO.output(WindowLED,GPIO.HIGH) #OFF  
GPIO.output(GateLED,GPIO.HIGH)  #OFF  
GPIO.output(m1,GPIO.HIGH)       #OFF
GPIO.output(m2,GPIO.HIGH)      #OFF

#Timers and counters
MOTOR_TIMER = 0.5 # value in secs motor is dispensing
MOTOR_TIMER2 = 0.5
mixer.init() # initialize pygame mixer
TD = 40 # distnace in cm that triggers command to press button
VERSION = "Software V0.3.0"#see description at top
PedalCounter = 1 #consective allowed pedal presses before sleeptimer
DelayTimer = 100 #Treat intervial after max presses ( measured in seconds)

#Display setup
mylcd.lcd_display_string(VERSION, 1,0)# Dispaly current software version 
time.sleep(1)
mylcd.lcd_clear()
mylcd.lcd_display_string("Manual", 2,0)
mylcd.lcd_display_string("Bell", 2,12)

#load instance of sound file
Greeting1 = mixer.Sound('/home/pi/thecore/Jackpot.wav')
Greeting2 = mixer.Sound('/home/pi/thecore/Startup_female.wav')
Greeting3 = mixer.Sound('/home/pi/thecore/good_girl_female.wav')
Greeting4 = mixer.Sound('/home/pi/thecore/press_the_button_stupid_female.wav')
Greeting5 = mixer.Sound('/home/pi/thecore/bell.wav')
Greeting6 = mixer.Sound('/home/pi/thecore/more_credits_female.wav')
Greeting7 = mixer.Sound('/home/pi/thecore/buzzer.wav')
Greeting8 = mixer.Sound('/home/pi/thecore/GFM.wav')
#Greeting9 = mixer.Sound('')
Greeting0 = mixer.Sound('/home/pi/thecore/applause.wav')

'''TEST SOUND FILES'''
#Greeting1.play()
#Greeting2.play()
#Greeting3.play()
#Greeting4.play()
#Greeting5.play()
#Greeting6.play()
#Greeting7.play()
#Greeting8.play()
#Greeting9.play()
#Greeting0.play()

'''TEST LED STRIPS'''
#Window_LED()
#Gate_LED()
''''''''''''''''''''''''''''''''''''''''''''''''
def distance():
    GPIO.output(GPIO_TRIGGER, True) # set Trigger to HIGH
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False) # set Trigger after 0.01ms to LOW
    
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time() 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
    time.sleep(.5)
    return distance
                  
        
def dispencer1():
    Greeting1.play()
    GPIO.output(WindowLED,GPIO.LOW)
    print('LEDs ON')
    GPIO.output(m1,GPIO.LOW)
    print('motor turned ON')
    time.sleep(MOTOR_TIMER)
    GPIO.output(m1,GPIO.HIGH)
    print('motor turned OFF')
    GPIO.output(WindowLED,GPIO.HIGH)
    print('LEDs OFF')
    
def dispencer2():
    GPIO.output(WindowLED,GPIO.LOW)
    print('LEDs ON')
    time.sleep(.5)
    GPIO.output(m2,GPIO.LOW)
    print('motor turned ON')
    time.sleep(MOTOR_TIMER)
    GPIO.output(m2,GPIO.HIGH)
    print('motor turned OFF')
        
def Gate_LED():
    GPIO.output(GateLED,GPIO.LOW)
    print('LEDs ON')
    time.sleep(.5)
    GPIO.output(GateLED,GPIO.HIGH)
    print('motor turned OFF')
    GPIO.output(GateLED,GPIO.LOW)
    print('LEDs ON')
    time.sleep(.5)
    GPIO.output(GateLED,GPIO.HIGH)
    print('motor turned OFF')
    
def Window_LED():
    GPIO.output(WindowLED,GPIO.LOW)
    print('LEDs ON')
    time.sleep(.5)
    GPIO.output(WindowLED,GPIO.HIGH)
    print('LEDs OFF')
    time.sleep(.5)
    GPIO.output(WindowLED,GPIO.LOW)
    print('LEDs ON')
    time.sleep(.5)
    GPIO.output(WindowLED,GPIO.HIGH)
    print('LEDs OFF')    

def ManualOverride():
    GPIO.wait_for_edge(blue_button, GPIO.FALLING)
    print('Falling edge detected on blue button')# interrupt program if button is presses ( Manual override )
    Greeting1.play()
    dispencer1()
    Window_LED()
    Greeting3.play()
    Gate_LED()
    Main()
        
def DinnerBell():
    #GPIO.wait_for_edge(green_button, GPIO.FALLING)
    #print('Falling edge detected on green button')# interrupt program if button is presses ( Ring dinner bell )
    Greeting5.play()
    time.sleep(1)
    #Main()
    
def RedButton():
    GPIO.wait_for_edge(red_button, GPIO.FALLING)
    print('Red Button fuction')
    Greeting0.play()
    
def YellowButton():
    GPIO.wait_for_edge(yellow_button, GPIO.FALLING)
    print('Yellow Button fuction')
    Greeting0.play()   
    
def Ranger():    
    dist = round(distance())# round sensor data number
    time.sleep(.05)    
    mylcd.lcd_display_string(f"MD = {dist} cm", 1,0)
    print(f"Measured Distance = {dist} cm")
    time.sleep(.05)
    
def Blue_Menu():
    mylcd.lcd_display_string("Time between lockout", 1,0)
    mylcd.lcd_display_string("30m", 2,0)
    mylcd.lcd_display_string("60m", 2,5)
    mylcd.lcd_display_string("120m", 2,10)
    mylcd.lcd_display_string("Back", 2,13)
    
    if GB_state == GPIO.LOW:
        Main_Menu
    if BB_state == GPIO.LOW:
        DelayTimer = 1800        
    if RB_state == GPIO.LOW:
        DelayTimer = 3600       
    if YB_state == GPIO.LOW:
        DelayTimer = 7200
    Blue_Menu()
    
def Red_Menu():
    mylcd.lcd_display_string("How many treats", 1,0)
    mylcd.lcd_display_string("Abit", 2,0)
    mylcd.lcd_display_string("Some", 2,6)
    mylcd.lcd_display_string("more", 2,11)
    mylcd.lcd_display_string("Bk", 2,15)
    
    if GB_state == GPIO.LOW:
        Main_Menu
    if BB_state == GPIO.LOW:
        MOTOR_TIMER = 0.5       
    if RB_state == GPIO.LOW:
        MOTOR_TIMER = 0.7      
    if YB_state == GPIO.LOW:
        MOTOR_TIMER = 0.9
    Red_Menu()
    
def Yellow_Menu():
    mylcd.lcd_display_string("ConsecutivePedal", 1,0)
    mylcd.lcd_display_string("3", 2,0)
    mylcd.lcd_display_string("5", 2,6)
    mylcd.lcd_display_string("7", 2,11)
    mylcd.lcd_display_string("Bk", 2,15)
    
    if GB_state == GPIO.LOW:
        Main_Menu
    if BB_state == GPIO.LOW:
        PedalCounter = 3       
    if RB_state == GPIO.LOW:
        PedalCounter = 5      
    if YB_state == GPIO.LOW:
        PedalCounter = 7
    Yellow_Menu()
    
def Green_Menu():
    mylcd.lcd_display_string("Distance sensor", 1,0)
    mylcd.lcd_display_string("40cm", 2,0)
    mylcd.lcd_display_string("50cm", 2,6)
    mylcd.lcd_display_string("60cm", 2,11)
    mylcd.lcd_display_string("BK", 2,15)
    
    if GB_state == GPIO.LOW:
        Main_Menu
    if BB_state == GPIO.LOW:
        TD = 40       
    if RB_state == GPIO.LOW:
        TD = 50      
    if YB_state == GPIO.LOW:
        TD = 60
    Green_Menu()

def Main_Menu():
    
    while True:
        mylcd.lcd_clear()
        mylcd.lcd_display_string("Setup Menu", 1,0)
        mylcd.lcd_display_string("BB", 2,0)
        mylcd.lcd_display_string("RB", 2,4)
        mylcd.lcd_display_string("YB", 2,8)
        mylcd.lcd_display_string("GB", 2,12)
        if GB_state == GPIO.LOW:
            Main_Menu()
        if BB_state == GPIO.LOW:
            PedalCounter = 3       
        if RB_state == GPIO.LOW:
            PedalCounter = 5      
        if YB_state == GPIO.LOW:
            PedalCounter = 7


def TimeOut():
    
    time_end = time.time() + (60 * 5) # 15 min loop timer (60secs * 15 = 15 min)    
    while time.time() < time_end:
        
        CP_state = GPIO.input(CenterPedal)
        GB_state = GPIO.input(green_button)
        RB_state = GPIO.input(red_button)
        YB_state = GPIO.input(yellow_button)
        BB_state = GPIO.input(blue_button)
        
        if CP_state == GPIO.LOW:
            Greeting7.play()
        
        elif GB_state == GPIO.LOW:
            print('The Green button has been pressed inside of time out')
            DinnerBell()
            #time.sleep(1)
            
        elif RB_state == GPIO.LOW:
            print('The Red Button has been pressed inside of time out')
            dispencer2()
            #time.sleep(.1)
            
        elif YB_state == GPIO.LOW:
            print('The Yellow has been pressed inside of time out')
            Greeting0.play()
            time.sleep(1)
            
        elif BB_state == GPIO.LOW:
            print('This was the blue button inside of time out')
            dispencer1()
            #time.sleep(.1)
            
            
def MAINLOOP():# first code that gets run

    print('The Program is Running')
    time.sleep(1)
    counter = 0
    
    while True:
        print('Program is running through the loop')
        #time.sleep(10)
        CP_state = GPIO.input(CenterPedal)
        GB_state = GPIO.input(green_button)
        RB_state = GPIO.input(red_button)
        YB_state = GPIO.input(yellow_button)
        BB_state = GPIO.input(blue_button)
        
        
        if CP_state == GPIO.LOW:
            print(' The Pedal has been pressed')
            dispencer1()        
            counter = counter + 1
            print('counter vaule is %.lf' % counter)
            if counter >= PedalCounter:
                print('You are in time out')
                Greeting7.play()
                TimeOut()# jump to TimeOut Function for timed loop with button checking
                print('Get ready.... Here comes the Dinner bell')
                DinnerBell()
                counter = 0
            
        elif GB_state == GPIO.LOW:
            print('The Green button has been pressed')
            DinnerBell()
            #time.sleep(1)
                
        elif RB_state == GPIO.LOW:
            print('The Red Button has been pressed')
            dispencer2()
            #time.sleep(.1)
                
        elif YB_state == GPIO.LOW:
            print('The Yellow has been pressed')
            Greeting0.play()
            time.sleep(1)
                
        elif BB_state == GPIO.LOW:
            print('This was the blue button')
            dispencer1()
            #time.sleep(.1)
            
        #elif distance == 40:
         #   Greeting8.play()
           
            
        
#This is were the program starts       
MAINLOOP()       
        
    
    
    




             

