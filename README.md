# 📌 การใช้งาน MicroPython กับ KidBright และ Ultrasonic Sensor

## 🔥 เกี่ยวกับโปรเจกต์
โปรเจกต์นี้เป็น **เครื่องจ่ายแอลกอฮอล์อัตโนมัติ** โดยใช้ **MicroPython บน KidBright** ควบคุม **เซ็นเซอร์อัลตราโซนิก (Ultrasonic Sensor)** และ **เซอร์โวมอเตอร์ (Servo Motor)**

## 🛠️ อุปกรณ์ที่ต้องใช้
- **บอร์ด KidBright**
- **Ultrasonic Sensor (HC-SR04)**
- **Servo Motor**
- **สาย USB สำหรับอัปโหลดโค้ด**

## 🔌 การต่อวงจร
| อุปกรณ์          | ขา KidBright |
|-----------------|-------------|
| Trig (Ultrasonic) | **12 (D12)** |
| Echo (Ultrasonic) | **14 (D14)** |
| Servo (Signal)    | **15 (D15)** |
| VCC (5V)          | **5V**       |
| GND               | **GND**      |

## 📝 โค้ด MicroPython สำหรับควบคุมการจ่ายแอลกอฮอล์
```python
from machine import Pin, PWM
import time

# กำหนดขาสำหรับเซ็นเซอร์อัลตราโซนิก
trig = Pin(12, Pin.OUT)
echo = Pin(14, Pin.IN)

# กำหนดขาสำหรับเซอร์โวมอเตอร์
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
    distance = (duration * 0.0343) / 2  # แปลงเวลาเป็นระยะทาง (cm)
    return distance

# ฟังก์ชันควบคุมเซอร์โว
def set_servo(angle):
    duty = int((angle / 180) * 102 + 26)  # คำนวณ Duty Cycle
    servo.duty(duty)

# วนลูปหลัก
while True:
    dist = get_distance()
    print("ระยะทาง:", dist, "cm")
    
    if dist < 10:  # ถ้าระยะ < 10 ซม. ให้กดแอลกอฮอล์
        set_servo(0)  # กดหัวจ่าย
        time.sleep(0.5)
        set_servo(90)  # คืนตำแหน่งเดิม
        time.sleep(2)  # ป้องกันการกดซ้ำ
    
    time.sleep(0.1)
```

## 🚀 วิธีการใช้งาน
1. **ต่อวงจร** ตามตารางด้านบน
2. **อัปโหลดโค้ด** ไปยัง KidBright ผ่าน **Thonny IDE** หรือ **Ampy**
3. **เปิดใช้งานบอร์ด** และลองนำมือเข้าใกล้เซ็นเซอร์ (น้อยกว่า 10 ซม.)
4. **เซอร์โวจะหมุน** เพื่อกดหัวจ่ายแอลกอฮอล์อัตโนมัติ

## 📌 หมายเหตุ
- ค่าระยะทางที่ **10 ซม.** สามารถเปลี่ยนแปลงได้ตามต้องการ
- ต้องการพลังงานที่เพียงพอ **(แนะนำใช้แหล่งจ่าย 5V แยกสำหรับเซอร์โว)**

## 🔗 แหล่งข้อมูลเพิ่มเติม
- [MicroPython Official Documentation](https://micropython.org/)
- [KidBright Official Website](https://www.kid-bright.org/)

📌 **ร่วมพัฒนาและช่วยกันแก้ไขได้ที่ GitHub!** ✅
