import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG = 23 
ECHO = 24

print ("Distance Measurement In Progress")

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)

try:
    while True:

        GPIO.output(TRIG, False)
        print ("Waiting For Sensor To Settle")
        time.sleep(2)

        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO)==0:
          pulse_start = time.time()

        while GPIO.input(ECHO)==1:
          pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17150

        distance = round(distance, 2)

        print ("Salt level in CM:", distance)
        
        if distance>=55: ##red light
            GPIO.output(25,GPIO.HIGH)
        else: GPIO.output(25,GPIO.LOW)
        
        if distance<=25: ##green light
            GPIO.output(6,GPIO.HIGH)
        else: GPIO.output(6,GPIO.LOW)
        
        if distance>=25.01 and distance<= 54.99: ##yellow light
            GPIO.output(26,GPIO.HIGH)
        else: GPIO.output(26,GPIO.LOW)
        

except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
    GPIO.cleanup()
