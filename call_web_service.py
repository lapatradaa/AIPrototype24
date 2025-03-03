import requests
import json

# URL ของ API
url = 'http://13.75.95.136/simpleAPI'

# ป้อนข้อความจากผู้ใช้
msg = input("กรุณาป้อนข้อความ: ")

# รายชื่อและ IP ที่มีอยู่แล้ว
recipients = {
    "Phu": "104.43.58.161",
    "tarkung": "20.255.61.79"
}

# ให้ผู้ใช้ป้อนชื่อและ IP ของผู้รับเอง หรือเลือกจากที่มีอยู่แล้ว
print("\nเลือกรายชื่อที่ต้องการส่งข้อความ:")
for i, name in enumerate(recipients.keys(), start=1):
    print(f"{i}. {name} (IP: {recipients[name]})")
print(f"{len(recipients) + 1}. ป้อนชื่อและ IP เอง")

choice = input("กรุณาเลือกหมายเลข: ")

if choice.isdigit() and int(choice) in range(1, len(recipients) + 1):
    recipient = list(recipients.keys())[int(choice) - 1]
    ip = recipients[recipient]
else:
    recipient = input("ป้อนชื่อผู้รับ: ")
    ip = input("ป้อน IP ของผู้รับ: ")
    
    # ตรวจสอบว่า IP ซ้ำหรือไม่
    if ip in recipients.values():
        print("\nพบ IP นี้อยู่แล้วในระบบ ข้ามไปยังขั้นตอนถัดไป...")
    else:
        recipients[recipient] = ip  # เพิ่มเข้าไปใน dictionary

# ชื่อผู้ส่ง
sender = "ploykwan"  # สามารถเปลี่ยนเป็น input() เพื่อให้ผู้ใช้ป้อนเองได้

# สร้าง dictionary สำหรับข้อมูลที่จะส่งไป
myobj = {
    'message_key': 'message_val',
    'msg': msg,  # ใช้ข้อความที่ผู้ใช้ป้อน
    'ผู้รับ': recipient,  # ชื่อผู้รับ
    'ip': ip,  # IP ของผู้รับ
    'ผู้ส่ง': sender  # ชื่อผู้ส่ง
}

# แสดงข้อมูลก่อนส่ง
print("\nกำลังส่งข้อความ... \n")
print(f"ข้อมูลที่ส่งไป: ")
print(f"----------------------------")
print(f"ผู้ส่ง: {sender}")
print(f"ผู้รับ: {recipient}")
print(f"IP ของผู้รับ: {ip}")
print(f"ข้อความที่ส่ง: {msg}")
print(f"----------------------------\n")

# ส่งคำขอ POST
x = requests.post(url, data=json.dumps(myobj))

# ตรวจสอบผลลัพธ์และแสดงผล
if x.status_code == 200:
    print(f"การส่งข้อความสำเร็จ! คำตอบจาก API: {x.text}")
else:
    print(f"[ERROR] การส่งข้อความล้มเหลว! รหัสสถานะ: {x.status_code}")