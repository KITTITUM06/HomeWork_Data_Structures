# ==============================================================================
# quiz_hash_table_slide_detailed.py
# อ้างอิงจากสไลด์สอนที่มีโน้ตสีแดง: ⭐ Quiz Hash และตัวอย่างการใช้งาน HashTable
# ==============================================================================


# ==============================================================================
# รูปแบบที่ 1: สไตล์การบ้าน Grader (รับค่าบรรทัดเดียว -> Output 2 บรรทัด)
# ==============================================================================
# [คำอธิบายโจทย์อย่างละเอียด]
# ให้จำลองการทำงานของ HashTable ตามสไลด์ โดยมีอาเรย์คู่ขนาน 2 ตัว:
# 1. slots: เก็บตัวระบุตำแหน่ง (Key)
# 2. data : เก็บข้อมูลจริง (Value)
#
# เงื่อนไขการทำงาน (ตามโน้ตอาจารย์):
# - ฟังก์ชันแฮช: ถ้า Key เป็นตัวเลขใช้ key % size, ถ้าเป็นข้อความใช้ผลรวม ASCII % size
# - การชน (Collision): ถ้าช่องนั้นมี Key อื่นอยู่แล้ว ให้ทำ rehash ขยับไปทีละ 1 ช่อง
# - การอัปเดต (#replace): ถ้า Key ที่ใส่เข้ามาซ้ำกับ Key ที่มีอยู่แล้วในตาราง
#   ให้เขียนทับข้อมูลในอาเรย์ data ทันทีโดยไม่ต้องขยับหาช่องใหม่
#
# [การแจกแจง Input]
# รับข้อมูลในบรรทัดเดียว คั่นด้วย spacebar
# - ข้อมูลคู่ Key:Value เช่น 54:cat 26:dog ...
# - ตัวเลขตัวสุดท้ายเดี่ยวๆ คือ ขนาดของตาราง (Table Size)
#
# [การแจกแจง Output]
# บรรทัดที่ 1: แสดงอาเรย์ slots (รายชื่อ Key ทั้งหมดที่อยู่ในตาราง)
# บรรทัดที่ 2: แสดงอาเรย์ data (รายชื่อ Value ทั้งหมดที่ตรงกับ Key ใน slots)
#
# [ตัวอย่าง Input]
# 54:cat 26:dog 93:lion 17:tiger 77:bird 31:cow 44:goat 55:pig 20:chicken 20:duck 11
# (สังเกต: มีการใส่ 20:chicken แล้วตามด้วย 20:duck เพื่อทดสอบเงื่อนไข #replace)
#
# [การคำนวณเบื้องหลัง (Trace)]
# ขนาดตาราง = 11
# - 54 % 11 = 10 -> slots[10]=54, data[10]='cat'
# - 26 % 11 = 4  -> slots[4]=26,  data[4]='dog'
# - 93 % 11 = 5  -> slots[5]=93,  data[5]='lion'
# - 17 % 11 = 6  -> slots[6]=17,  data[6]='tiger'
# - 77 % 11 = 0  -> slots[0]=77,  data[0]='bird'
# - 31 % 11 = 9  -> slots[9]=31,  data[9]='cow'
# - 44 % 11 = 0  -> ชนช่อง 0 -> ขยับไปช่อง 1 -> slots[1]=44, data[1]='goat'
# - 55 % 11 = 0  -> ชนช่อง 0, 1 -> ขยับไปช่อง 2 -> slots[2]=55, data[2]='pig'
# - 20 % 11 = 9  -> ชนช่อง 9, 10, 0, 1, 2 -> ลงช่อง 3 -> slots[3]=20, data[3]='chicken'
# - 20:duck      -> Key 20 มีอยู่แล้วที่ช่อง 3 -> ทำ #replace -> data[3]='duck'
#
# [ตัวอย่าง Output]
# [77, 44, 55, 20, 26, 93, 17, None, None, 31, 54]
# ['bird', 'goat', 'pig', 'duck', 'dog', 'lion', 'tiger', None, None, 'cow', 'cat']
# ==============================================================================
def run_hash_table_grader_style():
    raw_inputs = input().split()
    table_size = int(raw_inputs[-1])
    pairs = raw_inputs[:-1]

    slots = [None] * table_size
    data = [None] * table_size

    for p in pairs:
        key_str, val = p.split(":")
        # เช็กว่าเป็น Key ตัวเลข หรือ ตัวอักษร
        key = int(key_str) if key_str.lstrip('-').isdigit() else key_str

        # 1. ฟังก์ชันแฮชเริ่มต้น (hashfunction)
        if isinstance(key, int):
            pos = key % table_size
        else:
            pos = sum(ord(c) for c in key) % table_size

        # 2. แก้การชน (rehash) หรือ ตรวจสอบการซ้ำ (#replace)
        steps = 0
        while slots[pos] is not None and slots[pos] != key and steps < table_size:
            pos = (pos + 1) % table_size  # rehash ขยับทีละ 1
            steps += 1

        # บันทึก Key และ Value ลงตำแหน่งที่หาได้
        slots[pos] = key
        data[pos] = val

    # แสดงผล 2 บรรทัดตรงตามภาพผลลัพธ์ในสไลด์
    print(slots)
    print(data)


