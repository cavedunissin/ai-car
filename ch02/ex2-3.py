#!/usr/bin/env python3
import time

import RPi.GPIO as GPIO

# 設定腳位
PWM_PIN_left_1 = 5
PWM_PIN_left_2 = 6
PWM_PIN_right_3 = 13
PWM_PIN_right_4 = 19

IR_LEFT_PIN = 17
IR_MIDDLE_PIN = 27
IR_RIGHT_PIN = 22

DUTY_CYCLE = 65

def main():
    # 初始化 GPIO
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(IR_RIGHT_PIN, GPIO.IN)  #GPIO 17 -> Left IR in
    GPIO.setup(IR_MIDDLE_PIN, GPIO.IN) #GPIO 27 -> Cent IR in
    GPIO.setup(IR_LEFT_PIN, GPIO.IN)   #GPIO 22 -> Right IR in

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

    #定義車子動作
    def forward():
        pwm_left_1.ChangeDutyCycle(DUTY_CYCLE)
        pwm_left_2.ChangeDutyCycle(0)
        pwm_right_3.ChangeDutyCycle(DUTY_CYCLE)
        pwm_right_4.ChangeDutyCycle(0)
    def turn_left():
        pwm_left_1.ChangeDutyCycle(0)
        pwm_left_2.ChangeDutyCycle(0)
        pwm_right_3.ChangeDutyCycle(DUTY_CYCLE)
        pwm_right_4.ChangeDutyCycle(0)

    def turn_right():
        pwm_left_1.ChangeDutyCycle(DUTY_CYCLE)
        pwm_left_2.ChangeDutyCycle(0)
        pwm_right_3.ChangeDutyCycle(0)
        pwm_right_4.ChangeDutyCycle(0)

    def stop():
        pwm_left_1.ChangeDutyCycle(0)
        pwm_left_2.ChangeDutyCycle(0)
        pwm_right_3.ChangeDutyCycle(0)
        pwm_right_4.ChangeDutyCycle(0)

    #光感應器循跡建議
    def track_line():
        middle_val = GPIO.input(IR_MIDDLE_PIN)
        left_val = GPIO.input(IR_LEFT_PIN)
        right_val = GPIO.input(IR_RIGHT_PIN)
        print('光感:', left_val, middle_val, right_val)

        #中間收發器偵測為白
        if middle_val:
            if left_val and right_val:        # 白白白
                return 'stop'
            elif left_val and not right_val:  # 白白黑
                return 'left'
            elif not left_val and right_val:  # 黑白白
                return 'right'
            else:
                return 'forward'              # 黑白黑
        #中間收發器偵測為黑
        else:
            if left_val and right_val:        # 白黑白
                return 'stall'
            elif left_val and not right_val:  # 白黑黑
                return 'left'
            elif not left_val and right_val:  # 黑黑白
                return 'right'
            else:                             # 黑黑黑
                return 'stall'

    #執行程式
    try:
        while True:
            advice = track_line()

            if advice == 'left':
                print('動作:', '左轉')
                turn_left()

            elif advice == 'right':
                print('動作:', '右轉')
                turn_right()

            elif advice == 'stop':
                print('動作:', '停止')
                stop()

            elif advice == 'forward':
                print('動作:', '前進')
                forward()

            elif advice == 'stall':
                print('動作:', '前進')
                forward()
            print()
            
    except KeyboardInterrupt:
        print('使用者中斷')
    # 終止馬達
    pwm1.stop()
    pwm2.stop()
    
if __name__  == '__main__':
    main()
