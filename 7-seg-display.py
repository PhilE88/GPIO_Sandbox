#!/usr/bin/python
import RPi.GPIO as GPIO

import time

LEDS = dict(LED_A = 8, LED_B = 10, LED_DP = 12, LED_C = 11, LED_D = 13, LED_E = 15, LED_F = 5, LED_G = 16)
    
GPIO.setmode(GPIO.BOARD)

def spell(char):
    for x in LEDS:
        if char == "F":
            if x == "LED_A" or x == "LED_F" or x == "LED_G" or x == "LED_E":
                GPIO.output(LEDS[x], GPIO.HIGH)
            else:
                GPIO.output(LEDS[x], GPIO.LOW)
                
        if char == "U":
            if x == "LED_D" or x == "LED_F" or x == "LED_C" or x == "LED_E" or x == "LED_B":
                GPIO.output(LEDS[x], GPIO.HIGH)
            else:
                GPIO.output(LEDS[x], GPIO.LOW)
                
        if char == "C":
            if x == "LED_D" or x == "LED_F" or x == "LED_E" or x == "LED_A":
                GPIO.output(LEDS[x], GPIO.HIGH)
            else:
                GPIO.output(LEDS[x], GPIO.LOW)
                
        if char == "H":
            if x == "LED_G" or x == "LED_F" or x == "LED_C" or x == "LED_E" or x == "LED_B":
                GPIO.output(LEDS[x], GPIO.HIGH)
            else:
                GPIO.output(LEDS[x], GPIO.LOW)
                                
        if char == "Y":
            if x == "LED_G" or x == "LED_F" or x == "LED_C" or x == "LED_D" or x == "LED_B":
                GPIO.output(LEDS[x], GPIO.HIGH)
            else:
                GPIO.output(LEDS[x], GPIO.LOW)
                                
        if char == "O":
            if x == "LED_A" or x == "LED_F" or x == "LED_C" or x == "LED_E" or x == "LED_B" or x == "LED_D":
                GPIO.output(LEDS[x], GPIO.HIGH)
            else:
                GPIO.output(LEDS[x], GPIO.LOW)    

for x in LEDS:
    GPIO.setup(LEDS[x], GPIO.OUT)

for x in LEDS:
    GPIO.output(LEDS[x], GPIO.LOW)
    
phrase = "FUCHYOU"
for x in phrase:
    spell(x)
    time.sleep(0.6)



# i = 1
# while i < 6:
#     
#     for x in LEDS:
#         GPIO.output(LEDS[x], GPIO.HIGH)
#         time.sleep(0.1)
#         GPIO.output(LEDS[x], GPIO.LOW)
#         
#     i += 1
#     
for x in LEDS:
    GPIO.output(LEDS[x], GPIO.LOW)
    