# ==============================================================================
# รูปแบบที่ 2: โครงสร้างแบบ Class เต็มรูป ตรงตามสไลด์ ⭐ Quiz Hash
# ==============================================================================
# [คำอธิบาย]
# ใช้ในกรณีที่ข้อสอบกำหนดหัวคลาสมาให้เติมโค้ด หรือให้อิมพลีเมนต์ทั้งคลาส
# เมธอดสำคัญ:
# - hashfunction: คำนวณ Key % Size
# - rehash: สูตรจัดการชน (oldhash + 1) % size
# - put: ตรวจสอบช่องว่าง / เขียนทับข้อมูลเดิม (#replace)
# - get: เดินค้นหา Key ตามรอย rehash
# ==============================================================================
class HashTable:
    def __init__(self, size=11):
        self.size = size
        self.slots = [None] * self.size  # เก็บ Key
        self.data = [None] * self.size   # เก็บ Data / Value

    def hashfunction(self, key, size):
        if isinstance(key, str):
            return sum(ord(c) for c in key) % size
        return key % size

    def rehash(self, oldhash, size):
        # โน้ตอาจารย์: "แก้การชน -> แก้ตรงนี้" (ถ้าโจทย์สั่งขยับก้าวอื่น ให้แก้ตัวเลข + 1)
        return (oldhash + 1) % size

    def put(self, key, data):  # เขียนข้อมูล
        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue] is None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  # replace อัปเดตข้อมูลเดิม
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))
                while self.slots[nextslot] is not None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))

                if self.slots[nextslot] is None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data  # replace อัปเดตข้อมูลเดิม

    def get(self, key):  # ค้นหาข้อมูล
        startslot = self.hashfunction(key, len(self.slots))
        data = None
        stop = False
        found = False
        position = startslot

        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
                
# ==============================================================================
# quiz2_hash_table_slide_detailed.py
# โจทย์ Hash Table แบบจับคู่ Key-Data (อิงตามสไลด์ ⭐ Quiz Hash และ ใช้งาน HashTable)
# ==============================================================================


# ==============================================================================
# ข้อที่ 1: [HASH TABLE แบบ CLASS] อิมพลีเมนต์ตามสไลด์อาจารย์
# ==============================================================================
# [คำอธิบายการทำงาน]
# โครงสร้างตารางจะประกอบด้วย 2 ลิสต์ขนานกัน:
# 1. self.slots ทำหน้าที่เก็บค่า Key (รองรับทั้ง int และ string)
# 2. self.data ทำหน้าที่เก็บค่า Value / Data
#
# เมธอดสำคัญ:
# - hashfunction(key, size): ถ้า key เป็นเลข ใช้ key % size
#                            ถ้า key เป็นข้อความ ให้นำค่า ASCII มารวมกันแล้ว % size
# - rehash(oldhash, size): เลื่อนตำแหน่งเมื่อชนด้วย (oldhash + 1) % size
# - put(key, data): นำคู่ key-data ไปใส่ หากชนให้ rehash ไปเรื่อยๆ
#                   *หากพบ key เดิมซ้ำ ให้แทนที่ (replace) ข้อมูลเก่าด้วย data ใหม่ทันที
# - get(key): ค้นหาค่า data จาก key ที่ระบุ หากไม่พบให้คืนค่า None
# ==============================================================================
class MyHashTable:
    def __init__(self, size=11):
        self.size = size
        self.slots = [None] * self.size  # ตารางเก็บ Key
        self.data = [None] * self.size   # ตารางเก็บ Data

    def hashfunction(self, key, size):
        if isinstance(key, str):
            return sum(ord(ch) for ch in key) % size
        return key % size

    def rehash(self, oldhash, size):
        # จุดปรับแต่งการก้าวข้าม (skip) กรณีโจทย์เปลี่ยนระยะกระโดด
        return (oldhash + 1) % size

    def put(self, key, data):
        hv = self.hashfunction(key, len(self.slots))

        if self.slots[hv] is None:
            self.slots[hv] = key
            self.data[hv] = data
        elif self.slots[hv] == key:
            self.data[hv] = data  # อัปเดตข้อมูลทับเมื่อ key ซ้ำ
        else:
            nxt = self.rehash(hv, len(self.slots))
            while self.slots[nxt] is not None and self.slots[nxt] != key:
                nxt = self.rehash(nxt, len(self.slots))

            if self.slots[nxt] is None:
                self.slots[nxt] = key
                self.data[nxt] = data
            else:
                self.data[nxt] = data  # อัปเดตข้อมูลทับเมื่อ key ซ้ำ

    def get(self, key):
        start = self.hashfunction(key, len(self.slots))
        pos = start
        while self.slots[pos] is not None:
            if self.slots[pos] == key:
                return self.data[pos]
            pos = self.rehash(pos, len(self.slots))
            if pos == start:
                break
        return None

    def __setitem__(self, key, data):
        self.put(key, data)

    def __getitem__(self, key):
        return self.get(key)


