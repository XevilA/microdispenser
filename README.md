# 📌 คู่มือการใช้งาน MicroPython กับ KidBright

## 🔥 เกี่ยวกับโปรเจกต์

โปรเจกต์นี้เป็นแนวทางการใช้งาน **MicroPython บนบอร์ด KidBright** เหมาะสำหรับมือใหม่ที่ต้องการเรียนรู้การเขียนโปรแกรมเพื่อควบคุมอุปกรณ์อิเล็กทรอนิกส์ 🛠️

## 🛠️ อุปกรณ์ที่ต้องใช้

- 🖥️ **คอมพิวเตอร์** (Windows / macOS / Linux)

- 📟 **บอร์ด KidBright**

- 🔌 **สาย USB** (สำหรับเชื่อมต่อ KidBright กับคอมพิวเตอร์)

- 💡 **เซ็นเซอร์ต่าง ๆ** เช่น Light Sensor, Temperature Sensor, Servo Motor ฯลฯ

## 🔧 การติดตั้ง MicroPython บน KidBright

1\. ดาวน์โหลด **Firmware MicroPython** สำหรับ KidBright ได้ที่ [GitHub KidBright](https://github.com/KidBright)

2\. ใช้โปรแกรม **esptool.py** หรือ **Thonny IDE** เพื่อลง MicroPython

3\. เชื่อมต่อ KidBright ผ่าน USB แล้วแฟลชไฟล์ `.bin` ลงบอร์ด

## 📝 ตัวอย่างโค้ด MicroPython บน KidBright

### ✨ กระพริบไฟ LED บน KidBright

```python

from machine import Pin

import time

led = Pin(33, Pin.OUT)  # ขา LED บน KidBright

while True:

    led.value(1)  # เปิดไฟ

    time.sleep(1)

    led.value(0)  # ปิดไฟ

    time.sleep(1)

```

### 📡 อ่านค่า Light Sensor

```python

from machine import ADC

light_sensor = ADC(34)  # ขา Light Sensor

light_sensor.atten(ADC.ATTN_11DB)  # ปรับช่วงการอ่านค่า

while True:

    value = light_sensor.read()

    print("Light Level:", value)

```

## 🚀 แหล่งข้อมูลเพิ่มเติม

- [เว็บไซต์ทางการของ KidBright](https://www.kid-bright.org/)

- [MicroPython Official Docs](https://micropython.org/)

📌 **ร่วมพัฒนาและช่วยกันแก้ไขได้ที่ GitHub!** ✅
