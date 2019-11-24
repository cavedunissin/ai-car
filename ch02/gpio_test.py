#!/usr/bin/env python3

#匯入套件
import time
import RPi.GPIO as GPIO

# 設定腳位
PIN = 16


# 初始化 GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(PIN, GPIO.OUT)

while True:

    #定義GPIO動作
    def on():
        GPIO.output(PIN, True)
    def off():
        GPIO.output(PIN, False)
        

    #執行程式
    try:
        on()
        time.sleep(1)
        off()
        time.sleep(1)
        
    #例外中斷狀況
    except KeyboardInterrupt:
        off()
        GPIO.cleanup()
