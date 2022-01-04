from machine import Pin, I2C
import utime
from ssd1306 import SSD1306_I2C

TRIG = Pin(3, Pin.OUT) 
ECHO = Pin(2, Pin.IN)
GLED = Pin(4, Pin.OUT)
YLED = Pin(5, Pin.OUT)
RLED = Pin(6, Pin.OUT)
WIDTH = 128
HEIGHT = 32

i2c = I2C(0, scl = Pin(17), sda = Pin(16), freq = 200000)

oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

oled.fill(0)

oled.text("hello world", 0 , 0)

oled.show()

print ("Distance Measurement In Progress")

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
        
        picoTemp = machine.ADC(4)
        convertFactor = 3.3 / (65535)
        reading = picoTemp.read_u16() * convertFactor
        temp = 27 - (reading - 0.706)/0.001721
        tempStr = str(temp)
        
        WIDTH = 128
        HEIGHT = 32
        
        disStr = str(distance)
        
        i2c = I2C(0, scl = Pin(17), sda = Pin(16), freq = 200000)

        oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)


        oled.fill(0)
        oled.text("Distance: " + disStr, 0 , 0)
        oled.text("RPi Temp: " + tempStr, 0, 10)
        oled.show()
        
        
        if distance>=55: ##red light
            RLED.high()
            utime.sleep(1800)
            RLED.low()
            utime.sleep(900)
            RLED.high()
            utime.sleep(1800)
        else: RLED.low()
        
        if distance<=45: ##green light
            GLED.high()
            utime.sleep(1800)
            GLED.low()
            utime.sleep(900)
            RLED.high()
            utime.sleep(1800)
        else: GLED.low()
        
        if distance>=45.01 and distance<= 54.99: ##yellow light
            YLED.high()
            utime.sleep(1800)
            YLED.low()
            utime.sleep(900)
            YLED.high()
            utime.sleep(1800)
        else: YLED.low()
        

except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
