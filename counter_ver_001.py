# Counter ver 001
#Program will detect pin state change and increment a counter. Counter is maunal reest with buttonUP state change. ButtonDown will decrement counter( in case there was an accentical increamert)
#Display will dispaly current number vaule between 1 and 99.

import time # time module
import RPi.GPIO as GPIO #Pin interface module

# pin definitions
counterRest = 20
buttonUP = 21
buttonDown = 26
detectBottle = 19
soundBuzzer = 12


#set up pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#switch setup
GPIO.setup(counterRest, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(buttonUP, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(buttonDown, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(detectBottle, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(soundBuzzer, GPIO.OUT)

'''def RedButton():
    GPIO.wait_for_edge(counterRest, GPIO.FALLING)
    print('COUNTER RESET')
    Greeting0.play()
    
def YellowButton():
    GPIO.wait_for_edge(yellow_button, GPIO.FALLING)
    print('Yellow Button fuction')
'''    Greeting0.play()

def BUZZER():
    GPIO.output(soundBuzzer, True) # set Trigger to HIGH
    time.sleep(0.1)
    GPIO.output(soundBuzzer, False)

def MAINLOOP():# first code that gets run

    print('The Program is Running')
    time.sleep(1)
    counter = 0
    
    while True:
        print('Program is running through the loop')
        #time.sleep(10)
        counter_state = GPIO.input(counterRest)
        buttonUP_state = GPIO.input(buttonUP)
        buttonDown_state = GPIO.input(buttonDown)
        detectBottle_state = GPIO.input(detectBottle)
       
         
        if counter_stat == GPIO.LOW:
            print('Counter Rest')
            counter = 0
           
        elif buttonUP_state == GPIO.LOW:
            counter = counter + 1
            print('counter vaule is %.lf' % counter)
            print('Increment Button was pressed Increament counter')
            time.sleep(.1)
                
        elif buttonDown_state == GPIO.LOW:
            print('Counter was decermented')
            counter = counter - 1
            time.sleep(.1)
                
        elif detectBottle_state == GPIO.LOW:
            print('Bottle was Detected')
            counter = counter + 1
            BUZZER()
            print('counter vaule is %.lf' % counter)
            time.sleep(.1)
         
#This is were the program starts       
MAINLOOP() 