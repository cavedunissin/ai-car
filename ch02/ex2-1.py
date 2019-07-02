#!/usr/bin/env python3

#匯入套件
import time
import RPi.GPIO as GPIO

# 設定腳位
PWM_PIN_left_1 = 5
PWM_PIN_left_2 = 6
PWM_PIN_right_3 = 13
PWM_PIN_right_4 = 19

# 初始化 GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(PWM_PIN_left_1, GPIO.OUT)
GPIO.setup(PWM_PIN_left_2, GPIO.OUT)
GPIO.setup(PWM_PIN_right_3, GPIO.OUT)
GPIO.setup(PWM_PIN_right_4, GPIO.OUT)

while True:

    #定義車子動作
    def forward():
        GPIO.output(PWM_PIN_left_1, True)
        GPIO.output(PWM_PIN_left_2, False)
        GPIO.output(PWM_PIN_right_3, True)
        GPIO.output(PWM_PIN_right_4, False)

    def stop():
        GPIO.output(PWM_PIN_left_1, False)
        GPIO.output(PWM_PIN_left_2, False)
        GPIO.output(PWM_PIN_right_3, False)
        GPIO.output(PWM_PIN_right_4, False)

    #執行程式
    try:
        forward()
        time.sleep(1)
        stop()
        time.sleep(1)
        
    #例外中斷狀況
    except KeyboardInterrupt:
        stop()
        GPIO.cleanup()
