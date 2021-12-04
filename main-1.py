from machine import Pin
import utime
#GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)

TRIG = Pin(3, Pin.OUT) 
ECHO = Pin(2, Pin.IN)
GLED = Pin(4, Pin.OUT)
YLED = Pin(5, Pin.OUT)
RLED = Pin(6, Pin.OUT)

print ("Distance Measurement In Progress")

##GPIO.setup(TRIG,GPIO.OUT)
##GPIO.setup(ECHO,GPIO.IN)
##GPIO.setup(25,GPIO.OUT)
##GPIO.setup(26,GPIO.OUT)
##GPIO.setup(6,GPIO.OUT)

try:
    while True:

        TRIG.low()
        print ("Waiting For Sensor To Settle")
        utime.sleep(2)

        TRIG.high()
        utime.sleep(0.00001)
        TRIG.low()
        
        while ECHO.value()==0:
          pulse_start = utime.ticks_us()

        while ECHO.value()==1:
          pulse_end = utime.ticks_us()

        pulse_duration = pulse_end - pulse_start

        distance = (pulse_duration * 0.0343) / 2

        distance = round(distance, 2)

        print ("Salt level in CM:", distance)
        
        if distance>=55: ##red light
            RLED.high()
        else: RLED.low()
        
        if distance<=25: ##green light
            GLED.high()
        else: GLED.low()
        
        if distance>=25.01 and distance<= 54.99: ##yellow light
            YLED.high()
        else: YLED.low()
        

except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
    
