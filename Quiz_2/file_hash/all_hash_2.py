# รวมแนวโจทย์ HASH ระดับและสไตล์เดียวกับการบ้าน Grader (ไม่ซ้ำชุดเดิม)
# สไตล์: input().split() บรรทัดเดียว, โค้ด 10-15 บรรทัด, Output 2 บรรทัดเสมอ
# อ้างอิงทฤษฎีจากสไลด์: 09,12-Binary Tree and Traversal.pdf

# ==============================================================================
# ข้อที่ 1: Mid-Square Hash แบบระบุขนาดตาราง (ยกกำลัง ตัดกลาง แล้ว mod)
# ==============================================================================

# [คำอธิบายโจทย์]
# - รับ input บรรทัดเดียว: key, m_len (จำนวนตัวกลาง), table_size
# - นำ key ยกกำลังสอง (key ** 2)
# - ดึงตัวเลขตรงกลางตามความยาว m_len (ปัดเศษลงถ้าไม่ลงตัว)
# - บรรทัดที่ 1: แสดงตัวเลขตรงกลางที่ตัดออกมา
# - บรรทัดที่ 2: แสดงตำแหน่งช่องแฮช (ตัวกลาง mod ด้วย table_size)

# [ตัวอย่าง Input]
# 44 2 11
# (44^2 = 1936, ดึงตัวกลาง 2 หลักได้ '93', ขนาดตารางคือ 11)

# [ตัวอย่าง Output]
# 93
# 5
# (93 mod 11 ได้เศษ 5)
# ==============================================================================
def q1_midsquare_to_slot():
    key, m_len, table_size = map(int, input().split())

    # ยกกำลัง 2 ตามทฤษฎี Mid-Square ในสไลด์
    squared_str = str(key ** 2)
    total_len = len(squared_str)

    # หาตำแหน่งตัดกลางเหมือนการบ้านข้อ EX_25
    start_idx = (total_len - m_len) // 2
    middle_str = squared_str[start_idx:start_idx + m_len]

    middle_val = int(middle_str)
    slot = middle_val % table_size

    print(middle_str)
    print(slot)


# ==============================================================================
# ข้อที่ 2: Folding Hash แบบระบุขนาดตาราง (พับแบ่งช่วง รวมกัน แล้ว mod)
# ==============================================================================
# [สไตล์เดียวกับการบ้าน EX_24_Folding + สไลด์หน้า 8]
# - เป็นการต่อยอดจากการบ้านข้อ 1: เมื่อตัดแบ่งช่วงตัวเลขและบวกกันเสร็จแล้ว
#   ให้นำผลรวมนั้นมา mod ด้วยขนาดตารางแฮช เพื่อหา slot จริง
#
# [คำอธิบายโจทย์]
# - รับ input บรรทัดเดียว: ชุดตัวเลขยาว (num), ขนาดช่วงพับ (fold_size), ขนาดตาราง (table_size)
# - ตัดแบ่งตัวเลขเป็นช่วงๆ ตาม fold_size และหาผลรวม
# - บรรทัดที่ 1: แสดงผลรวมของท่อนที่แบ่งได้
# - บรรทัดที่ 2: แสดงตำแหน่งช่องแฮช (ผลรวม mod ด้วย table_size)
#
# [ตัวอย่าง Input]
# 4365554698 3 11
# (แบ่งทีละ 3 หลัก: 436 + 555 + 469 + 8 = 1468, ขนาดตาราง 11)
#
# [ตัวอย่าง Output]
# 1468
# 5
# (1468 mod 11 ได้เศษ 5)
# ==============================================================================
def q2_folding_to_slot():
    num, fold_size_str, table_size_str = input().split()
    fold_size = int(fold_size_str)
    table_size = int(table_size_str)

    chunks = []
    for i in range(0, len(num), fold_size):
        chunks.append(num[i:i + fold_size])

    total_sum = sum(map(int, chunks))
    slot = total_sum % table_size

    print(total_sum)
    print(slot)


# ==============================================================================
# ข้อที่ 3: ASCII Mod แต่ละตัวแล้วแสดงผล (Character Remainder Mapping)
# ==============================================================================
# [สไลด์หน้า 10: เรื่องการแปลง ASCII รายตัว]
# - รับข้อความ 1 คำ และขนาดตารางแฮช
# - บรรทัดที่ 1: แสดงค่า mod ของตัวอักษรแต่ละตัว (ord(char) % table_size) คั่นด้วย space
# - บรรทัดที่ 2: แสดงผลรวมของเศษทั้งหมด mod ด้วย table_size อีกรอบ
#
# [ตัวอย่าง Input]
# cat 11
# (ord: c=99, a=97, t=116 -> 99%11=0, 97%11=9, 116%11=6)
#
# [ตัวอย่าง Output]
# 0 9 6
# 4
# (ผลรวม 0 + 9 + 6 = 15, นำ 15 % 11 ได้เศษ 4)
# ==============================================================================
def q3_char_mod_mapping():
    text, table_size_str = input().split()
    table_size = int(table_size_str)

    mod_list = []
    for char in text:
        remainder = ord(char) % table_size
        mod_list.append(str(remainder))

    final_slot = sum(map(int, mod_list)) % table_size

    print(" ".join(mod_list))
    print(final_slot)


# ==============================================================================
# ข้อที่ 4: ตรวจสอบการชนตัวแรก (First Collision Detector)
# ==============================================================================
# [สไลด์หน้า 6: หัวข้อการเกิดการชนกันครั้งแรก]
# - รับชุดตัวเลขเข้ามาเรื่อยๆ โดยตัวเลขสุดท้ายคือขนาดตาราง (table_size)
# - นำแต่ละตัวมา mod หาช่อง ถ้าเจอตัวแรกที่ซ้ำกับช่องที่มีอยู่แล้ว ให้หยุดทันที
# - บรรทัดที่ 1: แสดงเลข key ตัวแรกที่ชน และเลขช่องที่เกิดการชน
# - บรรทัดที่ 2: แสดงเลข key ตัวก่อนหน้าที่เคยจองช่องนั้นไว้
#   (ถ้าไม่มีการชนเลย ให้พิมพ์คำว่า "No Collision")
#
# [ตัวอย่าง Input]
# 54 26 93 17 77 31 44 55 11
# (77 ลงช่อง 0, ต่อมา 44 mod 11 ได้ 0 ชนกับ 77)
#
# [ตัวอย่าง Output]
# Key 44 collided at slot 0
# Previous key: 77
# ==============================================================================
def q4_first_collision():
    data = list(map(int, input().split()))
    items = data[:-1]
    table_size = data[-1]

    table = [None] * table_size
    has_collision = False

    for item in items:
        slot = item % table_size
        if table[slot] is not None:
            # เจอการชนตัวแรกแล้ว
            print("Key " + str(item) + " collided at slot " + str(slot))
            print("Previous key: " + str(table[slot]))
            has_collision = True
            break
        else:
            table[slot] = item

    if not has_collision:
        print("No Collision")


# ==============================================================================
# จุดสลับเลือกรันข้อสอบใน VS Code
# (เวลาต้องการใช้ข้อไหน ให้ลบเครื่องหมาย # หน้าข้อนั้นออก แล้วกด Run)
# ==============================================================================
if __name__ == '__main__':
    # q1_midsquare_to_slot()
    # q2_folding_to_slot()
    # q3_char_mod_mapping()
    # q4_first_collision()
    pass