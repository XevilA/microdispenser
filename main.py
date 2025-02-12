from machine import Pin, PWM
import time

#เซ็นเซอร์อัลตราโซนิก
trig = Pin(12, Pin.OUT)
echo = Pin(14, Pin.IN)

# เซอร์โวมอเตอร์
servo = PWM(Pin(15), freq=50)  # ความถี่ 50Hz (มาตรฐานของ Servo)

# ฟังก์ชันวัดระยะทางจากเซ็นเซอร์อัลตราโซนิก
def get_distance():
    trig.low()
    time.sleep_us(2)
    trig.high()
    time.sleep_us(10)
    trig.low()
    
    while echo.value() == 0:
        pulse_start = time.ticks_us()
    while echo.value() == 1:
        pulse_end = time.ticks_us()
    
    duration = time.ticks_diff(pulse_end, pulse_start)
    distance = (duration * 0.0343) / 2  
    return distance

#ควบคุมเซอร์โว
def set_servo(angle):
    duty = int((angle / 180) * 102 + 26)  # คำนวณ Duty Cycle
    servo.duty(duty)


while True:
    dist = get_distance()
    print("ระยะทาง:", dist, "cm")
    
    if dist < 10:  # ถ้าระยะ < 10 ซม. ให้กดแอลกอฮอล์
        set_servo(0)  # กดหัวจ่าย
        time.sleep(0.5)
        set_servo(90)  
        time.sleep(2)  
    
    time.sleep(0.1)
