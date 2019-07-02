#!/usr/bin/env python3

import time
import RPi.GPIO as GPIO

# 設定腳位
PWM_PIN_left_1 = 5
PWM_PIN_left_2 = 6
PWM_PIN_right_3 = 13
PWM_PIN_right_4 = 19

DUTY_CYCLE = 65

# 初始化 GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PWM_PIN_left_1, GPIO.OUT)
GPIO.setup(PWM_PIN_left_2, GPIO.OUT)
GPIO.setup(PWM_PIN_right_3, GPIO.OUT)
GPIO.setup(PWM_PIN_right_4, GPIO.OUT)

pwm_left_1 = GPIO.PWM(PWM_PIN_left_1, 500)
pwm_left_2 = GPIO.PWM(PWM_PIN_left_2, 500)
pwm_right_3 = GPIO.PWM(PWM_PIN_right_3, 500)
pwm_right_4 = GPIO.PWM(PWM_PIN_right_4, 500)

pwm_left_1.start(0)
pwm_left_2.start(0)
pwm_right_3.start(0)
pwm_right_4.start(0)

while True:
    #定義車子動作
    def forward():
        pwm_left_1.ChangeDutyCycle(DUTY_CYCLE)
        pwm_left_2.ChangeDutyCycle(0)
        pwm_right_3.ChangeDutyCycle(DUTY_CYCLE)
        pwm_right_4.ChangeDutyCycle(0)
    def back():
        pwm_left_1.ChangeDutyCycle(0)
        pwm_left_2.ChangeDutyCycle(DUTY_CYCLE)
        pwm_right_3.ChangeDutyCycle(0)
        pwm_right_4.ChangeDutyCycle(DUTY_CYCLE)
    def right():
        pwm_left_1.ChangeDutyCycle(DUTY_CYCLE)
        pwm_left_2.ChangeDutyCycle(0)
        pwm_right_3.ChangeDutyCycle(0)
        pwm_right_4.ChangeDutyCycle(0)

    def left():
        pwm_left_1.ChangeDutyCycle(0)
        pwm_left_2.ChangeDutyCycle(0)
        pwm_right_3.ChangeDutyCycle(DUTY_CYCLE)
        pwm_right_4.ChangeDutyCycle(0)
    
    def stop():
        pwm_left_1.ChangeDutyCycle(0)
        pwm_left_2.ChangeDutyCycle(0)
        pwm_right_3.ChangeDutyCycle(0)
        pwm_right_4.ChangeDutyCycle(0)

    #執行程式
    try:
        DUTY_CYCLE= input("Enter motor PWM :")
        DUTY_CYCLE= int(DUTY_CYCLE)        
        forward()
        time.sleep(1)
        back()
        time.sleep(1)
        right()
        time.sleep(1)
        left()
        time.sleep(1)
        stop()
    #例外中斷狀況
    except KeyboardInterrupt:
        stop()
        GPIO.cleanup()
        break
    except:
        print("Error")