# ==============================================================================
# ข้อที่ 2: [HASH TABLE แบบ GRADER SCRIPT] สไตล์การบ้านรับส่งผ่าน input()
# ==============================================================================
# [คำอธิบายโจทย์และการรับ Input]
# รับข้อมูลคู่ "Key:Value" หลายๆ คู่ และตัวสุดท้ายคือ "ขนาดตาราง" ในบรรทัดเดียว คั่นด้วย spacebar
#
# [ตัวอย่าง Input]
# 54:cat 26:dog 93:lion 17:tiger 77:bird 31:cow 44:goat 55:pig 20:chicken 20:duck 11
#
# [ความหมายของ Input]
# - ชุดคู่ข้อมูล: 54:cat, 26:dog, ..., 20:duck (สังเกตว่ามี key 20 เข้ามาซ้ำเพื่อทดสอบการ replace)
# - ตัวเลขตัวสุดท้าย: 11 คือขนาดตารางแฮช (table_size)
#
# [การทำงานเบื้องหลัง (Trace)]
# 1. 77 % 11 = 0 -> ลงช่อง 0 (bird)
# 2. 44 % 11 = 0 -> ชนช่อง 0 เลื่อนไปช่อง 1 (goat)
# 3. 55 % 11 = 0 -> ชนช่อง 0, 1 เลื่อนไปช่อง 2 (pig)
# 4. 20 % 11 = 9 -> แต่เมื่อใส่ 54, 26, 93, 17 ลงไปก่อน จะเกิดการชนและเลื่อนไปช่องว่าง
# 5. เมื่อพบ 20:duck ซ้ำกับ key 20 เดิม -> ระบบจะอัปเดต value จาก 'chicken' เป็น 'duck' ทันที
#
# [รูปแบบ Output]
# บรรทัดที่ 1: แสดงรายการ Key ใน self.slots ทั้งหมด คั่นด้วยเว้นวรรค
# บรรทัดที่ 2: แสดงรายการ Data ใน self.data ทั้งหมด คั่นด้วยเว้นวรรค
#
# [ตัวอย่าง Output]
# 77 44 55 20 26 93 17 None None 31 54
# bird goat pig duck dog lion tiger None None cow cat
# ==============================================================================
def run_grader_hash_table():
    raw_inputs = input().split()
    table_size = int(raw_inputs[-1])
    pairs = raw_inputs[:-1]

    slots = [None] * table_size
    data = [None] * table_size

    for item in pairs:
        k_str, v_str = item.split(":")
        # ตรวจสอบว่าเป็น key ตัวเลขหรือตัวอักษร
        key = int(k_str) if k_str.isdigit() else k_str

        # คำนวณตำแหน่งเริ่มต้น
        if isinstance(key, int):
            pos = key % table_size
        else:
            pos = sum(ord(c) for c in key) % table_size

        # ตรวจสอบการชน หรือ ค้นหา key เดิมเพื่ออัปเดตค่า
        steps = 0
        while slots[pos] is not None and slots[pos] != key and steps < table_size:
            pos = (pos + 1) % table_size
            steps += 1

        # บันทึกหรือแทนที่ข้อมูล
        slots[pos] = key
        data[pos] = v_str

    # แสดงผลลัพธ์ 2 บรรทัด
    print(" ".join(map(str, slots)))
    print(" ".join(map(str, data)))


# ==============================================================================
# จุดสลับเลือกรันใน VS Code
# ==============================================================================
if __name__ == '__main__':
    # 1. ทดสอบแบบ Class ตามสไลด์รูปที่ 2:
    ht = MyHashTable(11)
    sample_pairs = [
        (54, "cat"), (26, "dog"), (93, "lion"), (17, "tiger"),
        (77, "bird"), (31, "cow"), (44, "goat"), (55, "pig"), (20, "chicken")
    ]
    for k, v in sample_pairs:
        ht[k] = v

    ht[20] = "duck"  # ทดสอบการ replace

    print("--- ผลลัพธ์การทดสอบแบบ Class ---")
    print("slots:", ht.slots)
    print("data: ", ht.data)
    print("Get Key 20:", ht[20])  # คืนค่า duck
    print("Get Key 99:", ht[99])  # คืนค่า None

    # 2. ปลดคอมเมนต์ด้านล่างหากต้องการรันทดสอบส่ง Grader:
    # run_grader_hash_table()